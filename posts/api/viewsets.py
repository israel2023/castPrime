from rest_framework import viewsets, permissions
from ..models import Usuario, Filme, Serie
from .serializers import UsuarioSerializer, FilmeSerializer, SerieSerializer
import logging
logger = logging.getLogger('custom')

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        logger.info(f'Novo usuário criado: {self.request.data["email"]}')
        serializer.save()
    
    # Falta fazer autenticação e Autorização

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
