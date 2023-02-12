# mysql-simple-healthcheckd

A simple HTTP endpoint which can be used by load balancers and proxies for MySQL health check. Created using the Python 3 simple HTTP server module.

## Usage

1. Clone this repo.

```
git clone https://github.com/tqn-org/mysql-simple-healthcheckd.git
cd ./mysql-simple-healthcheckd
```

2. Create a python venv and install required libraries.

```
python3 -m venv .
source ./bin/activate
pip3 install -r ./requirements.txt
```

3. Clone the configuration file and customise to your environment. Refer to the [Configuration file customisation](#configuration-file-customisation) section for further details.

```
cp ./conf.d/healthcheckd_conf_example ./conf.d/healthcheckd_conf
vim ./conf.d/healthcheckd_conf
```

4. Try it out!

```
python3 main.py [-c FILE]
```

mysql-simple-healthcheckd should state that a HTTP endpoint has been started, as per below.

```
Sun Feb 12 11:16:29 2023 Starting MySQL health check HTTP endpoint at http://0.0.0.0:64444/
```

## Supported flags and arguments

| Flag | Argument | Description | Default value |
|-|-|-|-|
| `-c`, `--config` | `FILE` | Specify the path to mysql-simple-healthcheckd configuration file | ./conf.d/healthcheckd_conf |
| `-h`, `--help` | | Display help message | |

## Configuration file customisation

An example configuration is already provided to be cloned and customised.

```
[healthcheckd]
http_host   = 0.0.0.0
http_port   = 64444
db_host     = localhost
db_port     = 3306
db_username = healthcheck
db_password = healthcheckExamplePa$$w0rd
db_database = db_name_or_left_blank
```

The section `[healthcheckd]` must be presented at the top of the configuration file.

| Key | Type | Description | Example values |
|-|-|-|-|
| `http_host` | string | The IP/FQDN that the HTTP endpoint uses (default: 0.0.0.0) | 0.0.0.0, 192.0.2.10, healthcheckd.example.com |
| `http_port` | integer | The port (from 0 to 65535) that the HTTP endpoint listens to (default: 64444) | 64444, 80, 8080 |
| `db_host` | string | The IP/FQDN of the database server that mysql-simple-healthcheckd connects to | 192.0.2.11, localhost, db-server.example.com |
| `db_port` | integer | The port on the database server (from 0 to 65535) that mysql-simple-healthcheckd connects to | 3306, 6446 |
| `db_username` | string | The username used for connecting to the database server | healthcheck |
| `db_password` | string | The plaintext password for the above username | healthcheckExamplePa$$w0rd |
| `db_database` | string | The database name to be used once the connection is established. Can be left blank | healthcheck_db |