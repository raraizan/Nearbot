#!bin/python
from flask import Flask, jsonify
from random import randint

app = Flask(__name__)

state = [0]
# counter = 0

@app.route('/')
def index():
    # counter += 1
    state.append(randint(0, 10))
    return "State updated with element {}".format(state[-1])

@app.route('/api/v1/historial')
def get_historial():
    return jsonify({
        "historial": state,
        })

@app.route('/api/v1/state')
def get_state():
    return jsonify({
        "current": state[-1],
        })

if __name__ == '__main__':
    app.run(debug=True)