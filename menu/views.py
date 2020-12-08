from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from menu.models import Menu, MenuItem


def index(request):
    menu = Menu.objects.all()
    menuitem = MenuItem.objects.all()
    context = {'menu': menu, 'menumenuitem': menuitem}
    return render(request,'index.html' , context)