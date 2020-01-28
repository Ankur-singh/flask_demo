from flask import Flask

app = Flask(__name__)

## Simple route
@app.route('/')
def index():
    return '<h1>This is the INDEX Page.</h1>'

## some more route
@app.route('/rahul')
def result():
    return "<h1>This is the Rahul's Page.</h1>"

## Dynamic route
@app.route('/<string:name>')
def profile(name):
    # name = name.capitalize()
    return f"<h1>This is the {name}'s profile.</h1>"

if __name__ == '__main__':
    app.run(debug=True)