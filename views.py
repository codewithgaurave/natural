from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import sContact

# Create your views here.
def index(request):
    context={
            "variable1":"gaurav is a great man",
            "variable2":"zeeshan is a great man"
    }
    return render(request, 'index.html' ,context)
    #return HttpResponse("THIS IS HOME PAGE")

def about(request):
    return render(request, 'about.html' )

def services(request):
    return render(request, 'services.html' )

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        des=request.POST.get('des')
        contact=sContact(name=name,email=email,phone=phone,des=des,date=datetime.today())
        contact.save()
    return render(request, 'contact.html')