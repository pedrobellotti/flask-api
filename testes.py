import requests

url = 'http://127.0.0.1:5000/api/'

#Adiciona clientes
cliente={'codigo':'321',
'nome':'Teste 1', 
'razao_social': 'Cliente de Teste',
'cnpj': '12.345.678/0001-10'}
resp = requests.post(url + 'clientes', data=cliente)
print(resp.json())

cliente={'codigo':'987',
'nome':'Teste 2', 
'razao_social': 'Cliente de Teste 2',
'cnpj': '98.765.432/0001-99'}
resp = requests.post(url + 'clientes', data=cliente)
print(resp.json())

#Lista todos os clientes
resp = requests.get(url + 'clientes')
print(resp.json())

#Remove o cliente codigo 321

#Atualiza o nome do cliente 987