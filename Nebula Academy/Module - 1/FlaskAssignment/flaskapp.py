from flask import Flask, request, abort
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/status')
def hello():
    return {"status": "OK!"}

@app.route('/square/<int:number>')
def square(number):
    return {"result": number**2}

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return {"echo": data["message"]}

@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found"}, 404

@app.errorhandler(400)
def bad_request(error):
    return {"error": "Invalid POST data"}, 400

if __name__ == '__main__':
    app.run(debug=True)