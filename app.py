from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Set up app and DB path
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Set up SQL Schema


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    content = db.Column(db.String(1000), unique=True)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class NoteSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('title', 'content', 'fname')


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)


# endpoint to create new note
@app.route("/note", methods=["POST"])
def add_note():
    title = request.json['title']
    content = request.json['content']

    new_note = Note(title, content)

    db.session.add(new_note)
    db.session.commit()

    return note_schema.jsonify(new_note)


# endpoint to fetch all notes
@app.route("/note", methods=["GET"])
def get_notes():
    all_notes = Note.query.all()
    result = notes_schema.dump(all_notes)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
