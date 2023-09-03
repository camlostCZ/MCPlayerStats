import sys
import datetime

from ftplib import FTP, FTP_TLS, error_reply, error_perm

from config import Configuration, ErrorConfigFile, ErrorEnvSettings
from ftpworker import FTPWorker

from typing import IO


def process_file(fd: IO) -> None:
    fd.seek(0)
    

def collect_stats(cfg: Configuration):
    try:
        with FTP_TLS(cfg.server_name, cfg.username, cfg.password) as ftp:
            ftp_worker = FTPWorker(ftp, cfg.ftp_dir)

            date_str = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
            print(f"Searching for files from {date_str}...")
            pattern = f"^{date_str}"
            for item in ftp_worker.search_files(pattern):
                # TODO Download file
                # TODO Unpack file
                # TODO Process the unpacked file
                # TODO Write event info into DB
                ftp_worker.process_file(item, process_file)
    except error_reply:
        print("Error: Error in FTP communication.", file=sys.stderr)
    except error_perm as e:
        print(f"Error: {e}", file=sys.stderr)
