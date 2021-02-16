from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    resp = {'code': '200', 'message': 'blue/green deployment successfully executed!'}
    return jsonify(resp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)