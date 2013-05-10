# -*- coding: utf-8 -*-

from django.db.transaction import commit_on_success
from django.forms.formsets import formset_factory
from django.shortcuts import get_object_or_404, render
from forms_builder.forms.models import Form, Field
from teste.forms import CadastroForm, CampoForm

def entradas(request, form_id):
    pass

def formulario(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    return render(request, 'formulario.html', locals())

def home(request):
    return render(request, 'home.html', locals())

def listar(request):
    forms = Form.objects.order_by('title').all()
    return render(request, 'listar.html', locals())

@commit_on_success
def novo(request):
    cadastro_form = CadastroForm(request.POST or None)
    CampoFormSet = formset_factory(CampoForm)
    campos_forms = CampoFormSet(request.POST or None)
    if request.method == 'POST' and all([f.is_valid() for f in [cadastro_form, campos_forms]]):
        cadastro_form.save()
        for f in campos_forms:
            f.instance.form = cadastro_form.instance
            f.save()
    return render(request, 'novo.html', locals())
