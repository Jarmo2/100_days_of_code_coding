from bs4 import BeautifulSoup
import requests
from datetime import datetime
from flask import Flask, render_template


## request module and bs4 are used to scrape the current destination of bader III from vesselfinder.com
headers = {
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
}

response_ship = requests.get("https://www.vesselfinder.com/de/vessels/BADER-III-IMO-7504598-MMSI-308603000", headers=headers)

data = response_ship.text
soup = BeautifulSoup(data, "html.parser")

most_recent_dest = soup.find(class_="vi__r1 vi__sbt")

# string methods are used to split the result the location and the ETA
location_text = most_recent_dest.text.split('ETA:')[0].strip()
location_eta = most_recent_dest.text.split('ETA:')[1].strip().split(",")[0].split(" ")
# the following step removes the country location from the name of the port of arrival.
adjusted = " ".join(location_text.split(" ", 2)[:2])
# then the empty spaces are filled with hyphens
adjusted = adjusted.replace(" ", "-")

# here the month of the date of arrival is converted from an abbreviated name into a number
month = datetime.strptime(location_eta[0], '%b').month

## here an API is used to get to know what happend on the ETA in another year
response = requests.get(f"https://byabbe.se/on-this-day/{month}/{location_eta[1]}/events.json")
answer = response.json()

year = answer['events'][0]['year']
description = answer['events'][0]['description']
link = answer['events'][0]['wikipedia'][0]['wikipedia']

## here a flask app is used to make the website dynamic and give the current location to the weather widget and the history to the wikipedia widget.

app = Flask(__name__)
app.config['SECRET_KEY'] = "Ichfahrenach-Lummerland"

@app.route('/', methods=['GET', 'POST'])
def show_home():
    return render_template('index.html', location=adjusted, description=description, link=link, year=year, arrival_month=location_eta[0],
                           arrival_day=location_eta[1])

if __name__ == '__main__':
    app.run(debug=True)



