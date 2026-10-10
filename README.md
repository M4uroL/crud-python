# Users API

API REST para gerenciamento de usuários, desenvolvida com Flask, Flask-SQLAlchemy e MySQL. Permite cadastrar, listar, consultar, atualizar e excluir usuários.

> **Status:** o código-fonte atual é um protótipo e precisa de correções antes de executar. Consulte a seção [Pendências conhecidas](#pendências-conhecidas).

## Funcionalidades

- Listar todos os usuários
- Consultar um usuário pelo ID
- Cadastrar um usuário
- Atualizar nome e/ou e-mail
- Excluir um usuário

## Tecnologias

- Python
- Flask
- Flask-SQLAlchemy
- MySQL
- PyMySQL

## Requisitos

- Python 3.9 ou superior
- MySQL
- pip

## Instalação

Clone o repositório e acesse a pasta do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

Linux ou macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install Flask Flask-SQLAlchemy PyMySQL
```

## Configuração do banco de dados

Crie um banco de dados MySQL:

```sql
CREATE DATABASE database;
```

Configure a URI de conexão no aplicativo usando este formato:

```text
mysql+pymysql://USUARIO:SENHA@HOST:3306/NOME_DO_BANCO
```

Exemplo para um MySQL local:

```text
mysql+pymysql://root:SENHA@localhost:3306/database
```

Substitua `USUARIO`, `SENHA`, `HOST` e `NOME_DO_BANCO` pelos dados do seu ambiente. Não envie credenciais para o repositório; prefira carregá-las por variáveis de ambiente.

## Criar as tabelas

Com o aplicativo configurado, abra o shell do Flask:

```bash
flask --app app shell
```

No shell, execute:

```python
from app import db
db.create_all()
```

## Executar a aplicação

Depois de corrigir o arquivo para iniciar o servidor diretamente, execute:

```bash
python app.py
```

Por padrão, a API estará disponível em:

```text
http://127.0.0.1:5000
```

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/user` | Retorna a lista de usuários |
| `GET` | `/user/<id>` | Retorna um usuário pelo ID |
| `POST` | `/user/` | Cadastra um usuário |
| `PUT` | `/user/<id>` | Atualiza um usuário |
| `DELETE` | `/user/<id>` | Exclui um usuário |

### Cadastrar usuário

O corpo da requisição deve conter `name` e `email`:

```bash
curl -X POST http://127.0.0.1:5000/user/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana Silva","email":"ana@example.com"}'
```

### Listar usuários

```bash
curl http://127.0.0.1:5000/user
```

### Consultar usuário

```bash
curl http://127.0.0.1:5000/user/1
```

### Atualizar usuário

Envie um ou ambos os campos: `name` e `email`.

```bash
curl -X PUT http://127.0.0.1:5000/user/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana Souza"}'
```

### Excluir usuário

```bash
curl -X DELETE http://127.0.0.1:5000/user/1
```

## Modelo de dados

Cada usuário possui os seguintes campos:

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | Inteiro | Identificador único gerado pelo banco |
| `name` | Texto | Nome do usuário, até 50 caracteres |
| `email` | Texto | E-mail do usuário, até 120 caracteres |

## Pendências conhecidas

O código atual contém problemas que devem ser corrigidos antes do uso:

- O método `to_json()` deve acessar os atributos com `self`, por exemplo, `self.id`.
- A criação do usuário na rota `POST` contém um erro de sintaxe.
- A função que monta as respostas HTTP tem erros na montagem do conteúdo e no nome do argumento `mimetype`.
- As rotas devem tratar IDs inexistentes e retornar `404`.
- A rota `PUT` usa uma variável não definida ao montar a resposta.
- A rota `DELETE` deve usar `db.session.commit()` e retornar uma resposta válida.
- O servidor deve ser iniciado dentro de `if __name__ == "__main__":`.
- O import de `mysql.connector` não é utilizado pelo código apresentado.

## Licença

Adicione aqui a licença escolhida para o projeto.
