from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.http import QueryDict

from baby_project import settings

User = get_user_model()


def user_authenticate(email, password):
    try:
        user = User.objects.get(email=email)
    
    except User.DoesNotExist:
        return False
    
    if user is None:
        return False

    return user.check_password(password)


def set_password(request):
    _mutable = request.data._mutable
    request.data._mutable = True

    request.data['password'] = make_password(request.data['password'])

    request.data._mutable = _mutable

    return request.data
