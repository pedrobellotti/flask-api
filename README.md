# flask-api
a. API  REST  utilizando  JSON  para  realizar  um  CRUD  completo  em  uma tabela CLIENTE:

i. GET (Lista clientes)

ii. POST (Criar cliente) 

iii. PUT (Editar cliente) 

iv. DELETE (Remover cliente) 


b. Dê preferência para o modelo de Blueprints do Flask. 


c. Se possível, utilizar algum ORM para conexão e manutenção das querys (Sugestão: SQL Alchemy) 


d. Criar Migrações para criação da tabela no banco com os campos: 

i. código (primary_key / not null),

ii. nome (not null)

iii. razão social (not null)

iv. cnpj (not null),

v. data_inclusao (datetime / not null)

e. Criar  um  Padrão  de  Respostas  para  API,  com  status_code  e  mensagens  de sucesso ou erro, como por exemplo. 
```
    { 
    "status": 200, 
    "message": "Cliente criado com sucesso" 
    "error": "null" 
}
```

