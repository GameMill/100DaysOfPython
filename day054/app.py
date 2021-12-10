from flask import Flask
app = Flask(__name__)



@app.route('/') # flask run
def hello_world():
    return 'Hello, World!'

if(__name__ == "__main__"):
    # Running as a script
    app.run()