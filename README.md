# Petshop Admin

Aplicação Django para administração de petshop com telas próprias para gerenciamento de clientes e pets, além da rota padrão do Django Admin.

## Requisitos

- Python 3 instalado
- `pip` disponível no ambiente
- Ambiente virtual Python recomendado
- Para uso com MySQL: servidor MySQL disponível e bibliotecas compatíveis com `mysqlclient`

## Dependências usadas atualmente

Pelos imports, apps instalados e configuração do banco, o projeto utiliza atualmente:

- `Django`
- `python-decouple`
- `dj-database-url`
- `django-adminlte`
- `django-localflavor`
- `mysqlclient` para conexão com MySQL

Exemplo de instalação base:

```powershell
python -m venv .venv
.venv\Scripts\Activate
python -m pip install --upgrade pip
pip install Django python-decouple dj-database-url django-adminlte django-localflavor
```

Se for usar MySQL, instale também:

```powershell
pip install mysqlclient
```

## Como configurar a aplicação

1. Crie e ative o ambiente virtual.
2. Instale as dependências do projeto.
3. Se for usar MySQL, instale também o `mysqlclient`.
4. Crie o arquivo `.env` a partir de `.env.example`.
5. Aplique as migrações.
6. Inicie o servidor de desenvolvimento.

Exemplo de configuração com SQLite:

```powershell
python -m venv .venv
.venv\Scripts\Activate
python -m pip install --upgrade pip
pip install Django python-decouple dj-database-url django-adminlte django-localflavor
Copy-Item .env.example .env
python manage.py migrate
python manage.py runserver
```

Exemplo de configuração com MySQL:

```powershell
python -m venv .venv
.venv\Scripts\Activate
python -m pip install --upgrade pip
pip install Django python-decouple dj-database-url django-adminlte django-localflavor mysqlclient
Copy-Item .env.example .env
python manage.py migrate
python manage.py runserver
```

Depois disso, a aplicação ficará disponível em:

- `http://127.0.0.1:8000/admin/`
- `http://127.0.0.1:8000/app/cliente/cadastro`
- `http://127.0.0.1:8000/app/cliente/lista`

## Atualizações implementadas na aplicação

- Cadastro de clientes com formulário separado entre dados pessoais e endereço
- Listagem de clientes com ações de visualizar, editar e remover
- Tela de detalhes do cliente
- Cadastro de pets vinculado a um cliente específico
- Tela de detalhes do pet
- Cadastro de consultas vinculado a um pet específico
- Tela de detalhes da consulta
- Histórico de consultas exibido no perfil do cliente e no perfil do pet
- Modelos persistidos para clientes, endereços, pets, consultas e funcionários
- Campos de estado com opções brasileiras via `django-localflavor`

## Estado atual das funcionalidades

- O fluxo de clientes possui cadastro, listagem, edição, remoção e visualização de detalhes
- O fluxo de pets possui cadastro por cliente e visualização de detalhes
- O fluxo de consultas possui cadastro por pet e visualização de detalhes
- O histórico de consultas aparece na tela de detalhes do cliente e do pet
- A entidade `Funcionario` já existe no modelo de dados, mas ainda não possui rotas próprias na aplicação

## Criando acesso ao admin

Para acessar o admin com um usuário próprio:

```powershell
python manage.py createsuperuser
```

Durante a criação, o Django solicitará:

- nome de usuário
- e-mail
- senha
- confirmação da senha

Depois de criar o superusuário:

1. Certifique-se de que o servidor está em execução com `python manage.py runserver`.
2. Acesse `http://127.0.0.1:8000/admin/` no navegador.
3. Informe o nome de usuário e a senha cadastrados.
4. Utilize o painel administrativo para gerenciar os modelos registrados.

## Variáveis de ambiente

O projeto usa `python-decouple` para ler configurações do arquivo `.env`.

Conteúdo atual de referência em `.env.example`:

```env
ENV_SECRET_KEY=cole_aqui_uma_secret_key_do_django
ENV_DEBUG=True
ENV_ALLOWED_HOSTS=127.0.0.1,localhost
ENV_DATABASE_URL=sqlite:///db.sqlite3
```

Exemplo com MySQL:

```env
ENV_DATABASE_URL=mysql://usuario:senha@localhost:3306/twjobs
```

## Configurações aplicadas em `setup/settings.py`

Resumo do que já está configurado no projeto:

- `BASE_DIR` é definido com `pathlib.Path`
- `SECRET_KEY` é lida da variável `ENV_SECRET_KEY`
- `DEBUG` é lido da variável `ENV_DEBUG`, com `False` como valor padrão
- `ALLOWED_HOSTS` é lido de `ENV_ALLOWED_HOSTS` usando lista separada por vírgulas
- Os apps `app`, `django_adminlte` e `localflavor` estão registrados em `INSTALLED_APPS`
- O banco de dados é configurado pela variável `ENV_DATABASE_URL`
- Se `ENV_DATABASE_URL` não for informada, o projeto usa SQLite local em `db.sqlite3`
- O idioma da aplicação está configurado como `pt-br`
- O fuso horário está configurado como `UTC`
- `USE_I18N` está habilitado
- `USE_TZ` está habilitado
- Os arquivos estáticos usam `STATIC_URL = 'static/'`
- O tipo padrão de chave primária é `BigAutoField`

## Rotas atuais

- `/admin/` para a área administrativa padrão do Django
- `/app/cliente/cadastro` para cadastro de clientes
- `/app/cliente/lista` para listagem de clientes
- `/app/cliente/<id>` para exibir os detalhes de um cliente
- `/app/cliente/editar/<id>` para editar um cliente existente
- `/app/cliente/excluir/<id>` para confirmar e remover um cliente
- `/app/pet/cadastro/<id>` para cadastrar um pet para o cliente informado
- `/app/pet/<id>` para exibir os detalhes de um pet
- `/app/consulta/cadastro/<id>` para cadastrar uma consulta para o pet informado
- `/app/consulta/<id>` para exibir os detalhes de uma consulta

## Estrutura atual do projeto

```text
petshop-admin/
|-- app/
|   |-- entidades/
|   |-- forms/
|   |-- services/
|   |-- templates/
|   |-- views/
|-- setup/
|-- .env.example
|-- .gitignore
|-- db.sqlite3
|-- manage.py
|-- README.md
```

## Observações

- Ainda não existe um arquivo de dependências versionado, como `requirements.txt`
- O projeto pode rodar com SQLite local ou MySQL, conforme a `ENV_DATABASE_URL`
- O banco SQLite `db.sqlite3` já existe no projeto, mas as migrações continuam sendo necessárias ao preparar um novo ambiente
- O módulo de consultas já possui rotas públicas para cadastro e detalhamento, mas ainda pode evoluir com listagens e manutenção próprias
- A entidade `Funcionario` segue disponível apenas no modelo de dados e no admin, sem fluxo público dedicado
