from django.conf.urls import patterns, include, url
from django.contrib import admin
import forms_builder.forms.urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forms/', include(forms_builder.forms.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)

urlpatterns += patterns('teste.views',
    # Examples:
    # url(r'^$', 'teste.views.home', name='home'),
    # url(r'^teste/', include('teste.foo.urls')),
    url(r'^$', 'home', name='home'),
    url(r'^criar/', 'criar_editar_form', name='criar'),
    url(r'^editar/(?P<form_id>\d+)/', 'criar_editar_form', name='editar'),
    url(r'^entradas/(?P<form_id>\d+)/', 'entradas', name='entradas'),
    url(r'^formulario/(?P<form_id>\d+)/', 'formulario', name='formulario'),
    url(r'^listar/', 'listar', name='listar'),
)
