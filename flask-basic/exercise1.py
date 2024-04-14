from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>Welcome! Go to /puppy_latin/<your_name> to see your name in puppy latin!"

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1] != "y":
        return f"<h2>Your puppy latin name is {name}y</h2>"
    else:
        return f"<h2>Hello {name}! Your puppy latin name is {name[:-1]}iful</h2>"
    
if __name__ == "__main__":
    app.run()