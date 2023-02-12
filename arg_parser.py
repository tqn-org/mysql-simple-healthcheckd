import argparse

from os.path import dirname, join, realpath

DEFAULT_CONFIG_FILE_PATH = "./conf.d/healthcheckd_conf"

def get_args():
  arg_parser = argparse.ArgumentParser(
    prog="python3 main.py",
    description="mysql-simple-healthcheckd - A simple HTTP endpoint which can be used by load balancers and proxies for MySQL health check."
  )

  arg_parser.add_argument(
    "-c", "--config",
    metavar="FILE",
    dest="file",
    help=f"Path to mysql-simple-healthcheckd configuration file (default: {DEFAULT_CONFIG_FILE_PATH})",
    type=argparse.FileType("r"),
    default=realpath(join(dirname(__file__), DEFAULT_CONFIG_FILE_PATH))
  )

  return arg_parser.parse_args()
