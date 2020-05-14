
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/ria')
def hello():
    return 'Hello, ria!'
app.run(debug=True,port=0)
