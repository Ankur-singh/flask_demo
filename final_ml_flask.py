from flask import Flask, render_template, request
from new_iris import train_model
from sklearn.datasets import load_iris
import pickle

app = Flask(__name__)

def load_pickle(filename):
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()
    return model

iris = load_iris()
features = list(iris.feature_names)
targets = list(iris.target_names)

model = load_pickle('pickles/model.pkl')
scaler = load_pickle('pickles/scaler.pkl')

@app.route('/')
def index():
    return '<h1>Hello Everyone</h1>'

@app.route('/random')
def random():
    return render_template('inputs.html', features = features)

@app.route('/predict', methods=["POST"])
def predict():
    ## collecting the inputs
    inputs = []
    for f in features:
        inputs.append(float(request.form.get(f)))
    
    ## make a function if you have multiple preprocessing steps
    x = scaler.transform([inputs])
    result = model.predict(x)[0]
    return targets[result]


if __name__ == '__main__':
    app.run(debug=True)