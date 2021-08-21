# flask-api
## Pré-requisitos:
A API foi testada usando os seguintes pacotes com suas respectivas versões

* flask 2.0.1
* flask_restful 0.3.9
* flask_script 2.0.6
* flask_migrate 3.1.0
* flask_sqlalchemy 2.5.1
* flask_marshmallow 0.14.0
* marshmallow 3.13.0
* marshmallow-sqlalchemy 0.26.1


_____

## Funcionalidades:
* API  REST  utilizando  JSON  para  realizar  um  CRUD  completo  em  uma tabela CLIENTE:
* GET (Lista clientes)
* POST (Criar cliente) 
* PUT (Editar cliente) 
* DELETE (Remover cliente) 
_____
## Outros:
* Modelo de Blueprints do Flask. 
* SQL Alchemy para conexão e manutenção das querys
* Migrações para criação da tabela no banco com os campos: 
    * código (primary_key / not null)
    * nome (not null)
    * razão social (not null)
    * cnpj (not null)
    * data_inclusao (datetime / not null)
    * Padrão  de  Respostas com status_code e mensagens de sucesso ou erro, como por exemplo. 
    ```
    { 
        "status": 200, 
        "message": "Cliente criado com sucesso" 
        "error": "null" 
    }
    ```


