from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin # Uncomment the next two lines to enable the admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')), # Uncomment the admin/doc line below to enable admin documentation    
	url(r'^admin/', include(admin.site.urls)), # Uncomment the next line to enable the admin
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}), 
    url(r'^$', 'principal.views.inicio'), 
    url(r'^usuarios/$', 'principal.views.usuarios'), 
    url(r'^recetas/$', 'principal.views.lista_recetas'), 
    url(r'^receta/(?P<id_receta>\d+)$', 'principal.views.detalle_receta'), 
    url(r'^sobre/$', 'principal.views.sobre'), 
)
