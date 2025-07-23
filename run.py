from blueprint.app import createApp

myWebsite = createApp()

if __name__ == '__main__':
    myWebsite.run(host='0.0.0.0', debug=True)
