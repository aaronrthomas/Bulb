from django.shortcuts import render

# Create your views here.
def abc(request):
    return render(request,'home.html')
def efg(request):
    return render(request,'pay.html')
def hij(request):
    return render(request,'about.html')
def rat(request):
    return render(request,'bulb.html')
def cat(request):
    return render(request,'contact.html')
def dog(request):
    return render(request,'F&Q.html')