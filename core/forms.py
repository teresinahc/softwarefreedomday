# coding: utf-8
import os
import zipfile

from django import forms
from django.http import HttpResponse
from .models import Participante


class CertificadoForm(forms.Form):
    cpf = forms.RegexField(label=u'Número do CPF:', required=True,
                           regex=r'\A\d{3}\.\d{3}\.\d{3}-\d{2}',
                           error_message=u'Digite um CPF válido')
    cpf.widget.attrs.update({'autofocus': 'autofocus', 'required': 'required'})

    error_css_class = 'alert alert-danger'

    def process(self):
        cpf = self.cleaned_data['cpf']
        participante = Participante.objects.get(cpf=cpf)
        if participante.certificado_set.count() == 1:
            return HttpResponse(participante.certificado_set.latest('id').arquivo,
                                content_type='application/pdf')
        # TODO: Implementar quando o participante tiver mais de um certificado

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        cpf = cpf.replace('.', '').replace('-', '')
        try:
            participante = Participante.objects.get(cpf=cpf)
        except Participante.DoesNotExist:
            raise forms.ValidationError(u'CPF não encontrado')
        if not participante.certificado_set.exists():
            raise forms.ValidationError(u'Participante sem certificados cadastrados')
        return cpf
