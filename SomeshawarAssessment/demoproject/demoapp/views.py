from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Registration
from .forms import RegistrationForm

# Create your views here.

def registrationView(request):
    reg = Registration.objects.all()
    form = RegistrationForm()
    if request.method == 'GET':
        template_name = 'demoapp/registration.html'
        context = {'form': form,'reg':reg}
        return render(request, template_name, context)

    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            gender = form.cleaned_data['gender']
            flat = form.cleaned_data['flat']
            street = form.cleaned_data['street']
            country = form.cleaned_data['country']
            img = form.cleaned_data['img']
            usr = Registration(name=name,dob=dob,email=email,phone=phone,gender=gender,flat=flat,street=street,
                               country=country,img=img)
            usr.save()

        return HttpResponse(f"{name}, {dob}, {email}, {phone}, {gender}, {flat},{street},{country}, {img}")

