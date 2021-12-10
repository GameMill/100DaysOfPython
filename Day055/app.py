import flask

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>";
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>";
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>";
    return wrapper


app = flask.Flask("__main__")

@app.route('/')
def home_page():
    return "<h1>Hello World</h1>"

@app.route('/<int:id>/hello')
def Test(id):
    return str(id)
    
@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"





if __name__ == "__main__":
    app.run(debug=True)
    