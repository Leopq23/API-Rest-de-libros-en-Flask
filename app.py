from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
      conn = sqlite3.connect("libros.sqlite")
    except sqlite3.error as e:
      print(e)
    return conn

books_list = [
  {
    "id": 1,
    "nombre": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año_publicacion": 1967
  },
  {
    "id": 2,
    "nombre": "Don Quijote de la Mancha",
    "autor": "Miguel de Cervantes",
    "año_publicacion": 1605
  },
  {
    "id": 3,
    "nombre": "Orgullo y prejuicio",
    "autor": "Jane Austen",
    "año_publicacion": 1813
  },
  {
    "id": 4,
    "nombre": "1984",
    "autor": "George Orwell",
    "año_publicacion": 1949
  },
  {
    "id": 5,
    "nombre": "El gran Gatsby",
    "autor": "F. Scott Fitzgerald",
    "año_publicacion": 1925
  },
  {
    "id": 6,
    "nombre": "Matar a un ruiseñor",
    "autor": "Harper Lee",
    "año_publicacion": 1960
  },
  {
    "id": 7,
    "nombre": "Crimen y castigo",
    "autor": "Fiódor Dostoyevski",
    "año_publicacion": 1866
  },
  {
    "id": 8,
    "nombre": "La Odisea",
    "autor": "Homero",
    "año_publicacion": -700
  },
  {
    "id": 9,
    "nombre": "El señor de los anillos",
    "autor": "J.R.R. Tolkien",
    "año_publicacion": 1954
  },
  {
    "id": 10,
    "nombre": "Harry Potter y la piedra filosofal",
    "autor": "J.K. Rowling",
    "año_publicacion": 1997
  }
]

@app.route("/libros", methods=["GET","POST"])
def libros():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM libro")
        libros = [
            dict(id=row[0], nombre=row[1], autor=row[2], año_publicacion=row[3])
            for row in cursor.fetchall()
        ]
        if libros is not None:
            return jsonify(libros)

    if request.method == "POST":
        nuevo_autor = request.form["autor"]
        nuevo_año = request.form["año_publicacion"]
        nuevo_titulo = request.form["nombre"]
        sql = """ INSERT INTO libro (nombre, autor, año_publicacion)
                  VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql, (nuevo_titulo, nuevo_autor, nuevo_año))
        conn.commit()
        return f"Libro con el id: {cursor.lastrowid} se ha creado exitosamente"
    
@app.route("/libros/<int:id>", methods=["GET","PUT","DELETE"])
def libro(id): 
    conn = db_connection()
    cursor = conn.cursor()
    libro = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM libro WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            libro = r
        if libro is not None:
            return jsonify(libro), 200
        else:
            return "No se encontro el libro", 404
        
    if request.method == "PUT":
        sql = """ UPDATE libro
                  SET nombre=?,
                      autor=?,
                      año_publicacion=?
                  WHERE id=? """
        autor = request.form["autor"]
        nombre = request.form["nombre"]
        año_publicacion = request.form["año_publicacion"]
        libro_actualizado = {
              "id": id,
              "nombre": nombre,
              "autor": autor,
              "año_publicacion": año_publicacion
        }
        conn.execute(sql, (nombre, autor, año_publicacion, id))
        conn.commit()
        return jsonify(libro_actualizado)
            
    if request.method == "DELETE":
        sql = """ DELETE FROM libro WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "El libro con id: {} fue eliminado".format(id), 200



if __name__ == '__main__':
    app.run()

