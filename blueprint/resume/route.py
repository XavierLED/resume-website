from flask import render_template, Blueprint

resume = Blueprint('resume', __name__)

@resume.route('/')
def runResume():
    return render_template('resume/resume.html')
