import mysql.connector

from mysql.connector import errorcode
from mysql.connector.connection_cext import CMySQLConnection

_db_conn = None

def create_db_conn(user, password, host, port=3306, database=""):
  try:
    if int(port) not in range(65536):
      raise OverflowError("port must be 0-65535.")

    return mysql.connector.connect(
      user     = user,
      password = password,
      host     = host,
      port     = port,
      database = database
    )
  except mysql.connector.Error as err:
    err_msg = "Unexpected error occurred."

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      err_msg = "Invalid database credentials."
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      err_msg = "Database does not exist."
    elif err.errno in [
      errorcode.CR_SOCKET_CREATE_ERROR,
      errorcode.CR_CONNECTION_ERROR,
      errorcode.CR_CONN_HOST_ERROR,
      errorcode.CR_IPSOCK_ERROR,
      errorcode.CR_UNKNOWN_HOST,
      errorcode.CR_SERVER_GONE_ERROR,
      errorcode.CR_WRONG_HOST_INFO
    ]:
      err_msg = "Cannot connect to the database at the moment. Please try again later."

    return err_msg

def get_db_conn(config={}):
  global _db_conn
  
  if not _db_conn:
    try:
      _db_conn = create_db_conn(
        user     = config["db_username"],
        password = config["db_password"],
        host     = config["db_host"],
        port     = config["db_port"],
        database = config["db_database"]
        )
      return _db_conn
    except KeyError:
      raise KeyError("Missing or invalid config.")

def get_db_cursor():
  global _db_conn

  if type(_db_conn) != CMySQLConnection:
    return _db_conn

  try:
    _db_conn.connect()
    return _db_conn.cursor()
  except mysql.connector.Error:
    return "Cannot connect to the database at the moment. Please try again later."
    