from django.urls import path
from .views import *
app_name = 'app'
urlpatterns = [
     path('', asd, name='show_mainpage')
]