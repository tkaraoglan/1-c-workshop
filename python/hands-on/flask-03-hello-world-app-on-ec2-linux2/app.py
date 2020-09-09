from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    first = "This is my first condition experience in Flask"
    return render_template("index.html", mesaji = first)

@app.route("/for")
def for_example():
    names = ['Tolga', 'Asuman', 'Vildan', 'Yahya', 'Taha']
    return render_template("deneme.html", isimler = names)






if __name__ == "__main__":
    app.run(debug=True)



