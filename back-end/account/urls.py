from django.urls import path
from .views import signup, login, personal, baby


urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('<str:account_name>', personal, name="personal"),
    path('<str:account_name>/<int:baby_id>', baby, name="personal"),
]
