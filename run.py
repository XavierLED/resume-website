from blueprint.app import create_app

myWebsite = create_app()

if __name__ == '__main__':
    myWebsite.run(host='0.0.0.0', debug=True)
