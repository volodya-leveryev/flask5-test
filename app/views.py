from flask import render_template

from .models import Post


def index_page():
    posts = Post.query.order_by(Post.created).all()
    return render_template("index.html", posts=posts)


def post_page(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post)
