from flask import render_template, Blueprint, send_from_directory

resume = Blueprint('resume', __name__)

@resume.route('/')
def runResume():
    return send_from_directory('static/pdf', "Xaviers Resume.pdf")
