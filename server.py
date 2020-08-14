from flask import Flask, render_template
from base_name import base

app = Flask(__name__)

@app.route('/')
def main_page():
    return 'MAIN PAGE'



@app.route('/gen', methods=['POST'])
def gen():
    return base()


@app.route('/data')
def do_data():
    return render_template('data.html')

app.run(debug=True)