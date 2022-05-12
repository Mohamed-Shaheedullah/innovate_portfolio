from flask import Blueprint, render_template, redirect, request, url_for
# import necessary modules

#a blueprint defines a collection of views, templates and static assets
my_view = Blueprint('my_view', __name__)

# define all necessary page routes according to present html files
@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/index")
def index2():
    return render_template("index.html")

@my_view.route("/page1")
def page1():
    return render_template("page1.html")

@my_view.route("/page2")
def page2():
    return render_template("page2.html")

@my_view.route("/page3")
def page3():
    return render_template("page3.html")

@my_view.route("/page4")
def page4():
    return render_template("page4.html")

@my_view.route("/Admin")
def Admin():
    return render_template("Admin.html")

# redirect some routes to index.html

@my_view.route("/home")
def home_redirect():
    return redirect(url_for("my_view.index"))

@my_view.route("/javascript")
def homeb_redirect():
    return redirect(url_for("my_view.index"))

@my_view.route("/js")
def homeb2_redirect():
    return redirect(url_for("my_view.index"))