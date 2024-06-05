from rest_framework import serializers
from ..models import Usuario, Filme, Serie

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'senha']

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['id', 'titulo', 'diretor', 'data_lancamento', 'duracao_minutos', 'descricao', 'criado_em', 'capa_url', 'url_filme']

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ['id', 'titulo', 'criador', 'data_estreia', 'numero_temporadas', 'descricao', 'criado_em', 'capa_url', 'url_serie']
