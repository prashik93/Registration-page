from django.contrib import admin
from .models import Registration

# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name','dob','email','phone','gender','flat','street','country','img']

admin.site.register(Registration,RegistrationAdmin)