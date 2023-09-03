import re

from collections.abc import Callable
from ftplib import FTP, FTP_TLS, error_reply, error_perm
from tempfile import TemporaryFile
from typing import Generator

class FTPWorker:
    def __init__(self, ftp: FTP, remote_dir: str) -> None:
        self.ftp = ftp
        ftp.cwd(remote_dir)


    def process_file(self, filename: str, callback: Callable[[], None]) -> None:
        with TemporaryFile() as tf:
            self.ftp.retrbinary(f"RETR {filename}", callback=tf.write)
            callback(tf)
            

    def search_files(self, pattern: str) -> Generator[str, None, None]:
        rx = re.compile(pattern)
        return (x for x, y in self.ftp.mlsd() if rx.match(x))
