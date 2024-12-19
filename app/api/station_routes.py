from  flask import Blueprint, jsonify, request
from app.models import station, db
from app.models import Station
from flask_login import login_required, current_user
from app.forms import StationForm, EditStationForm

station_routes = Blueprint("station", __name__)

@station_routes.route("/", methods=["GET"])
@login_required
def stations():
    if current_user.is_authenticated:
        stations = Station.query.all()
        data = {"stations": {station.id: station.to_dict() for station in stations if station.user_id == current_user.id}}
        return jsonify(data)


@station_routes.route("/", methods=["POST"])
@login_required
def create_station():
    form = StationForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        station = Station(
            name=form.data["name"],
            lat=form.data["lat"],
            lng=form.data["lng"],
            address=form.data["address"],
            uri=form.data["uri"],
            location_id=form.data["location_id"],
            user_id=current_user.id,
        )
        print(station)
        db.session.add(station)
        db.session.commit()
        return station.to_dict()
    return form.errors, 401


@station_routes.route("/<int:id>", methods=["PUT"])
@login_required
def edit_station():
    form = EditStationForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        station = Station(
            name=form.data["name"],
            lat=form.data["lat"],
            lng=form.data["lng"],
            address=form.data["address"],
            uri=form.data["uri"],
            location_id=form.data["location_id"],
            user_id=current_user.id,
        )
        db.session.add(station)
        db.session.commit()
        return station.to_dict()
    return form.errors, 401


@station_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_station(id):
    if current_user.id:
        station = Station.query.get(id)
        if station and station.user_id == current_user.id:
            db.session.delete(station)
            db.session.commit()
            return {"message": "Station deleted successfully"}
    return {"error": "Station not found or unauthorized"}, 401