from django.shortcuts import render

# Create your views here.
def display(request):
    return render(request,"home.html")

def theme(request):
    return render(request,'themecake.html')

def cakes(request):
    return render(request,'cakepastries.html')