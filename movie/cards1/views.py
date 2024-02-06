from django.shortcuts import render
from cards1.models import Movie
from cards1.forms import movieform

# Create your views here.

def home(request):
    m=Movie.objects.all()
    return render(request,'home.html',{'m':m})
def add(request):
    if(request.method=="POST"):
        form=movieform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return home(request)
    form=movieform()
    return render(request,'add.html',{'form':form})
def view(request,p):
    m=Movie.objects.get(id=p)
    return render(request,'view.html',{'m':m})
def delete(request,p):
    m=Movie.objects.get(id=p)
    m.delete()
    return home(request)
def update(request,p):
    m = Movie.objects.get(id=p)
    if (request.method == "POST"):
        form = movieform(request.POST, request.FILES,instance=m)
        if form.is_valid():
            form.save()
            return home(request)

    form=movieform(instance=m)

    return render(request,'update.html',{'form':form})

