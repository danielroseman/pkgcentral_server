from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^pkgcentral/', include('pkgcentral.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^submit/(?P<checksum>\S+)/$', 'packages.views.submit'),
    url(r'^host_compare/(?P<source_name>[\w.]+)/(?P<comparator_name>[\w.]+)/$',
     'packages.views.host_differences', name='host_compare'),
    url(r'^version_compare/(?P<source_name>[\w.]+)/(?P<comparator_name>[\w.]+)/$',
     'packages.views.version_differences', name='version_compare'),
)
