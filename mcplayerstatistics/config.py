import os
import yaml


class ErrorEnvSettings(Exception):
    pass


class ErrorConfigFile(Exception):
    pass


class Configuration:
    def __init(self) -> None:
        self.server_name = ""
        self.port = ""
        self.ftp_dir = ""
        self.username = ""
        self.password = ""
    

    def load_config(self, cfg_path: str) -> None:
        self.load_env_vars()
        self.load_from_file(cfg_path)
        

    def load_from_file(self, cfg_path: str) -> None:
        # Load configuration
        try:
            with open(cfg_path, encoding="utf-8") as cfg_file:
                cfg = yaml.safe_load(cfg_file)

            self.server_name = cfg["HOST"]
            self.port = cfg["PORT"]
            self.ftp_dir = cfg["FTP_PATH"]
        except:
            raise ErrorConfigFile
        

    def load_env_vars(self) -> None:
        # Get secrets
        try:
            self.username = os.environ["USERNAME"]
            self.password = os.environ["PASSWORD"]
        except KeyError:
            raise ErrorEnvSettings


