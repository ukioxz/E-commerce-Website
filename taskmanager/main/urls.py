from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('items', views.about)
]