import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Test route
def hello_world():
    return "Hello, world!"

app.add_url_rule('/', 'hello', hello_world)

if __name__ == '__main__':
    app.run()