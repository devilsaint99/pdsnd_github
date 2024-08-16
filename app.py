from flask import Flask, render_template, request, session, url_for, redirect
import bikeshare1 as b1
app = Flask(__name__)
app.secret_key = 'devilsaint'

@app.route("/", methods=['POST', 'GET'])
def main():
    
    return render_template('index.html',cities=b1.city, months=b1.months.values(), weekdays=b1.weekdays.values())


@app.route("/trips_insights",methods=['POST', 'GET'])
def trips_insights():
    if request.method == "POST":
        session["city"] = request.form["city"]
        month_value = next((key for key, value in b1.months.items() if value == request.form["month"]), None)
        session["month"] = month_value
        session["day"] = request.form["weekday"]
    df= b1.load_data(session["city"],session["month"], session["day"])
    time_stats = b1.time_stats(df)
    station_stats = b1.station_stats(df)
    return render_template('trips_stations.html', time_stats = time_stats, station_stats = station_stats)

@app.route("/user_insights", methods=['POST', 'GET'])
def user_insights():
    if request.method == "POST":
        session["city"] = request.form["city"]
        month_value = next((key for key, value in b1.months.items() if value == request.form["month"]), None)
        session["month"] = month_value
        session["day"] = request.form["weekday"]
    df = b1.load_data(session["city"],session["month"], session["day"])
    user_stats = b1.user_stats(df)
    subscriber_count = user_stats[0]['Subscriber']
    customer_count = user_stats[0]['Customer']
    male_count = user_stats[1]['Male']
    female_count = user_stats[1]['Female']
    earliest_yr = user_stats[2]
    recent_yr = user_stats[3]
    common_yr = user_stats[4]
    we_user_stats = [subscriber_count, customer_count, male_count, female_count, earliest_yr, recent_yr, common_yr]


    return render_template('user.html', user_stats = we_user_stats)
