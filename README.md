# API de Produtos

Esta é uma API REST simples para gerenciamento de produtos, construída com **Flask** e **SQLite**.

### Funcionalidades

- **Listar Produtos:** Obtenha todos os produtos cadastrados;
- **Buscar Produto por ID:** Encontre um produto específico usando seu ID.
- **Adicionar Produto:** Crie um novo produto no banco de dados.
- **Atualizar Produto:** Modifique as informações de um produto existente.
- **Deletar Produto:** Remova um produto do banco de dados.

### Tecnologias Utilizadas

- **Python:** Linguagem de programação;
- **Flask:** Framework web para Python.
- **SQLite3:** Banco de dados relacional leve.

---

## **Como Executar o Projeto**
Se você deseja utilizar esta API na sua máquina, siga os passos:
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SamuelOlDourado/api-gerenciar-produtos.git
   cd api-gerenciar-produtos
   ```
2. **Instale as dependências:**
   ```bash
   pip install flask
   ```
3. **Crie o banco de dados SQLite (caso não exista):**
    ```sql
    CREATE TABLE Produtos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL,
      descricao TEXT,
      preco REAL,
      estoque INTEGER,
      categoria TEXT
   );
   ```
4. **Inicie a aplicação:**
   ```bash
   python app.py
   ```
   
A API estará disponível em:  `http://127.0.0.1:5000/`

---
## Testando com Postman

Você pode testar os endpoints desta API utilizando o Postman:

1. Abra o Postman.
2. Crie uma nova requisição e informe a URL (por exemplo, `http://127.0.0.1:5000/todos_produtos`).
3. Escolha o método HTTP correto (GET, POST, PUT, DELETE).
4. Para POST ou PUT, selecione Body > Raw > JSON e insira os dados (exemplo de JSON):
```json
{
    "nome": "NotebookA",
    "descricao": "Notebook para trabalho e jogos",
    "preco": 3500.0,
    "estoque": 30,
    "categoria": "Eletrônicos"
}
```
---
## Endpoints da API

Aqui estão os endpoints disponíveis e como usá-los:

### 1. Home
- **URL:** `/`
- **Método:** GET
- **Descrição:** Retorna uma mensagem de boas-vindas.
- **Resposta de Exemplo:** API de Produtos

### 2. Listar Todos os Produtos
- **URL:** `/todos_produtos`
- **Método**: GET
- **Descrição:** Retorna uma lista de todos os produtos cadastrados.
- **Resposta de Exemplo:**
```json
[
    {
        "id": 1,
        "nome": "produto1",
        "descricao": "descricao1",
        "preco": 1500.0,
        "estoque": 50,
        "categoria": "categoria1"
    },
    {
        "id": 2,
        "nome": "produto12",
        "descricao": "descricao2",
        "preco": 250.0,
        "estoque": 120,
        "categoria": "categoria1"
    }
]
```

### 3. Adicionar Novo Produto
- **URL:** `/adicionar_produto`
- **Método:** POST
- **Descrição:** Adiciona um novo produto ao banco de dados.
- **Corpo da Requisição (JSON):**
```json
{
    "nome": "NotebookA",
    "descricao": "Notebook para trabalho e jogos",
    "preco": 3500.0,
    "estoque": 30,
    "categoria": "Eletrônicos"
}
```
- **Resposta de Sucesso:**  `{"mensagem": "produto adicionado com sucesso!"}`
- **Resposta de Erro (400 Bad Request):**  `{"erro": "Dados inválidos ou incompletos"}`

### 4. Buscar Produto por ID
- **URL:** `/produto/<id>` (substitua `<id>` pelo ID do produto)
- **Método:** GET
- **Descrição:** Retorna os detalhes de um produto específico.
- **Resposta de Exemplo (para ID 1):**
```json
{
    "id": 1,
    "nome": "produto1",
    "descricao": "descricao1",
    "preco": 1500.0,
    "estoque": 50,
    "categoria": "categoria1"
}
```
- **Resposta de Erro (404 Not Found):**  `{"erro": "Produto não encontrado"}`

### 5. Deletar Produto
- **URL:** `/deletar_produto/<id>` (substitua `<id>` pelo ID do produto)
- **Método:** DELETE
- **Descrição:** Deleta um produto do banco de dados.
- **Resposta de Sucesso:**  `{"mensagem": "Produto deletado com sucesso!"}`
- **Resposta de Erro (404 Not Found):**  `{"erro": "Produto não encontrado"}`

### 6. Atualizar Produto
- **URL:** `/atualizar_produto/<id>` (substitua `<id>` pelo ID do produto)
- **Método:** PUT
- **Descrição:** Atualiza as informações de um produto existente.
- **Corpo da Requisição (JSON):**
```json
{
    "nome": "NotebookAtualizado",
    "descricao": "Notebook para trabalho e jogos",
    "preco": 3500.0,
    "estoque": 30,
    "categoria": "Eletrônicos"
}
```
- **Resposta de Sucesso:**  `{"mensagem": "Produto atualizado com sucesso!"}`
- **Resposta de Erro (404 Not Found):**  `{"erro": "produto não encontrado"}`
- **Resposta de Erro (400 Bad Request):** `{"erro": "Dados inválidos ou incompletos"}`
