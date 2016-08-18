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
**Observação**: O projeto foi feito usando python 2.7 e mysql

1. Instalar o ActivePython (http://www.activestate.com/activepython/downloads)
2. Criar o env com o virtualenv para o projeto
3. Fazer o checkout do projeto
4. Criar o banco algpedia
	4.1. Na pasta AlgPedia/database tem um dump, rode o .sql no seu workbench ou heidi...
5. Instalar as dependências através de PIP e PYPM (para windows)
	5.1 $source env/bin/activate
	5.2 $pip install -r requirements/requirements.txt
		5.2.1 Algumas dependências binárias podem falhar usando o pip pelo requirements, existe a alternativa de baixar o whl por este site http://www.lfd.uci.edu/~gohlke/pythonlibs/ e instalar usando $pip install <nome_do_arquivo.whl>
	5.3 Para sair do ambiente virtual do Python, rode  $ deactivate
6.Rodar python manage.py runserver para inicializar o serviço em localhost:8000 por padrão.

**Nosso trello**: https://trello.com/b/P8TgPwjK/algpedia
