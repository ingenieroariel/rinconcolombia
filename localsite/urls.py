from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'example/', 'vendamos.localsite.views.example', {}),
)
