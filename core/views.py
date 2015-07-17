from django.shortcuts import render
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

from .models import Participante
from .forms import CertificadoForm


class CertificadoView(FormView):
    template_name = 'index.html'
    form_class = CertificadoForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return form.process()
