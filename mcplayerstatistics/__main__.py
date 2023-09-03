import sys

from config import Configuration, ErrorConfigFile, ErrorEnvSettings
from playerstats import collect_stats


PATH_CONFIG = "config.yaml"

try:
    cfg = Configuration()
    cfg.load_config(PATH_CONFIG)

    collect_stats(cfg)
except ErrorConfigFile:
    print("Error: Unable to load configuration.", file=sys.stderr)
except ErrorEnvSettings:
    print("Error: Required system variables not found.", file=sys.stderr) 


