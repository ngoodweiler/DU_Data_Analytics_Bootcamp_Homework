## Step 2 - Climate App

# Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

# * Use FLASK to create your routes.

### Routes
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask setup
app = Flask(__name__)

# Routes
@app.route("/")
def welcome():
    return (
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/'START(YYYY-MM-DD)'<br/>"
        f"/api/v1.0/'START(YYYY-MM-DD)'/'END(YYYY-MM-DD)'"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    precipitation = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>"2016-08-23").all()
    session.close()
    all_prcp = []
    prcp_date = []
    prcp_prcp = []
    for date, prcp in precipitation:
        prcp_date.append(date)
        prcp_prcp.append(prcp)
    for i in range(len(prcp_date)):
        prcp_dict = {prcp_date[i]:prcp_prcp[i]}
        all_prcp.append(prcp_dict)
    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations = session.query(Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation).all()
    session.close()
    all_stations = []
    for station, name, lat, lng, elev in stations:
        station_dict = {}
        station_dict['Station ID'] = station
        station_dict['Station Name'] = name
        station_dict['Latitude'] = lat
        station_dict['Longitude'] = lng
        station_dict['Elevation'] = elev
        all_stations.append(station_dict)
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    tobs = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date>"2016-08-23").filter(Measurement.station == "USC00519281").all()
    session.close()
    all_tobs = []
    for date, temp in tobs:
        tobs_dict = {}
        tobs_dict['Date'] = date
        tobs_dict['Temperature'] = temp
        all_tobs.append(tobs_dict)
    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def start_only(start):
    end_date = '2017-08-24'
    session = Session(engine)
    temperatures = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end_date).all()
    session.close()
    temperature_stats = ['Minimum Temp','Average Temp','Maximum Temp']
    temps = []
    for minimum, average, maximum in temperatures:
        temps.append(minimum)
        temps.append(average)
        temps.append(maximum)
    temp_dict = dict(zip(temperature_stats,temps))
    return jsonify(temp_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    session = Session(engine)
    temperatures = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
    temperature_stats = ['Minimum Temp','Average Temp','Maximum Temp']
    temps = []
    for minimum, average, maximum in temperatures:
        temps.append(minimum)
        temps.append(average)
        temps.append(maximum)
    temp_dict = dict(zip(temperature_stats,temps))
    return jsonify(temp_dict)


if __name__ == '__main__':
    app.run(debug=True)
