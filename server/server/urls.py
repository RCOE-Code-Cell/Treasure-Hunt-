from django.contrib import admin
from django.urls import path, include
from django.http import  HttpResponse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns



def index(request):
    return HttpResponse("Hello, world!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name=  'index'),
    path('api/',include('cc_admin.urls')),
    path('api/',include('round.urls'))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns  += staticfiles_urlpatterns()








