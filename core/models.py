from django.db import models


class Participante(models.Model):
    cpf = models.CharField(max_length=15, unique=True)

    def __unicode__(self):
        return self.cpf


def upload_certificados(instance, filename):
    return 'uploads/certificados/{}/{}'.format(
        instance.participante.cpf.replace('.', '').replace('-', ''),
        instance.tipo + '.pdf'
    )


class Certificado(models.Model):
    TIPO_CHOICES = (
        ('palestra', u'Palestra'),
        ('curso-1', u'Curso 1'),
        ('curso-2', u'Curso 2')
    )
    participante = models.ForeignKey(Participante)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    arquivo = models.FileField(upload_to=upload_certificados)

    def __unicode__(self):
        return u'%s - %s' % (self.participante.cpf, self.get_tipo_display())
