from django.contrib import admin
from .models import registered_people,joining_people
# Register your models here.


admin.site.register(registered_people)
admin.site.register(joining_people)

