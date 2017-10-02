from django.http import HttpResponse
from django.conf.urls import url
from django.conf import settings
from django.core.wsgi import get_wsgi_application

import sys
import os

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', 'f#&o4)9ibe=k1ofu696+4rt8#5e73fsf9leuj5@-&$nf4%(#jn')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

def placeholder(request, width, height):
    # TODO: Rest of the view will go here
    return HttpResponse('Ok')

def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
    url(r'^$', index),
)

application = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
