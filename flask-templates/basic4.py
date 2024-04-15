from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index4.html')

@app.route('/signup')
def signup():
    return render_template('signup4.html')

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou4.html',
                           first=first,
                           last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_4.html'), 404

if __name__ == "__main__":
    app.run(debug=True)