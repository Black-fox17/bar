from django.shortcuts import render
import datetime
# Create your views here.
def date(request):
    x = datetime.datetime.now()
    y = x.day
    y1 = x.month
    y2 = x.year
    if y == 31 or y == 29:
        f = 0
    else:
        f = 30 - y
    f1 = y1 * 30
    fin = f1 - f
    h1 = (fin/360) * 100
    h2 = round(h1)
    h3 = 100 - h2
    return render(request,"bar/date.html",{"g":h2,"g2":h3})