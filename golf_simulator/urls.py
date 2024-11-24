from django.urls import path
from . import views

urlpatterns = [
    path('simulate/', views.simulate_shot, name='simulate_shot'),
    path('result/', views.shot_result, name='shot_result'),
]