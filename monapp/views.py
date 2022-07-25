from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from monapp.models import Person

# Create your views here.
def index(request):
    return HttpResponse("<h1>Bonjour</h1>")

def user(request, id):
    return render(request, "monapp/user.html", locals())

def person(request):
    persons = Person.objects.all()
    return render(request, "monapp/person.html", {
        "persons": persons    
    })