import pymysql

conn = pymysql.connect(
    host='sql10.freesqldatabase.com',
    database='sql10758209',
    user='sql10758209',
    password='HcG72ZE88C',
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
