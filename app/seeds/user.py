from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

user_seeds = [
    {
        "user": "Demo",
        "email": "demo@example.com",
        "password": "password",
    },
    {
        "user": "marnie",
        "email": "marnie@example.com",
        "password": "password",
    },
    {
        "user": "bobbie",
        "email": "bobbie@example.com",
        "password": "password",
    },
]


# Adds a demo user, you can add other users here if you want
def seed_user():
    # use the "users" array to insert records into the db
    for user_seed in user_seeds:
        user = User(
            user=user_seed["user"],
            email=user_seed["email"],
            password=user_seed["password"],
        )
        db.session.add(user)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the user table.
# SQLAlchemy doesn't have a built in function to do this. With
# postgres in production TRUNCATE removes all the data from the table,
# and RESET IDENTITY resets the auto incrementing primary key, CASCADE
# deletes any dependent entities. With sqlite3 in development you need
# to instead use DELETE to remove all data and it will reset the
# primary keys for you as well
def undo_user():
    if environment == "production":
        db.session.execute(
            f'TRUNCATE table "{SCHEMA}.user" RESTART IDENTITY CASCADE;'
        )
    else:
        db.session.execute(text('DELETE FROM "user"'))

    db.session.commit()
