import http
from models import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import bcrypt
from flask import request, make_response
import jwt

engine = create_engine("postgresql://user:pass@localhost:5432/db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def resolve_createUser(obj, info, email, password):
    try:
        check_email = bool(session.query(User).filter_by(email=email).first())
        
        if check_email:
            raise Exception('This email is already in use!')

        byte_pwd = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(byte_pwd, bcrypt.gensalt())

        new_user = User(email=email, password=hashed_password.decode('utf-8'))

        session.add(new_user)
        session.commit()

        # Make sure the new user is created before returning the payload
        created_user = session.query(User).filter_by(email=new_user.email).first()

        # jwt secret should be stored in env var and if possible should be changed regularly
        token = jwt.encode({"user": {"id": created_user.id, "email": created_user.email}}, "secret", algorithm="HS256")
        # decode_token = jwt.decode(token, "secret", algorithms=["HS256"])

        payload = {
            "success": True,
            "user": created_user.to_dict(),
            "jwt": token
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload