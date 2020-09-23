from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route ("/", methods=["GET", "POST"])
def home ():
    #result = ""
    if "result" in request.args: 
        result = request.args["result"]
    if request.method == "POST":
        entered_number = request.form ["number"]
        result = int_to_rome(entered_number)
        if result == "Not Valid Input !!":
            return redirect (url_for ("home", result = "Not Valid! Please enter a number between 1 and 3999, inclusively."))
        else:
        	return redirect (url_for("result", number_decimal=entered_number, number_roman = result))
    else:
        return render_template ("index.html", result = result)
    
def int_to_rome(a):
    import sys

    a = int(a)
    if not 0 < a <4000:
        return "Not Valid Input !!"
    b = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    c = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    d= []
    for i in range(len(b)):
        count = int((a/b[i]))
        d.append(count*c[i])
        a -= count * b[i]
    return "".join(d)
    
	

@app.route("/result", methods = ["GET"])
def result():
    if "number_decimal" in request.args and "number_roman" in request.args: 
        number_decimal = request.args["number_decimal"]
        number_roman = request.args["number_roman"]
        print(request)
        print()
        print(request.args)
        return render_template("result.html", number_decimal = number_decimal, number_roman = number_roman)
    else:
        return render_template("result.html")
    

if __name__ == '__main__':
    app.run(debug=True)
#    app.run(host='0.0.0.0', port=80)