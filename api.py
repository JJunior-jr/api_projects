#!/c/Users/jacso/documents/00-Projetos_geral/00-Projetos_python/04-consumo_api_python/.venv/Scripts/python3


# criando as variáveis que receberão as listas de ceps

import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


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
# 5:iteração agora da lista de endereços de acordo com a chave/valor mencionada na variável
# 6: criando o dataframe com pandas, e atribuindo as os nomes das colunas para que já seja gravado de forma
# correta no banco de dados


for cep in lista_ceps:

    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)  # 1

    req = requests.get(url, timeout=10)  # 2

    endereco = req.json()  # 3

    lista_end.append([endereco['cep'],
                      endereco['logradouro'],
                     endereco['uf'],
                      endereco['bairro']])  # 4


df_enderecos = pd.DataFrame(
    lista_end, columns=['cep', 'logradouro', 'uf', 'bairro'])  # 6

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>AULA 2<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#1 Conexão de url com o banco de dados 
#2 O objeto 'create_engine' para a partir da url ele criar a conexão 
load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')

# db_connection= 'mysql+pymysql://user:password@host:port/database'
db_connection = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}' #1
db_connection = create_engine(db_connection) #2
df_enderecos.to_sql(con=db_connection, name='enderecos',
                    if_exists='append', index=False)

print('Dados carregados!!')

# for item in lista_end:  # 5
#   print(item)
