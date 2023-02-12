import time

from http.server import BaseHTTPRequestHandler, HTTPServer
from mysql.connector.connection_cext import CMySQLConnection, CMySQLCursor

from db_conn import get_db_conn, get_db_cursor

HEALTHCHECKD_QUERY = "SELECT 1;"

class MySQLSimpleHealthcheckHTTPRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path != "/":
      self.send_error(404, "Not Found")
      return
      
    db_cursor = get_db_cursor()

    if type(db_cursor) != CMySQLCursor:
      db_result = db_cursor
    else:
      db_cursor.execute(HEALTHCHECKD_QUERY)

      # Raw result should be a list of tuples - e.g. [(1,)]
      # I will print the query along with the result to HTML
      # Expected result: query = SELECT 1; result = [(1,)]
      db_result = f"query = {HEALTHCHECKD_QUERY} result = {db_cursor.fetchall()}"
      db_cursor.close()
    
    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.end_headers()

    self.wfile.write(db_result.encode("utf-8"))

def run_http_server(host, port):
  print(f"{time.asctime()} Starting MySQL health check HTTP endpoint at http://{host}:{port}/")
  http_server = HTTPServer((host, int(port)), MySQLSimpleHealthcheckHTTPRequestHandler)

  try:
    http_server.serve_forever()
  except KeyboardInterrupt:
    print(f"{time.asctime()} Stopping MySQL health check HTTP endpoint at http://{host}:{port}/")
    http_server.server_close()
