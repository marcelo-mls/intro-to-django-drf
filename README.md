# API Python com Django + DRF
> Primeiros passos com Django & Django Rest Framework

## Objetivo
Registrar o meu primeiro contato com [`Django`](https://www.djangoproject.com/) & [`Django Rest Framework (DRF)`](https://www.django-rest-framework.org/). A intenção foi criar uma `API` simples, que simula um **to-do list**. A aplicação possui duas `models` (não vinculadas) uma para Usuários e outra para Tarefas. Para desenvolver as `models` foi utilizado o `SQLite3` que já vem configurado por padrão com o framework.

Este **README** (que possui finalidade de aprendizado/tutorial) contém apenas uma descrição de tudo que foi feito (do zero) para desenvolver essa `API`.

## Como usar

- Clone o repositório
```sh
git clone git@github.com:marcelo-mls/intro-to-django-drf.git && cd intro-to-django-drf
```
- Crie o Ambiente Virtual
```sh
python3 -m venv .venv && source .venv/bin/activate
```
- Instale as Dependências
```sh
pip install -r requirements.txt
```
- Inicie o Servidor
```sh
python3 manage.py migrate
```
- Acesse as rotas da API
- [127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)
- [127.0.0.1:8000/api/users/](http://127.0.0.1:8000/api/users/)
- [127.0.0.1:8000/api/tasks/](http://127.0.0.1:8000/api/tasks/)


## Passo a passo

### 1. Ambiente virtual
1.1 - Criando o ambiente virtual
```sh
python3 -m venv .venv
```

1.2 - Ativando o ambiente virtual
```sh
source .venv/bin/activate
```

### 2. Instalações
2.1 - Django
```sh
pip install django
```

2.2 - Django Rest Framework (DRF)
```sh
pip install djangorestframework
```

2.2.1 - Dependências do DRF
```sh
pip install markdown
```
```sh
pip install django-filter
```

### 3. Criar [`requirements.txt`](https://github.com/marcelo-mls/intro-to-django-drf/blob/main/requirements.txt)
3.1 - Criando o arquivo que registra as dependências do projeto
```sh
pip freeze > requirements.txt
```

### 4. Inicialização
4.1 - Iniciando projeto na pasta [`config`](https://github.com/marcelo-mls/intro-to-django-drf/tree/main/config)
```sh
django-admin startproject config .
```

4.2 - Migrando as `models` que já vem pré-configuradas
```sh
python3 manage.py migrate
```

4.3 - Criando usuário para acessar rota `/admin` que já vem pré-configurada
```sh
python3 manage.py createsuperuser
```

4.4 - Iniciando a aplicação/modulo com o nome [`todo`](https://github.com/marcelo-mls/intro-to-django-drf/tree/main/todo)
```sh
django-admin startapp todo
```

### 5. Configurações
5.1 - Inserindo modulos no arquivo de configurações. Em: [`config/settings.py`](https://github.com/marcelo-mls/intro-to-django-drf/blob/main/config/settings.py)
```py
#  /config/settings.py

# ...
# Application definition

INSTALLED_APPS = [
# ...
    "todo",
    "rest_framework",
]
# ...
```
> Insira os valores acima na variável `INSTALLED_APPS`. o valor `todo` refere-se ao modulo/aplicação que criamos. Já o`rest_framework` indica o framework/pacote que vamos utilizar em conjunto com o Django

### 6. Desenvolvimento

6.1 - Criando as models `User` e `Task` no modulo [`/todo/models.py`](https://github.com/marcelo-mls/intro-to-django-drf/blob/main/todo/models.py)

6.1.1 - Realizando as migrações das models
```sh
python3 manage.py makemigrations
```
```sh
python3 manage.py migrate
```

6.1.2 - Inserindo dados no banco
> Esta etapa foi toda feita via terminal

- Acessando o Python
```sh
python3 manage.py shell
```
- Importando a(s) model(s)
```py
from todo.models import Task
```
- Instanciando a(s) model(s) para cria o(s) registro(s)
```py
x = Task(title="Criar README.md")
```
- Salvando o registro no banco
```py
x.save()
```

6.2 - Registrando as models criadas no modulo [`/todo/admin.py`](https://github.com/marcelo-mls/intro-to-django-drf/blob/main/todo/admin.py)

6.3 - **Criando** e configurando um modulo serializador para converter os objetos `python` para `json` (e vice-versa). Desenvolvido em: [`/todo/serializer.py`](https://github.com/marcelo-mls/intro-to-django-drf/blob/main/todo/serializer.py)

6.4 - Configurando as views em [`/todo/views.py`](https://github.com/marcelo-mls/intro-to-django-drf/blob/main/todo/views.py)

6.5 - **Criando** e configurando as rotas em: [`/todo/urls.py`](https://github.com/marcelo-mls/intro-to-django-drf/blob/main/todo/urls.py)

6.6 - Informando para o projeto principal as rotas que acabaram de ser criadas. Desenvolvido em: [`/config/urls.py`](https://github.com/marcelo-mls/intro-to-django-drf/blob/main/config/urls.py)

<br />

---

Developed by [Marcelo Marques](https://www.linkedin.com/in/marcelo-mls/), © 2023.

<div>
  <a href = "https://www.linkedin.com/in/marcelo-mls/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin" />
  </a>
  <a href="mailto:marcelo-mls@hotmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Hotmail-0077B5?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</div>
