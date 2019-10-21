from django.urls import path
from .views import signup, login, personal, babies, follow


urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('<str:account_name>', personal, name="personal"),
    path('<str:account_name>/babies/', babies, name="babies"),
    path('<str:account_name>/follow/', follow, name="follow"),
]
