from flask import Flask

def createApp():
    app = Flask(__name__, template_folder='templates')
    
    from blueprint.resume.route import resume
    from blueprint.projects.routes import projects
    from blueprint.home.route import home
    from blueprint.contact.route import contact
    
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(projects, url_prefix='/projects')
    app.register_blueprint(contact, url_prefix='/contact')
    app.register_blueprint(resume, url_prefix='/resume')
    return app

