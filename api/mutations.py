from models import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import bcrypt

engine = create_engine("postgresql://user:pass@localhost:5432/db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def resolve_createUser(obj, info, email, password):
    try:
        check_email = session.query(User).filter_by(email=email)
        check = session.query(check_email.exists())
        if check:
            raise Exception('This email is already in use!')

        byte_pwd = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(byte_pwd, bcrypt.gensalt())

        new_user = User(email=email, password=hashed_password)

        session.add(new_user)
        session.commit()

        # Make sure the new user is created before returning the payload
        created_user = session.query(User).filter_by(email=new_user.email).first()

        payload = {
            "success": True,
            "user": created_user.to_dict()
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload