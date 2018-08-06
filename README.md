AlgPedia
========

Algpedia é um um projeto open source.
Uma enciclopédia livre sobre algoritmos e implementações desenvolvida como projeto final de alunos da UFRJ (Thais Viana e Pablo Abdelhay) 

## Funcionalidades implementadas:

1. Wiki
2. Sistema de recomendação por reputação e confiança
3. Extração de dados (web crawler)
4. Tradução de base relacional para base semântica
5. Buscas
5. Sistema de tageamento

## Instruções:

**INSTALAÇÃO WINDOWS**

1. Download python 3.6, postgres, PG admin, gitHub, pip install
2. Clonar projeto no cmd 
	>> git clone https://github.com/thaisviana/AlgPedia.git
3. No cmd para instalar tudo o que é necessário: 
Dentro do diretório onde foi clonado o git, crie um ambiente virtual 
	>> python -m venv env
Entre na pasta do projeto (ex: C:\Users\Name\Documents\GitHub\AlgPedia\env)
Ativar o ambiente virtual 
	>> C:\Users\Name\Documents\GitHub\AlgPedia> env\Scripts\activate
Instale tudo que for necessário
	>> pip install -r requirements.txt
Confira o que está instalado e se tudo foi instalado corretamente
	>> pip freeze
4. Criar o banco de dados no PG admin (Add New Server)
5. Guardar informações: nome do banco, senha do banco, nome de usuário e senha de usuário. Escreva essas informações em settings.py na sua máquina.
6. Abra o prompt de comando. Entre na pasta da AlgPedia e ative o ambiente virtual.
7. Rode as migrações ($python manage.py migrate). O seu banco passará a ter as informações da algpedia
8. Crie um superusuário ($python manage.py createsuperuser)
9. Rode o servidor localmente($python manage.py runserver) e acesse no navegador: http://127.0.0.1:8000/

**INSTALAÇÃO LINUX (para distribuições debian-like)**

- verifique que está usando python 3 mais recente
- crie uma virtualenv, indico usar o nome passado no comando a seguir:
    $ pip install virtualenv
    $ virtualenv venv
- instale o mariadb (mysql para linux) e o MySQL-python usando o package manager na sua distribuição linux em distribuições debian-like seria:
    $ apt-get install mariadb-server mariadb-client
    $ apt-get install libmysqlclient-dev python-dev
- Clonar projeto https://github.com/thaisviana/AlgPedia.git no GitHub Desktop
- cd na pasta do projeto
- source env-linux/bin/activate
- voltar para /home/baldus/cmartins/AlgPedia
- instalar pacotes que estao no arquivo requirements-linux.txt usando o pip (pip install -r requirements-linux.txt)
    se a instalação falhar ao tentar instalar o pillow certifique-se da instalação do libjpeg. Em distribuições debian-like basta rodar: 
        $ apt-get install libjpeg62-turbo-dev
- pip freeze (só pra conferir o que está instalado)
- Para criar o banco de dados abra o arquivo local.py localizado em settings
- ache a definição dos DATABASES, ali estão as credenciais que serão usadas para conectar no banco
- com essas credenciais crie o usuario no mysql e de permissao 
    $ mysql -u root -p
    > grant all privileges on *.* to <usuario>@localhost identified by '<senha>' with grant option;
- crie o banco de dados
    > create database AlgPedia;
- na pasta root do projeto migre o banco
    $ python manage.py syncdb
    Não se preocupe se ele reclamar que nao migrou o algorithm, faremos isso a seguir
    $ python manage.py migrate
- Depois dessas etapas podemos iniciar o servidor
    $ python manage.py runserver
    acesse no navegador: http://127.0.0.1:8000/


**Nosso trello**: https://trello.com/b/P8TgPwjK/algpedia
