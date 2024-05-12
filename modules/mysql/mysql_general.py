import mysql.connector
from data.server.mysql_config import mysql_config

def connect_to_db():
    connection = mysql.connector.connect(
        host=mysql_config["host"],
        user=mysql_config["user"],
        password=mysql_config["password"],
        database=mysql_config["db"]
    )
    return connection


