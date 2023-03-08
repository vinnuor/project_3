from app2.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('abd/',abd,name='abd'),
    path('raina/',raina,name='raina')
]