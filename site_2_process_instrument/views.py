from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from site_2_process_instrument.forms import ContactForm
from django.core.mail import EmailMultiAlternatives
from site_2_process_instrument.models import Contact
#imported the model 
# from site_2_process_instrument.models import HomeSlider


# Create your views here.

def about(request):
    return render(request,"site2_instrument/project/about.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            form.save()
        return HttpResponse("done")
        

    

    return render(request,"site2_instrument/project/contact.html")




