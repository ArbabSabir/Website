from django.shortcuts import render



def Home(request):
    return render(request,"index.html")

def AboutUs(request):
    return render(request,"about.html")

def ContactUS(request):
    return render(request,"contact.html")

def Services(request):
    return render(request, "service.html")
