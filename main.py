from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__==("__main__"):
    app.run("0.0.0.0",443,True)