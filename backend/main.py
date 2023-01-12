from flask import Flask, render_template, url_for
from markupsafe import escape
app = Flask(__name__)


#name is a parameter passed in url and same is used in a function
@app.route("/")
def index(name=None):
    return "Hello World"

 
if __name__ == '__main__':
  app.run(debug=True)
  
