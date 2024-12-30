from sqlalchemy.sql import text

from app.models import db, Review, undo_table
from app.models.station import Station
from app.models.user import User
from app.seeds.user import user_seeds
from app.seeds.station import station_seeds


user_emails = [user_seed["email"] for user_seed in user_seeds]
station_uris = [station_seed["uri"] for station_seed in station_seeds]


review_seeds = [
    {
        "user_id": 1,
        "station_id": 1,
        "text": """
          Great place for premium gas,
          but the line can get long during rush hour.
        """,
    },
    {
        "user_id": 1,
        "station_id": 3,
        "text": """
          Love this place!
          The charging speed is awesome,
          and the restroom is always clean.
        """,
    },
    {
        "user_id": 2,
        "station_id": 2,
        "text": """
          Best fuel stop in town!
          The air pump works great and the staff is super friendly.
        """,
    },
    {
        "user_id": 2,
        "station_id": 1,
        "text": """
          Excellent experience!
          Staff is friendly, and the charging process is seamless.
        """,
    },
    {
        "user_id": 3,
        "station_id": 3,
        "text": """
          Charging works well, but the place is often crowded.
          Needs more space for parking.
        """,
    },
    {
        "user_id": 3,
        "station_id": 1,
        "text": """
          Excellent experience!
          Staff is friendly, and the charging process is seamless.
        """,
    },
]


def seed_review():
    users = User.query.filter(User.email.in_(user_emails)).all()
    stations = Station.query.filter(
        Station.uri.in_(station_uris)
    ).all()

    for review_seed in review_seeds:
        review = Review(
            text=review_seed["text"],
            user_id=users[review_seed["user_id"] - 1].id,
            station_id=stations[review_seed["station_id"] - 1].id,
        )
        db.session.add(review)

    db.session.commit()


def undo_review():
    undo_table("review")
