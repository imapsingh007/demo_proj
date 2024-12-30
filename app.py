from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, GitHub Actions!</h1><p>Welcome to the static deployment.</p>"

if __name__ == "__main__":
    app.run(debug=True)
