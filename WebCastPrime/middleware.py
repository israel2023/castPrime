import logging

logger = logging.getLogger('custom')

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Código executado da finalização da view
        logger.info('Middleware executado: Interceptando requisição')

        # Verifica se o cabeçalho 'X-Meu-Header' está presente na requisição
        if 'X-Meu-Header' in request.headers:
            # Armazena o valor do cabeçalho na sessão do usuário
            request.session['meu_header'] = request.headers['X-Meu-Header']
            logger.info('Valor do cabeçalho armazenado na sessão: %s', request.session['meu_header'])
            
        # Chama o próximo middleware na cadeia ou a view correspondente
        response = self.get_response(request)
        # Código executado depois da view
        logger.info('Middleware executado: Interceptando resposta')
        return response