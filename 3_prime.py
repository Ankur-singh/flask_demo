from flask import Flask, render_template, request
from prime_new import prime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/prime', methods = ["POST"])
def is_prime_forms():
    number = int(request.form.get('number'))
    return str(prime(number))

if __name__ == '__main__':
    app.run(debug=True)