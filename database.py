from app import app, db
from app.models.user import User
from app.models.station import Station
from app.models.review import Review

with app.app_context():
    db.drop_all()
    db.create_all()


    user1=User(id=1, user='user1', email='user1@gmail.com', password='password')
    user2=User(id=2, user='user2', email='user2@gmail.com', password='password')
    user3=User(id=3, user='user3', email='user3@gmail.com', password='password')
    user4=User(id=4, user='user4', email='user4@gmail.com', password='password')
    user5=User(id=5, user='user5', email='user5@gmail.com', password='password')
    user6=User(id=6, user='user6', email='user6@gmail.com', password='password')
    user7=User(id=7, user='user7', email='user7@gmail.com', password='password')
    user8=User(id=8, user='user8', email='user8@gmail.com', password='password')

    station1=Station(
        id=1, name="station1",lat=123456675,
        lng=123456785,address='1 number lane',
        uri='http://numberlane', location_id='1', user_id=1
    )
    station2=Station(
        id=2, name="station2",lat=123567897,
        lng=98776765,address='2 number lane',
        uri='http://numberlane', location_id='2', user_id=3
    )
    station3=Station(
        id=3, name="station3",lat=1239847566,
        lng=123758544,address='3 number lane',
        uri='http://numberlane', location_id='3', user_id=7
    )
    station4=Station(
        id=4, name="station4",lat=94837283,
        lng=72689904,address='4 number lane',
        uri='http://numberlane', location_id='4', user_id=8
    )
    station5=Station(
        id=5, name="station5",lat=982374847,
        lng=34598929,address='5 number lane',
        uri='http://numberlane', location_id='5', user_id=6
    )


    review1=Review(id=1, user_id=1, station_id=2, review='This place sucks')
    review2=Review(id=2, user_id=1, station_id=4, review='This place is awsome')
    review3=Review(id=3, user_id=1, station_id=3, review='i really like this place')
    review4=Review(id=4, user_id=2, station_id=5, review='Gas is cheap here')
    review5=Review(id=5, user_id=2, station_id=1, review='Bathroom smells like shit')
    review6=Review(id=6, user_id=3, station_id=2, review='expensive gas cheap food')
    review7=Review(id=7, user_id=3, station_id=4, review='cheap food expensive gas')
    review8=Review(id=8, user_id=3, station_id=5, review='very helpfull cashier')
    review9=Review(id=9, user_id=3, station_id=3, review='too far')
    review10=Review(id=10, user_id=4, station_id=1, review='hot chicks work here')
    review11=Review(id=11, user_id=5, station_id=2, review='no mcdonalds here')
    review12=Review(id=12, user_id=6, station_id=4, review='theres a masjid nearby')
    review13=Review(id=13, user_id=7, station_id=5, review='looks like a clurb')
    review14=Review(id=14, user_id=8, station_id=5, review='they spilled gas  on me')

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.add(user7)
    db.session.add(user8)

    db.session.add(station2)
    db.session.add(station3)
    db.session.add(station4)
    db.session.add(station5)

    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.add(review7)
    db.session.add(review8)
    db.session.add(review9)
    db.session.add(review10)
    db.session.add(review11)
    db.session.add(review12)
    db.session.add(review13)


    db.session.commit()

#review1=Review(id=1, user_id=[1], station_id=[2], review='This place sucks')
#review2=Review(id=2, user_id=[1], station_id=[4], review='This place is awsome')
#review3=Review(id=3, user_id=[1], station_id=[3], review='i really like this place')
#review1=Review(id=1, user_id=[2], station_id=[5], review='Gas is cheap here')
#review2=Review(id=2, user_id=[2], station_id=[1], review='Bathroom smells like shit')
#review1=Review(id=1, user_id=[3], station_id=[2], review='expensive gas cheap food')
#review2=Review(id=2, user_id=[3], station_id=[4], review='cheap food expensive gas')
#review3=Review(id=3, user_id=[3], station_id=[5], review='very helpfull cashier')
#review4=Review(id=4, user_id=[3], station_id=[3], review='too far')
#review1=Review(id=1, user_id=[4], station_id=[1], review='hot chicks work here')
#review1=Review(id=1, user_id=[5], station_id=[2], review='no mcdonalds here')
#review1=Review(id=1, user_id=[6], station_id=[3], review='theres a masjid nearby')
#review1=Review(id=1, user_id=[7], station_id=[4], review='looks like a clurb')
#review1=Review(id=1, user_id=[8], station_id=[5], review='they spilled gas  on me')
