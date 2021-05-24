from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name="welcome"),
    path('news_of_day',views.news_of_day,name="news_of_day")


]
