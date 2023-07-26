from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse

# Create your views here.
@cache_page(60 * 15)
def asd(request):
    response = HttpResponse("Привет, мир!")
    response['Cache-Control'] = 'public, max-age=3600'
    response['Expires'] = 'Sun, 19 Jan 2038 05:00:00 GMT'
    return response