from django.shortcuts import render

def welcomepage(request):
    return render(request, 'welcomepage.html')
 