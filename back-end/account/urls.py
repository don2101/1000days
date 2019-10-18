from django.urls import path
from .views import signup, login, personal, babies


urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('<str:account_name>', personal, name="personal"),
    path('<str:account_name>/babies/', babies, name="babies"),
]
