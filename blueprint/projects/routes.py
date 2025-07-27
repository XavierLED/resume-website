from flask import request, render_template, redirect, url_for, Blueprint

projects = Blueprint('projects', __name__)

@projects.route('/')
def runProjects():
    return render_template('projects/projects.html')

@projects.route('/resume-website')
def runWebsite():
    return render_template('projects/website.html')

@projects.route('/fitness-tracker')
def runFitnessTracker():
    return render_template('projects/fitnessTracker.html')

@projects.route('/connect4')
def runConnect():
    return render_template('projects/connect4.html')

@projects.route('/todo-go')
def runTodo():
    return render_template('projects/goTodo.html')

@projects.route('/tik-tak-toe')
def runTikTakToe():
    return render_template('projects/tikTakToe.html')

@projects.route('/tumor-detection')
def runTumor():
    return render_template('projects/tumorDetection.html')

@projects.route('/weather-app')
def runWeather():
    return render_template('projects/weatherapp.html')

@projects.route('/wiki-scraper')
def runWikiScraper():
    return render_template('projects/wikiScraper.html')



