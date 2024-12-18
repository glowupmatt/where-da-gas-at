from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user():
    demo = User(
        id=1,  user="Demo", email="demo@aa.io", password="password"
    )
    marnie = User(
        id=2,  user="marnie", email="marnie@aa.io", password="password"
    )
    bobbie = User(
        id=3,    user="bobbie", email="bobbie@aa.io", password="password"
    )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the user table.
# SQLAlchemy doesn't have a built in function to do this. With
# postgres in production TRUNCATE removes all the data from the table,
# and RESET IDENTITY resets the auto incrementing primary key, CASCADE
# deletes any dependent entities. With sqlite3 in development you need
# to instead use DELETE to remove all data and it will reset the
# primary keys for you as well.
def undo_user():
    if environment == "production":
        db.session.execute(
            f'TRUNCATE table "{SCHEMA}.user" RESTART IDENTITY CASCADE;'
        )
    else:
        db.session.execute(text('DELETE FROM "user"'))

    db.session.commit()
