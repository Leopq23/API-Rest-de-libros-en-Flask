from flask import Flask, request, jsonify

app = Flask(__name__)

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
    if request.method == "GET":
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            "No hay libros", 404

    if request.method == "POST":
        nuevo_autor = request.form["autor"]
        nuevo_año = request.form["año_publicacion"]
        nuevo_titulo = request.form["nombre"]
        iD = books_list[-1]["id"]+1

        nuevo_objeto = {
            "id": iD,
            "nombre": nuevo_titulo,
            "autor": nuevo_autor,
            "año_publicacion": nuevo_año
        }
        books_list.append(nuevo_objeto)
        return jsonify(books_list), 201
    
@app.route("/libros/<int:id>", methods=["GET","PUT","DELETE"])
def libro(id): 
    if request.method == "GET":
        for book in books_list:
            if book["id"] == id:
                return jsonify(book)
            pass
    if request.method == "PUT":
        for book in books_list:
            if book["id"] == id:
                book["autor"] = request.form["autor"]
                book["nombre"] = request.form["nombre"]
                book["año_publicacion"] = request.form["año_publicacion"]
                libro_actualizado = {
                    "id": id,
                    "autor": book["autor"],
                    "nombre": book["nombre"],
                    "año_publicacion": book["año_publicacion"]
                }
                return jsonify(libro_actualizado)
            
    if request.method == "DELETE":
        for index, book in enumerate(books_list):
            if book["id"] == id:
                books_list.pop(index)
                return jsonify(books_list)



if __name__ == '__main__':
    app.run()

