from flask import Flask, redirect, url_for, render_template

app=Flask(__name__)

@app.route("/")
def Home():
    return render_template(r"index.html")

#main_driver_function
if __name__== "__main__":
    app.run(debug=False,port=8080)