from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Home_Page_View(TemplateView):
    template_name = 'home.html'

class About_Page_View(TemplateView):
    template_name = 'about.html'
