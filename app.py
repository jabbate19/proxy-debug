from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_headers():
    headers = request.headers
    return str(headers)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')

