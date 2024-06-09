from django.shortcuts import render,redirect
from . import form
from . import models

def add(request):
    if request.method == "POST":
        input_form = form.AlbumForm(request.POST)
        print('hello')
        if input_form.is_valid():
            #print(input_form.cleaned_data)
            input_form.save()
            return redirect('album')
    else:
        input_form = form.AlbumForm()
    return render(request,'add.html', {"forms":input_form})

def edit(request,id):
    data = models.Albums.objects.get(pk=id)
    form_data = form.AlbumForm(instance=data)
    if request.method == "POST":
        form_data = form.AlbumForm(request.POST, instance = data)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')
    return render(request,'edit.html',{"form" : form_data})
    
 
    
    
    