from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse("Hello welcome to my Website")
def news_of_day(request):
    date=dt.date.today()
    #calling the convert day function
    # day=convert_dates(date)
    html=f'''
        <html>
        <body>
        <h1>News for  {date.day}-{date.month}-{date.year}</h1></body>
        </html>


    '''
    return HttpResponse(html)
# def convert_dates(date):
#     day_number=dt.date.weekday
#     days=['Monday','Tuesday','Wednesday','Thursday','Friday']
#     day=days[day_number]
#     return day
