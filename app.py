from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Voice Clone Call App Running"

if __name__ == "__main__":
    app.run(debug=True)
