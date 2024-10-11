import os
from flask import Flask, jsonify

app = Flask(__name__)

# Lista de libros con enlaces de descarga directa
libros = [
    {
        "name": "Libro 1",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 2",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 3",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 4",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 5",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 6",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 7",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 8",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 9",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 10",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 11",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 12",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 13",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 14",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 15 Христианская",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 16",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 17",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 18",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 19",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 20",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 21",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 22",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 23",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 24",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 25",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 26",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 27",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 28",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    },
{
        "name": "Libro 29 Астрологической код",
        "link": "https://drive.google.com/uc?export=download&id=10J3ESm7PGiAN2tCbq8h7ot9B8LhhGUfj"
    }

   
]

# Ruta para la página principal
@app.route('/')
def home():
    return "<h1>Bienvenido a la API de libros. Visita /books para ver la lista de libros.</h1>"

# Ruta para listar los libros
@app.route('/books')
def list_books():
    return jsonify(libros)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)