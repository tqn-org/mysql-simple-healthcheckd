from mysql.connector.connection_cext import CMySQLConnection

from arg_parser import get_args
from config_parser import read_config_file
from db_conn import get_db_conn
from server import run_http_server

def main():
  args = get_args()
  config = read_config_file(args.file)
  db_conn = get_db_conn(config)
  
  run_http_server(
    host = config["http_host"],
    port = config["http_port"]
  )
  
  if type(db_conn) == CMySQLConnection:
    db_conn.close()

if __name__ == "__main__":
  main()