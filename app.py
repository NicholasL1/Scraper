from flask import Flask, render_template, url_for
from bs4 import BeautifulSoup as soup
import requests
from datetime import datetime


# with open("templates/index.html", "r") as f:
#     doc = soup(f, "html.parser")
#     word = doc.find("div", class_="tile-container")

# print (word.string)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/weather')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=308c52fb7d9fcbf8bb5484efe08e579e'
    city = 'Toronto'

    info = requests.get(url.format(city)).json()

    sunrisetime = datetime.utcfromtimestamp(int(info['sys']['sunrise'])).strftime('%Y-%m-%d %H:%M') #Getting UTC timestamp and converting to date and time
    today = sunrisetime.split() #Splitting date and time into an array with two elements

    #Repeating process with sunset
    sunsettime = datetime.utcfromtimestamp(int(info['sys']['sunset'])).strftime('%Y-%m-%d %H:%M')
    night = sunsettime.split()

    holder = {
        'city': info['name'],
        'temperature': round(info['main']['temp']),
        'description': info['weather'][0]['description'].title(),
        'icon': info['weather'][0]['icon'],
        'country': info['sys']['country'],
        'feels': round(info['main']['feels_like']),
        'date': today[0],
        'sunrise': today[1],
        'sunset': night[1],
        'humidity': info['main']['humidity'],
        'pressure': info['main']['pressure'],
        'tempmin': info['main']['temp_min'],
        'tempmax': info['main']['temp_max'],
        'wind': round(info['wind']['speed']*3.6),
        'visibility': info['visibility']/10000,
    }

    return render_template('weather.html', holder=holder)

if __name__ == "__main__":
    app.run(debug=True)