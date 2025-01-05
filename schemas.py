from marshmallow import Schema, fields


class BooksSchema(Schema):
    id = fields.Integer(dump_only=True)
    book_name = fields.Str(required=True)
    description = fields.Str(required=True)
    genre = fields.Str(required=True)
    title = fields.Str(required=True)


class BookUpdateSchema(Schema):
    book_name = fields.Str(required=True)
    description = fields.Str(required=True)
    genre = fields.Str(required=True)
    title = fields.Str(required=True)

class BooksCreateSchema(Schema):
    id = fields.Integer(dump_only=True)
    book_name = fields.Str(required=True)
    description = fields.Str(required=True)
    genre = fields.Str(required=True)
    title = fields.Str(required=True)

class BooksDeleteSchema(Schema):
    message = fields.Str(required=True)
