from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template()


@app.route('/<usr>')
def user(usr):
    return render_template()

# TODO: Nastavka je ovdje: https://youtu.be/9MHYHgh4jYc?t=244

if __name__ == '__main__':
    app.run(debug=True)
