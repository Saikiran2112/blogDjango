from django.shortcuts import render
from .models import posts

def index(request):
    p=posts.objects.all()
    return render(request,"index.html",{'posts':p[::-1]})
def post(request,pk):
    p=posts.objects.get(id=pk)
    return render(request,"posts.html",{'posts':p})
