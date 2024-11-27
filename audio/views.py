from django.shortcuts import render

# Create your views here.
def audio(request):
    return render(request,'audio.html')
def audiobook1(request):
    return render(request,'audiobook1.html')
def audiobook2(request):
    return render(request,'audiobook2.html')
def audiobook3(request):
    return render(request,'audiobook3.html')
def audiobook4(request):
    return render(request,'audiobook4.html')
def audiobook5(request):
    return render(request,'audiobook5.html')
def audiobookstore(request):
    return render(request,'audiobookstore.html')