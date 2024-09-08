from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)
@app.route('/index/', methods=['GET'])
def index():
    return render_template('mic1.html')


if '__name__'=='__main__':
    app.run()