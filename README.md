# 📋 FORMULÁRIO DE DEVOLUÇÃO
<BR>

## 🎯 OBJETIVO DO PROJETO

Este projeto consiste em um formulário de devolução simples que fiz para empresa onde trabalho que permite a inserção de dados que serão armazenados automaticamente em um banco de dados.
<br>
<br>

## 📍 `ÍNDICE`
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Utilizar](#como-utilizar)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
<br>

## 💻 Funcionalidades 
- `Identificação do Cliente`: Campos para inserção de informações como nome, e-mail, e número do pedido.
<br>
<br>


- `Turno`: Campo para selecionar o turno relacionado à devolução (por exemplo, manhã, tarde, noite).
<br>
<br>


- `Conferente`: Campo para inserir o nome da pessoa responsável pela conferência da devolução.
<br>
<br>


- `Cliente`: Campo para inserir o nome do cliente que está realizando a devolução.
<br>
<br>

- `Transportadora`: Campo para inserir o nome da transportadora responsável pela entrega.
<br>
<br>

- `Número da Nota`: Campo para inserir o número da nota fiscal relacionado à devolução.
<br>
<br>

- `Quantidade de Caixas na Nota`: Campo para inserir a quantidade de caixas mencionadas na nota fiscal.
<br>
<br>

- `Quantidade de Caixas Recebidas`: Campo para inserir a quantidade de caixas que foram efetivamente recebidas.
<br>
<br>

- `Motivo da Devolução`: Campo para selecionar o motivo da devolução (por exemplo, avaria, produto errado).
<br>
<br>

- `Setor que causou a devolução`: Campo para selecionar o setor responsável pela causa da devolução (por exemplo, logística, expedição).
<br>
<br>

- `Valor da Devolução`: Campo para inserir o valor monetário da devolução.
<br>
<br>

- `Botão`: Botão que confirma todos os inputs e salva no banco de dados.
<br>
<br>

## 👩‍💻 Tecnologias Utilizadas
<img 
    align = "left"
    alt="css"
    title = "Python"
    width="30px"
    style="padding-right: 10px;"
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
<img 
    align = "left"
    alt="css"
    title = "Django"
    width="30px"
    style="padding-right: 10px;"
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg" />
 <img 
    align = "left"
    alt="css"
    title = "Html"
    width="30px"
    style="padding-right: 10px;"
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg" />
<img
    align = "left"
    alt="css"
    title = "CSS"
    width="30px"
    style="padding-right: 10px;"
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" />
 <img  
    align = "left"
    alt="css"
    title = "MySQL"
    width="30px"
    style="padding-right: 10px;"
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg" />
<br>
<br>
<br>

## 🔨 Instalação 
- Primerio deve criar o ambiente virtual com o comando **python venv -m nome_do_ambiente**.
<br>
<br>

- Após criar o ambiente virtual, para ativá-lo use o comando **./nome_do_ambiente/scripts/activate.ps1**.
<br>
<br>

- Já no ambiente virtual, utilize o comando **pip install django**.
<br>
<br>

- Instale a biblioteca bootstrap5 usando comando **pip install django-bootstrap5**.
<br>
<br>

- Instale a biblioteca mysqlclient usando o comando **pip install mysqlclient**.
<br>
<br>

- Instale a biblioteca PyMySQL usando o comando **pip install PyMySQL**.
<br>
<br>

- Instale caso não tenha o MySQL, instale ele também. Está disponivel no próprio site [Mysql](#https://dev.mysql.com/downloads/installer/)
<br>
<br>

- Baixe o MySQL Workbench e o MySQL command-line client
<br>
<br>

- Terá que colocar uma senha para acessar o MySQL com and-line client. Coloque uma senha que lembre para ficar mais fácil o acesso. 

## 🖱️ Como Utilizar
- Primeiro deve ter já criado um banco de dados, para use o comando CREATE DATABASE **nome_do_seu_banco** CHARACTER SET = utf8mb4 COLLATE utf8mb4_unicode_ci no command-line;
<br>
<br>

- Agora temos que ter um usuário e senha no seu banco de dados, para conseguir entrar no Workbench, para fazer isso use o comando CREATE USER '**seu_usuario**'@'localhost' IDENTIFIED WITH mysql_native_password BY '**sua_senha**';
<br>
<br>

- Agora é a parte final, onde damos os privilégio para poder manipular o banco de dados, use o comando GRANT ALL PRIVILEGES ON **nome_do_seu_banco**.* TO '**seu_usuario**'@'localhost' WITH GRANT OPTION;
<br>
<br>

Agora vá no vscode, no arquivo settings.py e na estrutura de banco de dados vai estar já padronizado para o sqlite3.

- Para criar um usuário para o painel administrador, utilize o comando **django manage.py createsuperuser**
<br>
<br>


- Utilize o comando **django manage.py makemigrations** para migrar o models do projeto para o banco de dados.
<br>
<br>

- Após isso, use o comando **django manage.py migrate** para a tabela no banco de dados criada.
<br>
<br>

- Se estiver tudo funcionando, é só abrir o banco de dados para ver se a tabela irá ser criada.



        
          
          
