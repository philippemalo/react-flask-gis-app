from models import db_session, Shape

shapes = db_session.query(Shape).order_by(Shape.id)

for shape in shapes:
    print('geom: ', shape.geom)
    print('ST_AsText: ', shape.geom.ST_AsText)
    