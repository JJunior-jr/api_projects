#!/c/Users/jacso/documents/00-Projetos_geral/00-Projetos_python/04-consumo_api_python/.venv/Scripts/python3


# criando as variáveis que receberão as listas de ceps

import requests

lista_ceps = ['01022000', '01310200', '04029200']
lista_end = []

# estrutura da requisicoes, fazer um "for" para iterar a cada chamada da api e mostra a resposta
# 1: na url uso o método ".format" para pegar os ceps da "lista_ceps" e conectar com o endpoint da  na url da
# api com isso o for faz a iteração.
# 2: Usar o "request" em uma variável com o metodo ".get" e dois parametros, a "url" e o "timeout"
# que aguarda até 3s para obter o resultado do "request.get()", caso precisase de autenticação
# teria que colocar mais parametros como o token de acesso.
# 3:crio uma variavel para pegar o objeto "req" que é fruto de um request e uso um metodo que é o 'json'
# 4: como o json é tipo um dicionario eu consulto o objeto "endereço" e pela chave


for cep in lista_ceps:

    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)  # 1

    req = requests.get(url, timeout=3)  # 2

    endereco = req.json()  # 3

    lista_end.append([endereco['cep'], endereco['logradouro'],
                     endereco['uf'], endereco['bairro']])  # 4


for item in lista_end:

    print(item)
