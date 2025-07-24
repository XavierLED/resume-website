from flask import Flask

def createApp():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    
    from blueprint.resume.route import resume
    from blueprint.projects.routes import projects
    from blueprint.home.route import home
    
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(projects, url_prefix='/projects')
    app.register_blueprint(resume, url_prefix='/resume')
    return app

