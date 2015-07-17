from django.db import models


class Participante(models.Model):
    cpf = models.CharField(max_length=15, unique=True)
    certificado = models.FileField(upload_to='uploads/certificados')

    def __unicode__(self):
        return self.cpf
