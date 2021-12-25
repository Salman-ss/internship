from django.shortcuts import render
from django .db import models
from . models import Products

# Create your views here.

def auth(request):
    if request.method == 'POST':
        id=request.POST['username']
        print(id)
    return render(request,'index.html')