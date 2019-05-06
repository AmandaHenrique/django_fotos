from django.db import models

# Create your models here.

class Crush(models.Model):
    signo_opcoes = [
        ('ar', 'áries'),
        ('tr', 'touro'),
        ('gm', 'gêmeos'),
        ('cr', 'cancer'),
        ('le', 'leão'),
        ('vr', 'virgem'),
        ('lb', 'libra'),
        ('es', 'escorpiao'),
        ('sg', 'sargitário'),
        ('cp', 'capricórnio'),
        ('aq', 'aquario'),
        ('px', 'peixes'),
    ]


    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    data = models.DateField()
    signo = models.CharField(choices= signo_opcoes, max_length=2)
    qualidade = models.CharField(max_length=100)
    defeito = models.CharField(max_length=100, default= 'Não esta comigo')
    reciproco = models.BooleanField(default=False)
    solteiro = models.BooleanField(default=True)
    foto = models.ImageField(upload_to = '', null = True)

    def __str__(self):
        return self.nome