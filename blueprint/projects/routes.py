from flask import request, render_template, redirect, url_for, Blueprint

projects = Blueprint('projects', __name__, template_folder='templates')

@projects.route('/')
def runProjects():
    return render_template('projects.html')
