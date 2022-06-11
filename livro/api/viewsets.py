from rest_framework import viewsets
from livro.api import serializers
from livro import models


class LivroViewset(viewsets.ModelViewSet):
    serializer_class = serializers.LivroSerializer
    queryset = models.Livro.objects.all()
 
class EmprestimoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.EmprestimoSerializer
    queryset = models.Emprestimo.objects.all()

class UsuarioViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UsuarioSerializer
    queryset = models.Usuario.objects.all()

