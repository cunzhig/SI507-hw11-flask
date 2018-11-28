from secrets import *
from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

# default
@app.route('/')
def welcome():
    return '<h1>Welcome!</h1>'

# nyt
def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json'
    params={'api-key': nyt_key}
    return requests.get(extendedurl, params).json()

def get_headlines(nyt_results_dict):
    results = nyt_results_dict['results']
    headlines = []
    for r in results:
        content = r['title']+'('+r['url']+')'
        headlines.append(content)
    return headlines

# user/<name> 
@app.route('/user/<nm>')
def top_headlines(nm):
    story_list_json = get_stories('technology')
    headlines = get_headlines(story_list_json)
    html = render_template('user.html',name=nm,section='technology',my_list=headlines)
    html += "<a href = '/user/"+nm+"/home'> Go to home </a>"
    return html


@app.route('/user/<nm>/home')
def ec1(nm):
    story_list_json = get_stories('home')
    headlines = get_headlines(story_list_json)
    html = render_template('user.html',name=nm,section='home',my_list=headlines)
    html += "<a href = /user/"+nm+"> Go Back </a>"
    return html


if __name__ == '__main__':
    app.run(debug=True)