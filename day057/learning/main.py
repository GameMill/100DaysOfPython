from flask import Flask
from flask.templating import render_template
import random
import datetime
import requests

app = Flask(__name__);

@app.route('/')
def home_page():
    random_number = random.randint(1,10)
    return render_template("index.html",RandomNumber=random_number,year=datetime.datetime.now().year)

@app.route('/guess/<name>')
def guess_page(name):
    if name == "":
        return "404";

    age = requests.get("https://api.agify.io/?name="+name).json()
    gender = requests.get("https://api.genderize.io/?name="+name).json()
    
    return render_template("guess.html",Name=name,age=age,gender=gender)

@app.route('/blog')
def blog():
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)