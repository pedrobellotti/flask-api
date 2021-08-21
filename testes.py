import requests

url = 'http://127.0.0.1:5000/api/'

#Adiciona clientes
cliente1={'codigo':'321',
'nome':'Teste 1', 
'razao_social': 'Cliente de Teste',
'cnpj': '12.345.678/0001-10'}
resp = requests.post(url + 'clientes', data=cliente1)
print(resp.json())

cliente2={'codigo':'987',
'nome':'Teste 2', 
'razao_social': 'Cliente de Teste 2',
'cnpj': '98.765.432/0001-99'}
resp = requests.post(url + 'clientes', data=cliente2)
print(resp.json())

#Lista todos os clientes
resp = requests.get(url + 'clientes')
print(resp.json())

#Remove o cliente codigo 321
resp = requests.delete(url + 'clientes', data=cliente1)
print(resp.json())

#Atualiza o nome do cliente 987
cliente2={'codigo':'987', 'nome': 'Cliente 2'}
resp = requests.put(url + 'clientes', data=cliente2)
print(resp.json())