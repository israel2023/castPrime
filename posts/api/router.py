from rest_framework import routers
from posts.api import viewsets

router= routers.DefaultRouter()
router.register('usuario', viewsets.UsuarioViewSet)
router.register('filme', viewsets.FilmeViewSet)
router. register('series', viewsets.SerieViewSet)