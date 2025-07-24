from flask import render_template, Blueprint

contact = Blueprint('contact', __name__)

@contact.route('/')
def runContact():
    return render_template('contact/contact.html')
