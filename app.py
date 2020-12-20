from flask import Flask


app = Flask(__name__)


data = []


@app.route('/')
def index():
    return 'API de Eventos'


if __name__ == '__main__':
    app.run(debug=True)
