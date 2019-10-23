import jwt, datetime

from baby_project import settings

key = settings.SECRET_KEY

def create_token(data):
    payload = set_payload(data)
    token = jwt.encode(payload, key, algorithm="HS256")
    return token


def decode_token(token):
    try:
        decoded = jwt.decode(token, key, algorithms="HS256")
        
        return decoded
    except jwt.ExpiredSignatureError:
        return False
    except jwt.DecodeError:
        return False


def set_payload(data):
    jwt_payload = {
        'email': data["email"],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
    }

    return jwt_payload