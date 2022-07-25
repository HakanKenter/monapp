from monapp.models import Person
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(City)
admin.site.register(PersonAddress)
admin.site.register(Interest)