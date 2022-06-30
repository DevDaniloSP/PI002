from typing import Any
from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

def upload_image_livro(instance, filename):
    return f"{instance.isbn}-{filename}"

class Livro(models.Model):
    isbn = models.IntegerField()
    titulo = models.CharField(max_length=150, null=True)
    thumb = models.ImageField(upload_to=upload_image_livro,blank=True, null=True)
    autor = models.CharField(max_length=150, null=True)
    editora = models.CharField(max_length=150, null=True)
    assunto = models.CharField(max_length=150, null=True)
    resumo = models.TextField(max_length=500, null=True)
    data_cadastro = models.DateField(default=date.today)

    def __str__(self):
        return self.titulo


class Emprestimo(models.Model):
    isbn = models.ForeignKey(Livro, on_delete=models.PROTECT)
# Chave que conectará ao banco de livros
    ra = models.ForeignKey('Usuario', on_delete=models.CASCADE)
# Chave que conectará com a table de empréstimo
    dataemp = models.DateTimeField()
# Nome alternativo: Empréstimo
    datadev = models.DateTimeField(blank=True, null=True)
# Nome alternativo: Devolução
    ativo = models.BooleanField(default=False)
    data_cadastro = models.DateField(default=date.today)

    #def __str__(self):
    #    return self.isbn

    def __str__(self) -> int:
        return f"{self.ra} | {self.livro}"    

class Usuario(AbstractUser):
    ra = models.IntegerField(null=True , blank=True)
    # Chave que conectará com a table de empréstimo
    ano = models.CharField(max_length=50)
    turma = models.CharField(max_length=50)
#    data_cadastro = models.DateField(default=date.today)
