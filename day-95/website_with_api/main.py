import requests
from flask import Flask, render_template

#tram data
URL_NO_F = "https://cdt.hafas.de/opendata/apiserver/departureBoard?accessId=c2fb3438-45a4-48ff-9f5f-3546da29c6a9&lang=fr&id=200405057&format=json"
station_id_hamilius = "200405057"
URL = f"https://cdt.hafas.de/opendata/apiserver/departureBoard?accessId=c2fb3438-45a4-48ff-9f5f-3546da29c6a9&lang=fr&id={station_id_hamilius}&format=json"

def get_tram_data():
    response = requests.get(URL)
    response_as_json = response.json()
    next_tram_time = response_as_json['Departure'][0]["time"]
    next_tram_direction = response_as_json['Departure'][0]["direction"]
    return next_tram_time, next_tram_direction

#Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'




@app.route('/')
def show_page():
    next = False
    heading = "When is your next tram leaving Hamilius?"
    sub_heading = "The world is wide open. Will it take you to Luxexpo or to the Gare?"
    other = "click here to find the next one"
    return render_template("index.html", title=heading, subtitle=sub_heading, next=next, refresh=other)

@app.route('/next')
def show_next():
    next = True
    next_tram_t, next_tram_d = get_tram_data()
    print(next_tram_d)
    if next_tram_d == "Kirchberg, Luxexpo":
        heading = "This is your next tram."
        sub_heading = f"Your tram is going to {next_tram_d[:9]}. It's departing at {next_tram_t}."
        other = "Refresh?"
        luxexpo = True
        return render_template("index.html", title=heading, subtitle=sub_heading, next=next, refresh=other, luxexpo=luxexpo)

    if next_tram_d == "Luxembourg, Gare Centrale (Tram)":
        heading = "This is your next tram."
        sub_heading = f"Your tram is going to {next_tram_d[12:25]}. It's departing at {next_tram_t}."
        other = "Refresh?"
        gare = True
        return render_template("index.html", title=heading, subtitle=sub_heading, next=next, refresh=other, gare=gare)
    else:
        heading = "Error"
        sub_heading = f"No tram found."
        other = "Try again?"
        return render_template("index.html", title=heading, subtitle=sub_heading, next=next, refresh=other)



if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
