from app1.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('king/',king,name='king'),
    path('vikin/',vikin,name='vikin')
    
]