from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        'variable1':"this is Python",
        'variable2':"this is Django"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        disc = request.POST.get('desc')
        datetime.today()
        contact = Contact(name = name, email = email, phone = phone, desc = desc, datetime = datetime.today())
        contact.save()


    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")