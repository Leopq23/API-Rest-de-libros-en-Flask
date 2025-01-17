import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

conn = pymysql.connect(
    host=DB_HOST,
    database='sql10758209',
    user=DB_USER,
    password=DB_PASSWORD,
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
