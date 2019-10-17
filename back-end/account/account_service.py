from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.http import QueryDict

from baby_project import settings

import jwt, datetime

User = get_user_model()
key = "settings.SECRET_KEY"


def create_token(data):
    payload = set_payload(data)
    token = jwt.encode(payload, key, algorithm="HS256")
    
    return token


def set_payload(data):
    jwt_payload = {
        'email': data["email"],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
    }

    return jwt_payload


def user_authenticate(email, password):
    try:
        user = User.objects.get(email=email)
    
    except User.DoesNotExist:
        return False
    
    if user is None:
        return False

    return user.check_password(password)


def set_password(request):
    request_dict = request.data.dict()
    
    request_dict['password'] = make_password(request.data['password'])
    modified_data = QueryDict('', mutable=True)
    modified_data.update(request_dict)

    return modified_data
