from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'example/', 'rinconcolombia.localsite.views.example', {}),
)
