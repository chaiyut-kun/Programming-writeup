import datetime
import calendar

date_time =  datetime.datetime( 2009, *reversed(list( map( int , input().split() ) )) )
day_in_week = calendar.day_name[date_time.weekday()]
print(day_in_week)