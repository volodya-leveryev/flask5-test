from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .models import db, Post

admin = Admin()
admin.add_view(ModelView(Post, db.session))
