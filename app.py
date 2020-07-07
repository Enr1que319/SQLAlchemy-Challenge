from flask import Flask, jsonify, json, request
from datetime import datetime as dt
import pymongo
import os


# Files to load localy
# precipitation_file = "Resources/Last_Year_Measurement.json"
# stations_file = "Resources/stations.json"
# temp_obs = "Resources/Higher_temb_obs.json"

# precipitation = json.load(open(precipitation_file))
# stations = json.load(open(stations_file))
# temp = json.load(open(temp_obs))

conn = os.environ.get("MONGODB_URI")

client = pymongo.MongoClient(conn)
db = client.videogames
collection = db.surfer_climate
surfer_climate_data = collection.find({}, {"_id": 0})

selected_data = []

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route('/')
def home():
    url = request.base_url
    print('Server received request for "Home" page...')
    return (
        f'<h1> Surfs Up! </h1><br>'
        f'Here are the API routes about the Climate and Station Analysis in Honolulu, Hawaii<br>'
        f'Last year precipitation API: <a href="{url}api/v1.0/precipitation" target="_blank">{url}api/v1.0/precipitation</a><br>'
        f'Stations API: <a href="{url}api/v1.0/stations" target="_blank">{url}api/v1.0/stations</a><br>'
        f'Temperature Observations (TOBS) for the previous year API: <a href="{url}api/v1.0/tobs" target="_blank">{url}api/v1.0/tobs</a><br><hr></hr>'
        f'<h2> Dynamic API </h2>'
        f'<h3>From selected date to the last date:</h3>'
        f'Minimum, Maximum and Average of Temperature API : {url}api/v1.0/yyyy-mm-dd<br>'
        f'Example : <a href="{url}api/v1.0/2017-01-01" target="_blank">{url}api/v1.0/2017-01-01</a>'
        f'<h3>From selected date to the selected date:</h3>'
        f'Minimum, Maximum and Average of Temperature API : {url}/api/v1.0/start date/end date<br>'
        f'Example : <a href="{url}api/v1.0/2016-10-01/2017-05-01" target="_blank">{url}api/v1.0/2016-10-01/2017-05-01</a><br>'
        '<br>Note: format(yyyy-mm-dd)<br>'
        'API only contains data from 2016-09-01 to 2017-08-23'
    )


@app.route('/api/v1.0/precipitation')
def precip():
    return jsonify(surfer_climate_data[1])


@app.route('/api/v1.0/stations')
def stat():
    return jsonify(surfer_climate_data[2])


@app.route('/api/v1.0/tobs')
def tem_obs():
    return jsonify(surfer_climate_data[0])


@app.route('/api/v1.0/<start>')
def start_date(start):

    user_date = dt.strptime(start, '%Y-%m-%d')

    if dt.strptime(start, '%Y-%m-%d') < dt.strptime('2016-09-01', '%Y-%m-%d') or dt.strptime(start, '%Y-%m-%d') > dt.strptime('2017-08-23', '%Y-%m-%d'):
        return jsonify({'error': f'Date "{start}" not found. '}), 404
    else:
        precipitation = surfer_climate_data[1]['data']

        for row in precipitation:
            search_date = row['date']

            row_date = dt.strptime(search_date, '%Y-%m-%d')

            if row_date >= user_date:
                num = row['prcp']
                if num is None:
                    continue
                else:
                    selected_data.append(num)

    statics = [{'Max Temperature': max(selected_data), 'Min Temperature': min(selected_data),
                'Avg Temperature': round(sum(selected_data)/len(selected_data), 2)}]

    return jsonify(max(statics))


@app.route('/api/v1.0/<start>/<end>')
def start_end_date(start, end):

    user_date_start = dt.strptime(start, '%Y-%m-%d')
    user_date_end = dt.strptime(end, '%Y-%m-%d')

    if dt.strptime(start, '%Y-%m-%d') < dt.strptime('2016-09-01', '%Y-%m-%d') or dt.strptime(start, '%Y-%m-%d') > dt.strptime('2017-08-23', '%Y-%m-%d'):
        return jsonify({'error': f'Date "{start}" not found. '}), 404
    else:
        precipitation = surfer_climate_data[1]['data']

        for row in precipitation:
            search_date = row['date']

            row_date = dt.strptime(search_date, '%Y-%m-%d')

            if row_date >= user_date_start and row_date <= user_date_end:
                num = row['prcp']
                if num is None:
                    continue
                else:
                    selected_data.append(num)
            else:
                continue

    statics = [{'Max Temperature': max(selected_data), 'Min Temperature': min(selected_data),
                'Avg Temperature': round(sum(selected_data)/len(selected_data), 2)}]

    return jsonify(max(statics))


if __name__ == "__main__":
    # @TODO: Create your app.run statement here
    app.run(debug=True)
