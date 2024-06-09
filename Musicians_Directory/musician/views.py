from django.shortcuts import render,redirect
from .form import Musicianform
from . import models

def add(request):
    if request.method == 'POST':
        input_form = Musicianform(request.POST)
        if input_form.is_valid():
            input_form.save()
            return redirect('musicians')
    else:
        input_form = Musicianform()
    return render(request,'add.html',{'forms': input_form})

def delete(request,id):
    data = models.Musician.objects.get(pk=id)
    data.delete()
    return redirect('home')

def edit_musician(request,id):
    data = models.Musician.objects.get(pk=id)
    form_data = Musicianform(instance=data)
    if request.method == 'POST':
        form_data = Musicianform(request.POST,instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')
    return render(request,'edit.html',{'form' : form_data})

