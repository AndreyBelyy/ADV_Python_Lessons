from flask import Flask, render_template
# import requests
import json

application = Flask(__name__)


@application.route("/")
def index():
    return "/Users/aegar/Documents/kube/index.html"


@application.route("/help")
def help():
    return "<b><font color=blue>Wikipedia?</font></b>"


@application.route("/user")
def usermain_page():
    return "User's Main Page"


@application.route("/user/<username>")
def show_user_page(username):
    return "Hello " + username.upper()


@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return "SubPath is: " + subpath


@application.route("/kvadrat/<int:x>")
def calc_kvadrat(x):
    return "Kvadrat ot " + str(x) + " = " + str(x * x)


@application.route("/htmlpage")
def show_html_page():
    myfile = open("index.html", mode='r')
    page = myfile.read()
    myfile.close()
    return page


@application.route("/html/1")
def show_html_page1():
    return render_template('/Users/aegar/PycharmProjects/ADV_Python_Lessons/Flask/templates/index.html', name=1)


# _____Main______#
if __name__ == "__main__":
    application.debug = True
    application.env = "Worker-new"
    application.run()
