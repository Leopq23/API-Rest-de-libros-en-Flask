from flask import Flask, request, jsonify
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

app = Flask(__name__)

def db_connection():
    conn = None
    try:
      conn = pymysql.connect(
          host= DB_HOST,
          database='sql10758209',
          user=DB_USER,
          password=DB_PASSWORD,
          charset='utf8mb4',
          cursorclass= pymysql.cursors.DictCursor
      )
    except pymysql.MySQLError as e:
      print(e)
    return conn

@app.route("/libros", methods=["GET","POST"])
def libros():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM libro")
        libros = cursor.fetchall()
        conn.close()
        return jsonify(libros), 200

    if request.method == "POST":
        nuevo_autor = request.form["autor"]
        nuevo_año = request.form["año_publicacion"]
        nuevo_titulo = request.form["nombre"]
        sql = """ INSERT INTO libro (nombre, autor, año_publicacion)
                  VALUES (%s, %s, %s)"""
        cursor.execute(sql, (nuevo_titulo, nuevo_autor, nuevo_año))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return f"Libro con el id: {last_id} se ha creado exitosamente", 201
    
@app.route("/libros/<int:id>", methods=["GET","PUT","DELETE"])
def libro(id): 
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM libro WHERE id=%s", (id,))
        libro = cursor.fetchone()
        conn.close()
        if libro:
            return jsonify(libro), 200
        else:
            return "No se encontro el libro", 404
        
    if request.method == "PUT":
        sql = """ UPDATE libro
                  SET nombre=%s,
                      autor=%s,
                      año_publicacion=%s
                  WHERE id=%s """
        autor = request.form["autor"]
        nombre = request.form["nombre"]
        año_publicacion = request.form["año_publicacion"]
        libro_actualizado = {
              "id": id,
              "nombre": nombre,
              "autor": autor,
              "año_publicacion": año_publicacion
        }
        cursor.execute(sql, (nombre, autor, año_publicacion, id))
        conn.commit()
        conn.close()
        return jsonify(libro_actualizado)
            
    if request.method == "DELETE":
        sql = """ DELETE FROM libro WHERE id=%s """
        cursor.execute(sql, (id,))
        conn.commit()
        return "El libro con id: {id} fue eliminado".format(id), 200



if __name__ == '__main__':
    app.run()

