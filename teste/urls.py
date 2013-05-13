from django.conf.urls import patterns, include, url
from django.contrib import admin
import forms_builder.forms.urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teste.views.home', name='home'),
    # url(r'^teste/', include('teste.foo.urls')),
    url(r'^$', 'teste.views.home', name='home'),
    url(r'^criar/', 'teste.views.criar_editar_form', name='criar'),
    url(r'^editar/(?P<form_id>\d+)/', 'teste.views.criar_editar_form', name='editar'),
    url(r'^entradas/(?P<form_id>\d+)/', 'teste.views.entradas', name='entradas'),
    url(r'^formulario/(?P<form_id>\d+)/', 'teste.views.formulario', name='formulario'),
    url(r'^listar/', 'teste.views.listar', name='listar'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forms/', include(forms_builder.forms.urls)),
)
