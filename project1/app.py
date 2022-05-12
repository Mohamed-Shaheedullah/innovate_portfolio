# instructions for running in Linux
# cd /home/raf/Documents/Git_Repos/innovate/project1
# source proj_venv/bin/activate
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run

from flask import Flask, render_template # flask imports
from views import my_view # local imports

# run flask, enable views
app = Flask(__name__)
app.register_blueprint(my_view)

# for routes  that are not defined, route to error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", e=e)

# run program
if __name__=="__main__":
    app.run(debug=True, port=8000) 