from flask import Flask, render_template, url_for
from bs4 import BeautifulSoup as soup
import requests


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
    city = 'Brampton'

    info = requests.get(url.format(city)).json()

    holder = {
        'city': city,
        'temperature': info['main']['temp'],
        'description': info['weather'][0]['description'],
        'icon': info['weather'][0]['icon'],
    }
    print(holder)

    return render_template('weather.html')


if __name__ == "__main__":
    app.run(debug=True)