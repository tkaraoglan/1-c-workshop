from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/',methods = ["GET", "POST"])
def home():
    return render_template('index.html')

    

@app.route('/result' )
def result():
    return render_template('result.html')


@app.route('/result')
def result1():
    if request.method == 'POST':
        numbertyeni = request.form['number']
        return 
# @app.route('/greet', methods=['POST'])
# def greet():
#     if 'user' in request.args:
#         usr = request.args['user']
#         return render_template('greet.html', user=usr)
#     else:
#         return render_template('greet.html', user='Send your user name with "user" param in query string')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         user_name = request.form['username']
#         return render_template('secure.html', user=user_name)
#     else:
#         return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
#    app.run(host='0.0.0.0', port=80)