import configparser

from os.path import dirname, join, realpath

EXAMPLE_CONFIG_FILE_PATH = "./conf.d/healthcheckd_conf_example"

def read_config_file(file):
  config_parser = configparser.ConfigParser()

  try:
    config_parser.read_file(file)
    return config_parser["healthcheckd"]
  except configparser.Error:
    err_msg = "Invalid config. Please refer to the example provided below.\n\n"

    with open(realpath(join(dirname(__file__), EXAMPLE_CONFIG_FILE_PATH)), "r") as example_config_file:
      err_msg += f"{example_config_file.read()}\n"

    raise configparser.Error(err_msg)
  finally:
    file.close()
