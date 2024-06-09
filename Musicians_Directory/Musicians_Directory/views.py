from django.shortcuts import render
from musician.models import Musician
from album.models import Albums

def home(request):
    data = Albums.objects.all()
    return render(request,'base.html',{'value': data})