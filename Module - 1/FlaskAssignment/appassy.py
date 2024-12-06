from flask import Flask, request

app = Flask(__name__)

@app.route('/status')
def status():
    return {"status": "API is running"}

@app.route('/reverse/<string:text>')
def reverse_text(text):
    return {"reversed": text[::-1]}

@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.json
    if not data or 'a' not in data or 'b' not in data:
        return {"error": "Invalid input, fields 'a' and 'b' are required"}, 400
    try:
        a = float(data['a'])
        b = float(data['b'])
        return {"sum": a + b}
    except ValueError:
        return {"error": "Fields 'a' and 'b' must be numbers"}, 400



if __name__ == '__main__':
    app.run(debug=True)
