from flask import Flask,render_template
from flask_restful import Api

app = Flask(__name__)
api=Api(app)

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)