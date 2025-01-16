import sqlite3

conn = sqlite3.connect("libros.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE libro (
    id integer PRIMARY KEY,
    nombre text NOT NULL,
    autor text NOT NULL,
    año_publicacion integer
)"""

cursor.execute(sql_query)
