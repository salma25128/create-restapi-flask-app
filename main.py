from flask import Flask, Request
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)


class Books(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'hello '


@app.route('/books')
def get_books():
    books = Books.query.all()
    output = []
    for book in books:
        book_data = {'name': book.name, 'description': book.description}
        
        output.append(book_data)
        

    return {"books": books}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({"name":book.name, "description": book.description})


@app.route('/books', methods=['POST'])
def add_book():
    book = Books(name=request.json['name'], description=request.json['description'])
    db.session.add(book)
    db.session.commit()
    return{'id': book.id}

# TEST ON POSTMAN BY ADD URL / POST REQUEST / JSON 