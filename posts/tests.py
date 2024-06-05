import json

from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Usuario, Filme, Serie

class APITestCase(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.access_token = AccessToken.for_user(self.user)
        self.authorization_header = f'Bearer {self.access_token}'

    def test_create_usuario(self):
        # Teste de criação de usuário
        response = self.client.post('/api/usuarios/', {
            'email': 'novousuario@example.com'
        }, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.count(), 1)
        
        # Verifica se os dados do usuário foram salvos corretamente
        usuario = Usuario.objects.first()
        self.assertEqual(usuario.email, 'novousuario@example.com')

    def test_retrieve_usuario(self):
        # Cria um usuário
        usuario = Usuario.objects.create(email='teste@example.com')
        
        # Teste de recuperação de usuário
        response = self.client.get(f'/api/usuarios/{usuario.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se os dados do usuário recuperado estão corretos
        self.assertEqual(response.data['id'], usuario.id)
        self.assertEqual(response.data['email'], usuario.email)

    def test_update_usuario(self):
        # Cria um usuário
        usuario = Usuario.objects.create(email='teste@example.com')
        
        # Teste de atualização de usuário
        updated_data = {'email': 'usuarioatualizado@example.com'}
        response = self.client.put(f'/api/usuarios/{usuario.id}/', json.dumps(updated_data), content_type='application/json', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Recarrega o objeto do banco de dados
        usuario.refresh_from_db()

        # Verifica se os dados do usuário foram atualizados corretamente
        self.assertEqual(usuario.email, updated_data['email'])

    def test_delete_usuario(self):
        # Cria um usuário
        usuario = Usuario.objects.create(email='teste@example.com')
        
        # Teste de exclusão de usuário
        response = self.client.delete(f'/api/usuarios/{usuario.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Usuario.objects.count(), 0)

    def test_create_filme(self):
        # Teste de criação de filme
        response = self.client.post('/api/filmes/', {
            'titulo': 'Novo Filme',
            'diretor': 'Diretor Exemplo',
            'data_lancamento': '2024-05-24',
            'duracao_minutos': 120,
            'descricao': 'Descrição do novo filme'
        }, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Filme.objects.count(), 1)
        
        # Verifica se os dados do filme foram salvos corretamente
        filme = Filme.objects.first()
        self.assertEqual(filme.titulo, 'Novo Filme')
        self.assertEqual(filme.diretor, 'Diretor Exemplo')
        self.assertEqual(filme.data_lancamento, '2024-05-24')
        self.assertEqual(filme.duracao_minutos, 120)
        self.assertEqual(filme.descricao, 'Descrição do novo filme')

    def test_retrieve_filme(self):
        # Cria um filme
        filme = Filme.objects.create(titulo='Teste Filme', diretor='Diretor Teste', data_lancamento='2024-05-24', duracao_minutos=120, descricao='Descrição do teste')
        
        # Teste de recuperação de filme
        response = self.client.get(f'/api/filmes/{filme.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se os dados do filme recuperado estão corretos
        self.assertEqual(response.data['id'], filme.id)
        self.assertEqual(response.data['titulo'], filme.titulo)
        self.assertEqual(response.data['diretor'], filme.diretor)
        self.assertEqual(response.data['data_lancamento'], filme.data_lancamento)
        self.assertEqual(response.data['duracao_minutos'], filme.duracao_minutos)
        self.assertEqual(response.data['descricao'], filme.descricao)

    def test_update_filme(self):
        # Cria um filme
        filme = Filme.objects.create(titulo='Teste Filme', diretor='Diretor Teste', data_lancamento='2024-05-24', duracao_minutos=120, descricao='Descrição do teste')
        
        # Teste de atualização de filme
        updated_data = {
            'titulo': 'Filme Atualizado',
            'diretor': 'Diretor Atualizado',
            'data_lancamento': '2024-06-01',
            'duracao_minutos': 130,
            'descricao': 'Descrição atualizada'
        }
        response = self.client.put(f'/api/filmes/{filme.id}/', json.dumps(updated_data), content_type='application/json', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Recarrega o objeto do banco de dados
        filme.refresh_from_db()

        # Verifica se os dados do filme foram atualizados corretamente
        self.assertEqual(filme.titulo, updated_data['titulo'])
        self.assertEqual(filme.diretor, updated_data['diretor'])
        self.assertEqual(filme.data_lancamento, updated_data['data_lancamento'])
        self.assertEqual(filme.duracao_minutos, updated_data['duracao_minutos'])
        self.assertEqual(filme.descricao, updated_data['descricao'])

    def test_delete_filme(self):
        # Cria um filme
        filme = Filme.objects.create(titulo='Teste Filme', diretor='Diretor Teste', data_lancamento='2024-05-24', duracao_minutos=120, descricao='Descrição do teste')
        
        # Teste de exclusão de filme
        response = self.client.delete(f'/api/filmes/{filme.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Filme.objects.count(), 0)

    def test_create_serie(self):
        # Teste de criação de série
        response = self.client.post('/api/series/', {
            'titulo': 'Nova Série',
            'criador': 'Criador Exemplo',
            'data_estreia': '2024-05-24',
            'numero_temporadas': 3,
            'descricao': 'Descrição da nova série'
        }, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Serie.objects.count(), 1)
        
        # Verifica se os dados da série foram salvos corretamente
        serie = Serie.objects.first()
        self.assertEqual(serie.titulo, 'Nova Série')
        self.assertEqual(serie.criador, 'Criador Exemplo')
        self.assertEqual(serie.data_estreia, '2024-05-24')
        self.assertEqual(serie.numero_temporadas, 3)
        self.assertEqual(serie.descricao, 'Descrição da nova série')

    def test_retrieve_serie(self):
        # Cria uma série
        serie = Serie.objects.create(titulo='Teste Série', criador='Criador Teste', data_estreia='2024-05-24', numero_temporadas=3, descricao='Descrição do teste')
        
        # Teste de recuperação de série
        response = self.client.get(f'/api/series/{serie.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se os dados da série recuperada estão corretos
        self.assertEqual(response.data['id'], serie.id)
        self.assertEqual(response.data['titulo'], serie.titulo)
        self.assertEqual(response.data['criador'], serie.criador)
        self.assertEqual(response.data['data_estreia'], serie.data_estreia)
        self.assertEqual(response.data['numero_temporadas'], serie.numero_temporadas)
        self.assertEqual(response.data['descricao'], serie.descricao)

    def test_update_serie(self):
        # Cria uma série
        serie = Serie.objects.create(titulo='Teste Série', criador='Criador Teste', data_estreia='2024-05-24', numero_temporadas=3, descricao='Descrição do teste')
        
        # Teste de atualização de série
        updated_data = {
            'titulo': 'Série Atualizada',
            'criador': 'Criador Atualizado',
            'data_estreia': '2024-06-01',
            'numero_temporadas': 4,
            'descricao': 'Descrição atualizada'
        }
        response = self.client.put(f'/api/series/{serie.id}/', json.dumps(updated_data), content_type='application/json', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Recarrega o objeto do banco de dados
        serie.refresh_from_db()

        # Verifica se os dados da série foram atualizados corretamente
        self.assertEqual(serie.titulo, updated_data['titulo'])
        self.assertEqual(serie.criador, updated_data['criador'])
        self.assertEqual(serie.data_estreia, updated_data['data_estreia'])
        self.assertEqual(serie.numero_temporadas, updated_data['numero_temporadas'])
        self.assertEqual(serie.descricao, updated_data['descricao'])

    def test_delete_serie(self):
        # Cria uma série
        serie = Serie.objects.create(titulo='Teste Série', criador='Criador Teste', data_estreia='2024-05-24', numero_temporadas=3, descricao='Descrição do teste')
        
        # Teste de exclusão de série
        response = self.client.delete(f'/api/series/{serie.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Serie.objects.count(), 0)
