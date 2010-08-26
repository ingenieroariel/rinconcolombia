from django.conf.urls.defaults import *

from satchmo_store.urls import urlpatterns
from django.conf import settings

urlpatterns += patterns('',
    (r'test/', include('rinconcolombia.localsite.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),   
    )

