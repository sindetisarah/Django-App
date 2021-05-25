from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse("Hello welcome to my Website")
def news_of_day(request):
    date=dt.date.today()
    #calling the convert day function
    day=convert_dates(date)
    html=f'''
        <html>
        <body>
        <h1>News for {day} {date.day}-{date.month}-{date.year}</h1></body>
        </html>


    '''
    return HttpResponse(html)
    # //getting the day of the week
    
def convert_dates(dates):
    day_number=dt.date.weekday(dates)
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #returning the actual days of the week
    day=days[day_number]
    return day
#A function to capture a particular day the news was issued
def past_days_news(request,past_date):
    try:
        #strptime function passes in date as a string and is late coveted to a date object by the date function
        date=dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        raise Http404()