from flask import Flask, render_template
from post import all_posts

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",posts = all_posts)

@app.route('/read/<int:id>')
def read(id):
    return render_template("post.html",post = all_posts[id])



if __name__ == "__main__":
    app.run(debug=True)
