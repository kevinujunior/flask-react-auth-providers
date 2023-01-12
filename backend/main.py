from flask import Flask, render_template, url_for
from markupsafe import escape
app = Flask(__name__)


#name is a parameter passed in url and same is used in a function
@app.route("/")
def index(name=None):
    return "Hello World"

@app.route("/signup")
def signup():
    return "Sign up"

@app.route("/login")
def login():
    return "Login"
    
@app.route("/authenticated_view")
def view():
    return "authenticated view"
if __name__ == '__main__':
  app.run(debug=True)
  
