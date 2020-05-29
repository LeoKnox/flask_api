from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message='Start programming'), 200

@app.route('/not_found')
def not_found():
    return jsonify(message='Resource won hide and seek'), 404

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message = f"Sorry {name}, you are not old enough."), 401
    else:
        return jsonify(message= f"Welcome {name}, you are old enough.")

@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message = f"Sorry {name}, you are not old enough."), 401
    else:
        return jsonify(message= f"Welcome {name}, you are old enough.")


if __name__ == '__main__':
    app.run()