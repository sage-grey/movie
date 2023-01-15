from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import movie_details
# Create your views here.



def index(request):
    obj=movie_details.objects.all()

    return render(request,"index.html",{'details':obj})

def details(request,movie_id):
    obj1=movie_details.objects.get(id=movie_id)

    return render(request,"about.html",{'details2':obj1})

def add(request):
    if request.method=="POST":
        name=request.POST.get('name')
        des = request.POST.get('des')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie=movie_details(name=name,des=des,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,movie_id):
    movie=movie_details.objects.get(id=movie_id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{'form':form,'movie':movie})

def delete(request,movie_id):
    if request.method=='POST':
        movie=movie_details.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')


    return render(request,'delete.html')