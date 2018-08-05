from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DATETIME, default=datetime.now, nullable=False)
    modified_at = db.Column(db.DATETIME, default=datetime.now, nullable=False)
    title = db.Column(db.String(128))
    content = db.Column(db.String(256))


@app.route('/')
def blog_list():
    title = "List"
    # データベースから取得してデータを渡す
    return render_template('index.html', title=title)


@app.route('/detail')
def detail():
    title = "Detail"
    return render_template('detail.html', title=title)


@app.route('/post')
def post():
    title = "Post"
    return render_template('post.html', title=title)


@app.route('/edit')
def edit():
    title = "Edit"
    return render_template('edit.html', title=title)



if __name__ == '__main__':
    app.run(debug=True)

