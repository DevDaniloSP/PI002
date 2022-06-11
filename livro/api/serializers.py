from rest_framework import serializers
from livro import models


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Livro
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emprestimo
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields ='__all__'
