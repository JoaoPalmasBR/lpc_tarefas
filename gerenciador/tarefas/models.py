from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nome=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    senha=models.CharField(max_length=200)
    
    def __str__(self):
        return '{}'.format(self.nome)

class Projeto(models.Model):
    nome=models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.nome)

class ProjetoUsuario(models.Model):
    projeto=models.ForeignKey('Projeto')
    usuario=models.ForeignKey('Usuario')
    def __str__(self):
        return '{}'.format(self.projeto.nome+" - "+self.usuario.nome)

class Tarefa(models.Model):
    nome=models.CharField(max_length=200)
    dataEHoraDeInicio=models.DateTimeField('dataEHoraDeInicio', default=timezone.now)
    usuario=models.ForeignKey('Usuario')
    projeto=models.ForeignKey('Projeto')