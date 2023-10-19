from flask import Flask, request, jsonify

app = Flask(__name__) if __name__ == '__main__' else Flask(__name__, instance_relative_config=True)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello World!'})

@app.route('/uploaddata', methods=['POST'])
def uploaddata():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'message': 'Data received!', 'data': data})
    
    return jsonify({'message': 'Data not received!'})

@app.route('/getdata', methods=['POST'])
def getdata():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'message': 'Data received!', 'data': data})
    
    return jsonify({'message': 'Data not received!'})

if __name__ == '__main__':
    app.run(debug=True)
