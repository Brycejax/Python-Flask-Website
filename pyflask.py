#------------------------------------------------------------------
# Developer ----- Bryce Martin 
# Description --- This program will get me familiar with using
#                 python and flask for web applications. I will
#                 utilize this program for a personal portfolio
#------------------------------------------------------------------

#importing flask object from flask library
from flask import Flask

# creating an instance '__name__" = "__main__"
app = Flask(__name__)

#this / means the homepage: this line is the url
@app.route('/')

#this function will map its contents to the @app.route
def home():
    return "Website content goes here"

@app.route('/about/')

def about():
    return "About Page goes here!"

if __name__=="__main__":
    app.run(debug=True)