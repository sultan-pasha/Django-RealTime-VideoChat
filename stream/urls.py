from django.urls import path
from .views import *

urlpatterns = [
        # 'livefe' -> function from views
        # 'live_camera' -> name at index.html>img src="{% url 'live_camera' %}
        path('', index, name="home"),
    ]