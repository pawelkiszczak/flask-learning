from flask import Flask
app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return "<h1> Hello Puppy!</h1>"

@app.route('/information') #127.0.0.1:5000/information
def info():
    return "<h1> Puppies are cute!"

# Dynamic routing
@app.route('/puppy/<name>')
def puppy(name):
    return f"<h1> This is a page for {name}</h1>"

# Debug mode example
@app.route('/kitties/<name>')
def kitty(name):
    return f"100th letter: {name[100]}"

if __name__ == "__main__":
    app.run(debug=True)