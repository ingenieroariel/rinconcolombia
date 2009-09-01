from django.conf.urls.defaults import *

from satchmo_store.urls import urlpatterns

urlpatterns += patterns('',
    (r'test/', include:('rinconcolombia.localsite.urls'))
)
