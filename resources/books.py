import uuid
from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.Books import BooksModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required, get_jwt
from schemas import BooksSchema, BooksCreateSchema, BookUpdateSchema, BooksDeleteSchema

blp = Blueprint("books", __name__, description="Opertaion on book")

@blp.route("/book/<string:id>")
@jwt_required()
class BookList(MethodView):
    @blp.response(200, BooksSchema)
    def get(self,id):
        claims = get_jwt()
        book = BooksModel.query.get(id)
        if not book:
            abort(404, message="Book with this ID does not exist")
        try:
            return book
        except KeyError:
            abort(404, message="Book with this id is not present")

    @blp.response(200, BooksDeleteSchema)
    @jwt_required()
    def delete(self, id):
        book = BooksModel.query.get(id)

        if not book:
            abort(404, message="Book with this ID does not exist")
        try:
            db.session.delete(book)
            db.session.commit()
        except (SQLAlchemyError, IntegrityError) as e:
            db.session.rollback()
            abort(500, message=f"{str(e)}")
    
    @blp.arguments(BookUpdateSchema)
    @blp.response(200, BooksSchema)
    @jwt_required()
    def put(self, request_data, id):        
        book = BooksModel.query.get(id)
        
        if not book:
            abort(404, message="Book with ID doesn't exists")

        book.book_name = request_data.get("book_name", book.book_name)
        book.description = request_data.get("description", book.description)
        book.genre = request_data.get("genre", book.genre)
        book.title = request_data.get("title", book.title)

        try:
            db.session.commit()
        except (SQLAlchemyError, IntegrityError) as e:
            db.session.rollback()
            abort(500, message="An error occur while updating")
        
@blp.route("/book")
class BookDetails(MethodView):
    @blp.response(200, BooksSchema(many=True))
    @jwt_required()
    def get(self):
        book = BooksModel.query.all()
        return book
    
    @blp.arguments(BooksCreateSchema)
    @blp.response(201, BooksSchema)
    @jwt_required()
    def post(self, request_data):
        book = BooksModel(**request_data)
        
        try:
            db.session.add(book)
            db.session.commit()
        except (SQLAlchemyError, IntegrityError) as e:
            print(f"Database error: {str(e)}")
            abort(500, message="An error occur while inserting records")
        return book