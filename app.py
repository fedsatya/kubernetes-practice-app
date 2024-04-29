from flask import Flask
app = Flask(__name__)

@app.route('/')
def first():
    return "First Application"

if __name__ == '__main__':
    app.run(debug=True)
