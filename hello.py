from django.http import HttpResponse
from django.conf.urls import url

def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
    url(r'^$', index),
)
