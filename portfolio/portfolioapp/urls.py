from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contactme',views.contactme,name='contactme'),
    path('LMS/',views.LMS,name='LMS'),
    path('cal/',views.cal,name='cal'),
    path('rps/',views.rps,name='rps'),
]
