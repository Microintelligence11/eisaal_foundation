from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, "about.html")


def achievement(request):
    return render(request, "achievement.html")



def national_donation(request):
    return render(request, "national_donation.html")


def international_donation(request):
    return render(request, "international_donation.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if len(name) <2  or len(email) <10 or len(message) < 10:
            messages.error(request, "pleces fill the form correctly.")
        else:
            contact = Contact(name=name, email=email, message=message)
            contact.save()
            messages.success(request,"your form has been submitted sucessfuly")

    return render(request, "contact.html")


def donationUpcomingProject(request):
    return render(request, "donationUpcomingProject.html")