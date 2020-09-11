from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return 'This is home page for no path, <h1> Welcome Home</h1>'

@app.route('/about')
def about():
    return '<h1>This is my about page </h1>'

@app.route('/error')
def error():
    return '<h1>Either you encountered an error or you are not authorized.</h1>' 

@app.route('/hello')
def hello():
    return '<h1>Hello, World! </h1>'

@app.route('/admin')
def admin():
    return redirect(url_for('error'))

# @app.route('/<name>')
# def greet(name):
#    return f'hello, { name }'

# @app.route('/<name>')
# def greet(name):
#     greet_format=f"""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Greeting Page</title>
# </head>
# <body>
#     <h1> Hello { name }!</h1>
#     <h1> Welcome to My greeting page!</h1>

# </body>
# </html>
# """
#     return greet_format

@app.route('/<name>')
def greet(name):
    number1 = 23
    number2 = 34
    return render_template('greet.html', isim = name, number1 = 23, number2 = 34, toplam = number1 + number2)

@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for('greet', name = 'Master Admin!!!'))

@app.route('/list100')
def list100():
    return render_template('list100.html')

@app.route('/evens')
def evens():
    return render_template('evens.html')    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
   #app.run(debug=True)


# Create a function named greet_admin which redirect the request to the hello path with param of 'Master Admin!!!!' 
# and assign to the route of ('/greet-admin')

# Rewrite a function named greet which which uses template file named `greet.html` under `templates` folder 
# and assign to the dynamic route of ('/<name>')

# Create a function named list10 which creates a list counting from 1 to 10 within `list10.html` 
# and assign to the route of ('/list10')

# Create a function named evens which show the even numbers from 1 to 10 within `evens.html` 
# and assign to the route of ('/evens')

# Add a statement to run the Flask application which can be reached from any host on port 80.
# ```

# - Write a template html file named `greet.html` which takes `name` as parameter under `templates` folder 

# - Write a template html file named `list10.html` which shows a list counting from 1 to 10 under `templates` folder 

# - Write a template html file named `evens.html` which shows a list of even numbers from 1 to 10 under `templates` folder 

# - Create a folder named `static` under `hands-on/flask-02-handling-routes-and-templates-on-ec2-linux2` folder and create a text file named `mytext.txt` with *This is a text file in static folder* content.

# - Add and commit all changes on local repo

# - Push `app.py`, `greet.html`, `list10.html`, `evens.html`, and `mytext.txt` to remote repo `clarusway-python-workshop` on GitHub.

# Part 4 - Run the Hello World App on EC2 Instance

# - Download the web application file from GitHub repo.

# - Run the web application

# - Connect the route handling and templating web application from the web browser and try every routes configured

# - Open the static file `mytext.txt` context from the web browser

# - Connect the route handling and templating web application from the terminal with `curl` command.