from flask import Flask

def createApp():
    app = Flask(__name__, template_folder='templates')

    from blueprint.projects.routes import projects
    from blueprint.home.route import home
    
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(projects, url_prefix='/projects')
    return app

