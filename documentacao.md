# Dados autorais:

Processo seletivo Fábrica de Software 2025.2.

Projetos do WorkShop Back-End.

Autor do repositório: Mailton Olinto de Oliveira Lemos.

# Requisitos:

* Criar conexão com API externa pública.
* A conexão consome a API pública JSONPlaceholder.
* Um modelo em template para consumir os dados da API para exibir os dados em browser.
* Relação entre as entidades 'user' e 'post'.
* Estrutura em HTML simples e amigável.
* Operações CRUD: criar, listar, atualizar e deletar do banco de dados da aplicação.
* Arquivos .gitignore, requirements e readme devem estar presentes. 
* A pasta venv não pode ser rastreada pelo Git
* Todo o projeto deve ser enviado para o Github

# Objetivo:

Criar uma aplicação, consumindo uma API externa pública através de tecnologia Python com framework Django, em ambiente VSCODE. A JSONPlaceholder
nos permite simular um blog, que poderemos criar conteúdo, modelar as relações das entidades e consumí-las através de templates.

# Desenvolvimento:

Esse projeto utiliza a linguagem de programação Python e o framework Django, também a biblioteca Requests. A IDE é Visual Studio Code (VSCODE), sendo ambiente LINUX. A documentação é feita em Editor de Texto Linux e formatação MarkDown.

# Definição de pronto:

Uma demanda estará pronto quando sanar todas as necessidades propostas pelos desafiantes e enviado ao repositório remoto do projeto.

# Funcionalidades e códigos:

## Banco de dados (models)

O `models.py` recebe duas classes: `Users` e `Post`. Essas duas classes são a base de dados a serem alimentadas pela API externa pública da aplicação. Nelas temos os campos:

Na classe `Users` estamos puxando os dados dos usuários:

`api_id` que recebe a id da API.

`name`que recebe os dados de name da API.

`username` que recebe os dados de username da API.

`email` que recebe os dados de email da API.


Na classe `Post` estamos puxando os dados dos posts:


`api_id` que recebe a id da API.

`title`que recebe os dados de title da API.

`body` que recebe os dados de body da API.

`user` que cria um relacionamento com `Users` do models.


Em ambas as classes, as variáveis recebem parâmetros delimitadores de dados, como máximo de caracteres, se são valores únicos ou se podem ser nulos.

## Views (lógica de páginas)

Nas views, temos classes para exibição das páginas:

### 1. A classe `HomeView`: 

Retorna o template da página `home.html`.

### 2. A classe `SincronizarView` importa os dados pro banco de dados:

Ela faz uma requisição para a JSONPlaceholder API através do `GET`, sincroniza os dados com o `get_or_create` para cada usuário que não exista, faz mais uma requisição `GET` para buscar os posts da API, relacionando os `Users` e os `Post` com `api_id`. Em seguida usa o `get_or_create` para cada post não existente.

Após esse processo, redireciona para a página do nome da URL.

### 3. A classe `PostListView` lista as postagens do banco de dados:

`model` é associada ao model `Post` e o template é associado ao `listar_posts.html`.

### 4. A classe `PostCreateView` cria as postagens do banco de dados:

`model` é associada ao model `Post` e o template é associado ao `criar_post.html`. Ele tem uma URL de sucesso `listar_posts.html` que o redireciona caso seja submetido com sucesso..

O campo `fields` recebe `title` e `body`. A classe usa esses campos para construir um formulário automaticamente.

Se for válido, ele retorna com sucesso com `form_valid()`.

### 5. A classe 'PostUpdateView' atualiza as postagens do banco de dados:


`model` é associada ao model `Post` e o template é associado ao `atualizar_posts.html`. Ele tem uma URL de sucesso `listar_posts.html` que o redireciona caso seja submetido com sucesso..

O campo `fields` recebe `title` e `body`. A classe usa esses campos para construir um formulário automaticamente.

### 6. A classe `PostDeleteView` deleta as postagens do banco de dados:

`model` é associada ao model `Post` e o template é associado ao `deletar_posts.html`. Ele tem uma URL de sucesso `listar_posts.html` que o redireciona caso seja submetido com sucesso..

## URLS (rotas)

Nas urls, devemos colocar quais caminhos nossa aplicação deve seguir para alcançar as páginas das views.

Nelas temos:

- ` ` vazio é o caminho da HomeView para ser renderizado na url.
- `sincronizar/` é o caminho da view SincronizarView para ser renderizado na url.
- `listar/` é o caminho da view PostListView para ser renderizado na url.
- `criar/` é o caminho da view PostCreateView para ser renderizado na url.
- `atualizar/` é o caminho da view PostUpdateView para ser renderizado na url.
- `deletar/` é o caminho da view PostDeleteView para ser renderizado na url.

Ao alcançar as views, serão renderizadas as `template_name` associadas nas views de cada classe. 

## Templates ("Front-end")

Em templates, colocamos as estruturas Front-End de nossas páginas em HTML5 e CSS.


Temos basicamente cinco (5) páginas HTML5 no diretório templates:

- `atualizar_posts.html`
- `criar_posts.html`
- `deletar_posts.html`
- `home.html`
- `listar_posts.html`

Os botões que funcionam como movimentações entre as páginas devem ser alimentadas pelas variáveis das URLs da aplicação. 

As varáveis das URLs são aquelas contidas em name = `valor`.

# Futuras melhorias:

* Adicionar validações de formulário.
* Estilizar as páginas em CSS para criar uma interface-usuário mais amigável.
* Criar um sistema de autenticação.
* Validações na view, formulário e models.
