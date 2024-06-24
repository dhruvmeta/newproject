from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('about/',views.about),
   path('contact/',views.contact),
   path('service/',views.service),
   path('team/',views.team),
   path('booking/',views.booking),
   path('menu/',views.menu),
   path('testimonial/',views.testimonial),

]