from flask import Flask, request, jsonify

app = Flask(__name__)

html = "<html><head><title>%s</title></head><body>%s</body></html>"

@app.route('/')
def home():
    return html%("Hello", "Hello, World!")

@app.route('/hello/<name>')
def hello_name(name):
    return html%("Hello", f"Hello, {name}!")

@app.route('/json', methods=['POST'])
def get_json():
    data = request.get_json()
    return html%("json", jsonify(data))

if __name__ == '__main__':
    app.run(debug=True)
