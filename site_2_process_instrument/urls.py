from django.urls import path
from . import views
from site_2_process_instrument import views

urlpatterns = [
    
    
    path('about/', views.about,name="About"),
    path('contact/', views.contact, name="Contact"),
    
]
