# API Documentation for Libro API

## Overview
The Libro API is a RESTful service built with Flask that allows users to interact with a MySQL database to manage a collection of books. The API supports operations to create, read, update, and delete (CRUD) book records.

## Endpoints

### 1. `GET /libros`
Retrieves a list of all books in the database.

**Response:**
- **200 OK**: Returns a JSON array of books.
- **500 Internal Server Error**: If the database connection fails.

**Example Response:**
```json
[
    {
        "id": 1,
        "nombre": "Book Title",
        "autor": "Author Name",
        "año_publicacion": 2021
    }
]
```

### 2. `POST /libros`
Adds a new book to the database.

**Request Parameters:**
- `nombre` (string): Title of the book.
- `autor` (string): Author of the book.
- `año_publicacion` (int): Year of publication.

**Response:**
- **201 Created**: Returns a success message with the ID of the newly created book.
- **500 Internal Server Error**: If the database connection fails or the insert operation fails.

**Example Response:**
```
Libro con el id: 1 se ha creado exitosamente
```

### 3. `GET /libros/<int:id>`
Retrieves a specific book by its ID.

**Path Parameters:**
- `id` (int): ID of the book to retrieve.

**Response:**
- **200 OK**: Returns a JSON object of the book.
- **404 Not Found**: If the book with the specified ID does not exist.
- **500 Internal Server Error**: If the database connection fails.

**Example Response:**
```json
{
    "id": 1,
    "nombre": "Book Title",
    "autor": "Author Name",
    "año_publicacion": 2021
}
```

### 4. `PUT /libros/<int:id>`
Updates an existing book by its ID.

**Path Parameters:**
- `id` (int): ID of the book to update.

**Request Parameters:**
- `nombre` (string): New title of the book.
- `autor` (string): New author of the book.
- `año_publicacion` (int): New year of publication.

**Response:**
- **200 OK**: Returns a JSON object of the updated book.
- **404 Not Found**: If the book with the specified ID does not exist.
- **500 Internal Server Error**: If the database connection fails or the update operation fails.

**Example Response:**
```json
{
    "id": 1,
    "nombre": "Updated Book Title",
    "autor": "Updated Author Name",
    "año_publicacion": 2022
}
```

### 5. `DELETE /libros/<int:id>`
Deletes a specific book by its ID.

**Path Parameters:**
- `id` (int): ID of the book to delete.

**Response:**
- **200 OK**: Returns a success message.
- **404 Not Found**: If the book with the specified ID does not exist.
- **500 Internal Server Error**: If the database connection fails or the delete operation fails.

**Example Response:**
```
El libro con id: 1 fue eliminado
```

## Database Setup
The `db.py` script sets up the MySQL database and creates the `libro` table with the following schema:

```sql
CREATE TABLE libro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre TEXT NOT NULL,
    autor TEXT NOT NULL,
    año_publicacion INT
);
```

## Environment Variables
The application relies on the following environment variables for database connection:

- `MYSQLHOST`: Host of the MySQL server.
- `MYSQLDATABASE`: Name of the MySQL database.
- `MYSQLUSER`: MySQL username.
- `MYSQLPASSWORD`: MySQL password.
- `MYSQLPORT`: Port number for the MySQL server.

Ensure these environment variables are correctly set in a `.env` file or the deployment environment.

## Running the Application
To run the application locally:
1. Ensure you have Python and MySQL installed.
2. Set up the `.env` file with the required environment variables.
3. Run `db.py` to set up the database.
4. Start the Flask application using:
   ```bash
   python app.py
   ```
5. The API will be available at `http://localhost:5000/`.

## Notes
- The API uses Flask and PyMySQL for database interactions.
- Error handling is minimal; ensure proper validations and error management in production.

