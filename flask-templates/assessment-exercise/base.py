from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    # Setup the boolean variables
    lower = False
    upper = False
    end_num = False

    # Get the username provided
    username = request.args.get('username')

    # Checks
    for letter in username:
        if letter.isupper():
            upper = True
        elif letter.islower():
            lower = True
    end_num = True if username[-1].isdigit() else False  

    report = lower and upper and end_num

    return render_template('report.html', 
                           report=report, 
                           upper=upper, 
                           lower=lower, 
                           end_num=end_num,
                           username=username)

if __name__ == "__main__":
    app.run(debug=True)