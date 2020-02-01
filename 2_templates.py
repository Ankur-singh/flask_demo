from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

## Rendering html file
@app.route('/')
def index():
    return render_template('index.html')

## Passing values to the front-end
@app.route('/heading')
def heading():
    heading = 'Heading from python'
    return render_template('index2.html', heading = heading)

## Extending base code
@app.route('/extend')
def jinja_extend():
    return render_template('extend.html')

## lists in jinja
@app.route('/list')
def jinja_list():
    names = ['Rahul', 'Gandhi', 'Virat', 'Conor']
    return render_template('list.html', names = names)

## conditions in jinja
@app.route('/condition')
def jinja_conditions():
    day = int(np.random.rand(1) * 10) % 2
    return render_template('condition.html', text = day)

if __name__ == '__main__':
    app.run(debug=True)
