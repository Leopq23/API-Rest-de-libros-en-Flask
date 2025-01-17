import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

conn = pymysql.connect(
    host=os.getenv('MYSQLHOST'),
    database=os.getenv('MYSQLDATABASE'),
    user=os.getenv('MYSQLUSER'),
    password=os.getenv('MYSQLPASSWORD'),
    port=int(os.getenv('MYSQLPORT')),
    charset='utf8mb4',
    cursorclass= pymysql.cursors.DictCursor
)


cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS libro")

# Crear la tabla con la columna 'id' como autoincremental
sql_query = """CREATE TABLE libro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre TEXT NOT NULL,
    autor TEXT NOT NULL,
    año_publicacion INT
)"""

cursor.execute(sql_query)
conn.close()
