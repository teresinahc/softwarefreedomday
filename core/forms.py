# coding: utf-8

from django import forms
from django.http import HttpResponse
from .models import Participante


class CertificadoForm(forms.Form):
    cpf = forms.RegexField(required=True, regex=r'\A\d{3}\.\d{3}\.\d{3}-\d{2}', error_message=u'Digite um CPF válido')

    def process(self):
        cpf = self.cleaned_data['cpf']
        participante = Participante.objects.get(cpf=cpf)
        return HttpResponse(participante.certificado, content_type='application/pdf')

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        cpf = cpf.replace('.', '').replace('-', '')
        participante = Participante.objects.filter(cpf=cpf)
        if not participante.exists():
            raise forms.ValidationError(u'CPF não encontrado')
        return cpf
