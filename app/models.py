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

    def __str__(self):
        return self.title

    # def __init__(self, *args, **kwargs):
    #     if not self.created:
    #         self.created = date.today()
    #     super(self).__init__(*args, **kwargs)
