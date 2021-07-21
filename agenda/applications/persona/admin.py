from django.contrib import admin

from .models import Person,Reunion, Hobby

admin.site.register(Person)
admin.site.register(Reunion)
admin.site.register(Hobby)

