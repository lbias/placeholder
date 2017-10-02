from django.http import HttpResponse
from django.conf.urls import url
from django.conf import settings

def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
    url(r'^$', index),
)

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)
