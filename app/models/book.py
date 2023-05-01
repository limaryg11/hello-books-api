from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    def to_dict(self):
        books_as_dict = {}
        books_as_dict["id"] = self.id
        books_as_dict["title"] = self.title
        books_as_dict["description"] = self.description

        return books_as_dict 