from django.urls import path
from . import views


urlpatterns = [
    path('', views.predict_price, name='default'), 
    path('predict/', views.predict_price, name='predict_price'),
]