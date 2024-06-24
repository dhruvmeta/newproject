from django.shortcuts import render
from .forms import bookingform

# Create your views here.
def index(request):
    if request.method=='POST':
       newbooking=bookingform(request.POST)
       if newbooking.is_valid():
           newbooking.save()
           print("booking successfuly !")  
       else:
            print(newbooking.errors)
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def booking(request):
    if request.method=='POST':
       newbooking=bookingform(request.POST)
       if newbooking.is_valid():
           newbooking.save()
           print("booking successfuly !")  
       else:
            print(newbooking.errors)   
    return render(request,'booking.html')

def menu(request):
    return render(request,'menu.html')

def testimonial(request):
    return render(request,'testimonial.html')
