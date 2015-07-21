---
Como executar?
---
1. Criar e ativar um [ambiente virtual](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
    * `mkvirtualenv sfd` para criar um virtualenv chamado sfd
    * `workon sfd` para ativar o virtualenv sempre que for trabalhar no projeto

2. Instalar as dependências
    * `pip install -r requirements.txt`

3. Criar um arquivo chamado `settings.ini` na pasta sfd com o seguinte conteúdo:
```
[settings]

DATABASE_URL = mysql://user:password@host:port/db_name
DEBUG = True
SECRET_KEY = a-really-random-secret-key

USE_S3 = True
; Caso queira usar a amazon s3 pra gerenciar arquivos estáticos e de media
; Se o USE_S3 for False, não precisa dos dados abaixo
S3_ACCESS_KEY = s3-access-key
S3_SECRET_KEY = s3-secret-key
S3_BUCKET_NAME = s3-bucket-name
```

4. Depois de criado o banco de dados (manualmente), crie as tabelas
    * `python manage.py migrate`

5. Iniciar o servidor web
    * `python manage.py runserver`
