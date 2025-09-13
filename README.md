# Desafio para processo seletivo - Workshop Backend Fábrica de Software 2025.2

Este projeto foi desenvolvido para o desafio final do Workshop da Fábrica de Software 2025.2.

## Tecnologias utilizadas

### Back-end:

- **Python 3**: Linguagem de programação base para lógica da aplicação.
- **Django MVT**: 'Framework web Python' para desenvolvimento do projeto, consumindo 'APIs', criando operações 'CRUD' e renderizando 'templates'.
- **Requests**: Biblioteca para requisição da 'API' externa pública para o projeto.
- **JSONPlaceholder**: 'API' externa pública para consumo de dados.

### Front-end:

- **HTML5**: Linguagem de marcação para construção dos 'templates'.

## Funcionalidades:

- **Criação de postagem**: Cria uma postagem e armazena no banco de dados.
- **Listagem de postagens**: Lista e visualiza as postagens armazenada no banco de dados.
- **Atualização de postagem**: Atualiza as postagens armazenadas no banco de dados.
- **Exclusão de postagem**: Delete as postagens armazenadas no banco de dados.
- **Sincronização de banco de dados**: Alimenta o banco de dados com as postagens já presentes na 'API' externa pública.

## Como rodar o projeto:

### 1. Clonando o repositório

Use o seguinte comando para clonar:

```
bash
git clone https://github.com/soturnacrosta/wsBackend-Fabrica25.2
cd ProjetoFInal/projetocrud
```

### 2. Configurando o projeto

1. **Crie e Ative um Ambiente Virtual (Recomendado)**

Vá na pasta raiz:

```
bash
python -m venv venv
`source venv/bin/activate`

No Windows, use `venv\Scripts\activate`
```

2. **Instale as Dependências**

```bash
pip install django requests
```

3. **Execute as Migrações**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Inicie o Servidor de Desenvolvimento**

```bash
python manage.py runserver
```

### 3. Testando a aplicação

1. **Abra seu navegador e acesse `http://127.0.0.1:8000/`.** 
2. **Clique em 'Sincronizar dados da 'API' para importar as postagens e usuários presentes na 'API' externa pública.**
3. **Utilize as funcionalidades de criar, listar, atualizar e deletar postagem.**

### Observação Importante: Sincronização Inicial de Dados

Após rodar o servidor, acesse `http://127.0.0.1:8000/sincronizar/` no seu navegador para popular o banco de dados com as postagens e usuários da 'API'. Sem este passo, o banco de dados estará vazio e a funcionalidade de listagem e edição não irá funcionar.

## Fontes

- https://jsonplaceholder.typicode.com/
- https://joaolucasgpc.notion.site/Class-Based-View-1a799b0a3ac58046aef1d89b8fd6846e
