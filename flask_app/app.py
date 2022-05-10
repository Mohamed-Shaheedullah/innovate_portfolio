# need to run venv
#

from flask import Flask, render_template # flask imports
from views import my_view # local imports

app = Flask(__name__)
app.register_blueprint(my_view)


# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True, port=8000) 

    