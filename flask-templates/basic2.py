from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    puppies = ['Fluffy', "Rufus", "Spykie"]
    return render_template('basic2.html',
                           puppies=puppies)

if __name__ == "__main__":
    app.run(debug=True)