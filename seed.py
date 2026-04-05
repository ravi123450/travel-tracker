from datetime import datetime, timedelta

from app import app, db
from models import Trip, User   # 👈 import User model

with app.app_context():

    # Clear old trips
    db.session.query(Trip).delete()

    routes = [
        [
            {"lat": 12.9716, "lng": 77.5946},
            {"lat": 12.9720, "lng": 77.5950},
            {"lat": 12.9730, "lng": 77.5960}
        ],
        [
            {"lat": 12.9600, "lng": 77.5800},
            {"lat": 12.9610, "lng": 77.5810},
            {"lat": 12.9620, "lng": 77.5820}
        ],
        [
            {"lat": 12.9900, "lng": 77.6100},
            {"lat": 12.9910, "lng": 77.6110},
            {"lat": 12.9920, "lng": 77.6120}
        ]
    ]

    modes = [
        "Walk", "Bike", "Car",
        "Bus", "Auto", "Cycle",
        "Train", "Car", "Walk"
    ]

    purposes = [
        "Work", "Study", "Shopping",
        "Leisure", "Travel", "Gym",
        "Hospital", "Office", "Personal"
    ]

    now = datetime.utcnow()

    # 👇 Fetch all users
    users = User.query.all()

    trip_counter = 1

    for user in users:   # 🔥 loop through each user

        for i in range(9):   # 9 trips per user

            route = routes[i % 3]

            start_time = now - timedelta(days=i+1, hours=i+2)
            trip_date = start_time.date()

            duration_min = 10 + i * 3
            end_time = start_time + timedelta(minutes=duration_min)

            t = Trip(
                user_id=user.id,   # 👈 dynamic user id
                trip_no=f"TEST-{user.id:02d}-{i+1:02d}",  # unique trip no

                purpose=purposes[i],

                start_lat=route[0]["lat"],
                start_lng=route[0]["lng"],
                end_lat=route[-1]["lat"],
                end_lng=route[-1]["lng"],

                start_time=start_time,
                end_time=end_time,
                trip_date=trip_date,

                distance=round(2.5 + i, 2),
                duration=duration_min,

                cost=30 + i * 10,
                companions=i % 3,

                mode=modes[i],

                route=route,
                map_image=None
            )

            db.session.add(t)
            trip_counter += 1

    db.session.commit()

    print(f"✅ {trip_counter-1} Dummy trips added for all users")
    
from datetime import datetime, timedelta

from app import app, db
from models import Trip, User   # 👈 import User model

with app.app_context():

    # Clear old trips
    db.session.query(Trip).delete()

    routes = [
        [
            {"lat": 12.9716, "lng": 77.5946},
            {"lat": 12.9720, "lng": 77.5950},
            {"lat": 12.9730, "lng": 77.5960}
        ],
        [
            {"lat": 12.9600, "lng": 77.5800},
            {"lat": 12.9610, "lng": 77.5810},
            {"lat": 12.9620, "lng": 77.5820}
        ],
        [
            {"lat": 12.9900, "lng": 77.6100},
            {"lat": 12.9910, "lng": 77.6110},
            {"lat": 12.9920, "lng": 77.6120}
        ]
    ]

    modes = [
        "Walk", "Bike", "Car",
        "Bus", "Auto", "Cycle",
        "Train", "Car", "Walk"
    ]

    purposes = [
        "Work", "Study", "Shopping",
        "Leisure", "Travel", "Gym",
        "Hospital", "Office", "Personal"
    ]

    now = datetime.utcnow()

    # 👇 Fetch all users
    users = User.query.all()

    trip_counter = 1

    for user in users:   # 🔥 loop through each user

        for i in range(9):   # 9 trips per user

            route = routes[i % 3]

            start_time = now - timedelta(days=i+1, hours=i+2)
            trip_date = start_time.date()

            duration_min = 10 + i * 3
            end_time = start_time + timedelta(minutes=duration_min)

            t = Trip(
                user_id=user.id,   # 👈 dynamic user id
                trip_no=f"TEST-{user.id:02d}-{i+1:02d}",  # unique trip no

                purpose=purposes[i],

                start_lat=route[0]["lat"],
                start_lng=route[0]["lng"],
                end_lat=route[-1]["lat"],
                end_lng=route[-1]["lng"],

                start_time=start_time,
                end_time=end_time,
                trip_date=trip_date,

                distance=round(2.5 + i, 2),
                duration=duration_min,

                cost=30 + i * 10,
                companions=i % 3,

                mode=modes[i],

                route=route,
                map_image=None
            )

            db.session.add(t)
            trip_counter += 1

    db.session.commit()

    print(f"✅ {trip_counter-1} Dummy trips added for all users")