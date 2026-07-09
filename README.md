# Petshop Admin

Aplicação Django inicial com painel administrativo habilitado em `/admin/`.

## Requisitos

- Python 3 instalado
- `pip` disponível no ambiente
- Ambiente virtual Python recomendado

## Dependências usadas atualmente

Pelos imports e configurações do projeto, as bibliotecas necessárias até o momento são:

- `Django`
- `python-decouple`
- `dj-database-url`
- `django-adminlte`

Exemplo de instalação:

```cmd
python -m venv .venv
.venv\Scripts\Activate
python -m pip install --upgrade pip
pip install Django python-decouple dj-database-url django-adminlte
```

## Como configurar a aplicação

1. Crie e ative o ambiente virtual.
2. Instale as dependências.
3. Crie o arquivo `.env` a partir de `.env.example`.
4. Aplique as migrações.
5. Inicie o servidor de desenvolvimento.

Exemplo no Windows com o prompt comando:

```cmd
python -m venv .venv
.venv\Scripts\Activate
python -m pip install --upgrade pip
pip install Django python-decouple dj-database-url django-adminlte
Copy-Item .env.example .env
python manage.py migrate
python manage.py runserver
```

Depois disso, a aplicação ficará disponível em:

- `http://127.0.0.1:8000/admin/`

Se quiser acessar o admin com um usuário, crie um superusuário:

```powershell
python manage.py createsuperuser
```

Durante a criação, o Django solicitará os dados principais do usuário administrativo:

- nome de usuário
- e-mail
- senha
- confirmação da senha

Depois de criar o superusuário:

1. Certifique-se de que o servidor está em execução com `python manage.py runserver`.
2. Acesse `http://127.0.0.1:8000/admin/` no navegador.
3. Informe o nome de usuário e a senha cadastrados no comando `createsuperuser`.
4. Após o login, utilize o painel administrativo para gerenciar os modelos registrados no Django Admin.

Se precisar recriar o acesso, execute o comando novamente com outro usuário ou altere a senha pelo shell administrativo do Django.

## Variáveis de ambiente

O projeto usa `python-decouple` para ler configurações do arquivo `.env`.

Conteúdo atual de referência em `.env.example`:

```env
ENV_SECRET_KEY=cole_aqui_uma_secret_key_do_django
ENV_DEBUG=True
ENV_ALLOWED_HOSTS=127.0.0.1,localhost
ENV_DATABASE_URL=sqlite:///db.sqlite3
```

Exemplo alternativo comentado no projeto para MySQL:

```env
# ENV_DATABASE_URL=mysql://usuario:senha@localhost:3306/twjobs
```

## Configurações aplicadas em `setup/settings.py`

Resumo do que já está configurado no projeto:

- `BASE_DIR` é definido com `pathlib.Path`.
- `SECRET_KEY` é lida da variável `ENV_SECRET_KEY`.
- `DEBUG` é lido da variável `ENV_DEBUG`, com `False` como valor padrão.
- `ALLOWED_HOSTS` é lido de `ENV_ALLOWED_HOSTS` usando lista separada por vírgulas.
- O app local `app` está registrado em `INSTALLED_APPS`.
- O pacote `django_adminlte` também está registrado em `INSTALLED_APPS`.
- O banco de dados é configurado pela variável `ENV_DATABASE_URL`.
- Se `ENV_DATABASE_URL` não for informada, o projeto usa SQLite local em `db.sqlite3`.
- O idioma da aplicação está configurado como `pt-br`.
- O fuso horário está configurado como `UTC`.
- `USE_I18N` está habilitado.
- `USE_TZ` está habilitado.
- Os arquivos estáticos usam `STATIC_URL = 'static/'`.
- O tipo padrão de chave primária é `BigAutoField`.

## Estrutura atual do projeto

```text
petshop-admin/
|-- app/
|-- setup/
|-- .env.example
|-- .gitignore
|-- db.sqlite3
|-- manage.py
```

## Observações

- Ainda não existe um arquivo de dependências versionado, como `requirements.txt`.
- A rota configurada atualmente é apenas a área administrativa em `/admin/`.
- O banco SQLite `db.sqlite3` já existe no projeto, mas as migrações continuam sendo necessárias ao preparar um novo ambiente.