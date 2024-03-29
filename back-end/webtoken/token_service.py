from django.contrib.auth import get_user_model
import jwt, datetime

from baby_project import settings

key = settings.SECRET_KEY
User = get_user_model()

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
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30000)
    }

    return jwt_payload


def check_user(user, token):
    decoded_token = decode_token(token)

    if user == User.objects.get(email=decoded_token['email']):
        return True
    
    return False
