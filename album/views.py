from django.shortcuts import render

# Create your views here.
def album(request):
    return render(request,'album.html') 
def payment(request):
    return render(request,'payment.html') 
def order(request):
    return render(request,'order.html') 