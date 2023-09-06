from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse  
def index(request):  
    return render(request,'index.html')  

def shop(request):
    return render(request, 'shop.html')

def detail(request):
    return render(request, 'detail.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')
