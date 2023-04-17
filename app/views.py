from flask import render_template, request

from .forms import CommentForm
from .models import db, Post, Comment


def index_page():
    posts = Post.query.order_by(Post.created).all()
    return render_template("index.html", posts=posts)


def post_page(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            comment = Comment()
            comment.author = form.author.data
            comment.text = form.text.data
            comment.post = post
            db.session.add(comment)
            db.session.commit()
            form = CommentForm()
    return render_template("post.html", post=post, form=form)
