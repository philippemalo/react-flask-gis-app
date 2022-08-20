from models import db_session, Shape

# Fill the table with some data
lake = Shape(name='Majeur', geom='POLYGON((0 0,1 0,1 1,0 1,0 0))')
db_session.add(lake)

db_session.commit()