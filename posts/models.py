from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    
    email = models.EmailField(max_length=254, unique=True)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.senha



class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=50)
    data_lancamento = models.DateField()
    duracao_minutos = models.IntegerField()
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    capa_url = models.URLField(blank=True)
    url_filme = models.URLField(blank=True)
    

    def __str__(self):
        return self.titulo


class Serie(models.Model):
    titulo = models.CharField(max_length=100)
    criador = models.CharField(max_length=50)
    data_estreia = models.DateField()
    numero_temporadas = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    capa_url = models.URLField(blank=True)
    url_serie = models.URLField(blank=True)

    def __str__(self):
        return self.titulo


