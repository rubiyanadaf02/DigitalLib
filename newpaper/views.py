from django.shortcuts import render

# Create your views here.
def newpaper(request):
    return render(request,'newpaper.html')