from flask import Flask

def createApp():
    app = Flask('__name__', template_folder='templates')

    return app

