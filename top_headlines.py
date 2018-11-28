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
    params={'api-key': api_key}
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
    html += "\n<a href = '/user/"+nm+"/home'>home </a>"
    html += "\n<a href = '/user/"+nm+"/opinion'>opinion </a>"
    html += "\n<a href = '/user/"+nm+"/world'>world </a>"
    html += "\n<a href = '/user/"+nm+"/national'>national </a>"
    html += "\n<a href = '/user/"+nm+"/politics'>politics </a>"
    html += "\n<a href = '/user/"+nm+"/nyregion'>nyregion </a>"
    html += "\n<a href = '/user/"+nm+"/business'>business </a>"
    html += "\n<a href = '/user/"+nm+"/technology'>technology </a>"
    html += "\n<a href = '/user/"+nm+"/science'>science </a>"
    html += "\n<a href = '/user/"+nm+"/health'>health </a>"
    html += "\n<a href = '/user/"+nm+"/sports'>sports </a>"
    html += "\n<a href = '/user/"+nm+"/arts'>arts </a>"
    html += "\n<a href = '/user/"+nm+"/books'>books </a>"
    
    html += "\n<a href = '/user/"+nm+"/movies'>movies </a>"
    html += "\n<a href = '/user/"+nm+"/theater'>theater </a>"
    html += "\n<a href = '/user/"+nm+"/sundayreview'>sundayreview </a>"
    html += "\n<a href = '/user/"+nm+"/fashion'>fashion </a>"
    html += "\n<a href = '/user/"+nm+"/tmagazine'>tmagazine </a>"
    html += "\n<a href = '/user/"+nm+"/food'>food </a>"
    html += "\n<a href = '/user/"+nm+"/travel'>travel </a>"
    html += "\n<a href = '/user/"+nm+"/magazine'>magazine </a>"
    html += "\n<a href = '/user/"+nm+"/realestate'>realestate </a>"
    html += "\n<a href = '/user/"+nm+"/automobiles'>automobiles</a>"
    html += "\n<a href = '/user/"+nm+"/obituaries'>obituaries </a>"
    html += "\n<a href = '/user/"+nm+"/insider'>insider</a>"
    return html

# user/<name>/home
@app.route('/user/<nm>/<sec>')
def ec1(nm,sec):
    story_list_json = get_stories(sec)
    headlines = get_headlines(story_list_json)
    html = render_template('user.html',name=nm,section=sec,my_list=headlines)
    html += "<a href = /user/"+nm+"> Go Back </a>"
    return html




if __name__ == '__main__':
    app.run(debug=True)