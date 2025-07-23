from flask import request, render_template, redirect, url_for, Blueprint

home = Blueprint('home', __name__)

@home.route('/')
def runProjects():
    return render_template('home/home.html')
