from app2.views import *
from django.urls import path

app_name='nothing'

urlpatterns=[
    path('das/',das,name='das'),
]