# from datetime import date

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    created = db.Column(db.Date())
    comments = db.relationship('Comment', back_populates='post')


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.Text(), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id', name='Post'))
    post = db.relationship('Post', back_populates='comments')
