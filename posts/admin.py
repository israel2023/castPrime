from django.contrib import admin


from .models import Usuario, Filme, Serie

#Registrando meus modelos, permitindo que meus modelos sejam a acessíveis e gerenciáveis atraves da interface de administração do Django
admin.site.register(Usuario)
admin.site.register(Filme)
admin.site.register(Serie)
