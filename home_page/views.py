from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from home_page.models import HomeSlider

    


def Home(request):
    return render(request,"scienco_home/index.html")

def SiteOneHome(request):
    return render(request,"site1_printing/project/index.html")


def SiteTwoHome(request):
    
    context = {
        "home_slider": HomeSlider.objects.all()
    }
   

    return render(request,"site2_instrument/project/index.html",context)