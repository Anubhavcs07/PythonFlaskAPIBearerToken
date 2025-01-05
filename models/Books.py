from db import db
import uuid

class BooksModel(db.Model):
    __tablename__ = "Books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=True)
    genre = db.Column(db.String(100), unique=False, nullable=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    