from django.shortcuts import render

# Create your views here.
def ebook(request):
    return render(request,'ebook.html') 
def ebookpage1(request):
    return render(request,'ebookpage1.html') 
def ebookpage2(request):
    return render(request,'ebookpage2.html') 
def ebookpage3(request):
    return render(request,'ebookpage3.html')
def ebookpage4(request):
    return render(request,'ebookpage4.html') 
def ebookpage5(request):
    return render(request,'ebookpage5.html')  
def ebookstore(request):
    return render(request,'ebookstore.html')