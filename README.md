# Sistema de Pedidos com API REST

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de Python, consumo de APIs REST e operações CRUD.

A aplicação utiliza a MockAPI como banco de dados remoto, permitindo cadastrar, consultar, atualizar e excluir pedidos através de requisições HTTP.

Além disso, o sistema possui uma interface interativa no terminal utilizando a biblioteca Rich para melhorar a experiência do usuário.

---

## Funcionalidades

### Pedidos

* Adicionar novo pedido
* Listar todos os pedidos
* Buscar pedido por ID
* Buscar pedidos por cliente
* Buscar pedidos por status
* Atualizar informações de um pedido
* Remover pedido

### Integração com API

* Método GET
* Método POST
* Método PATCH
* Método DELETE

### Tratamento de Erros

* Validação de entradas do usuário
* Tratamento de erros de conversão
* Tratamento de respostas HTTP
* Verificação de registros inexistentes (404)

---

## Tecnologias Utilizadas

* Python 3
* Requests
* Rich
* MockAPI

---

## Estrutura do Projeto

```bash
SistemaPedidos/
│
├── main.py
├── consultas.py
├── interface.py
└── README.md
```

### Arquivos

**main.py**

* Responsável pelo fluxo principal do sistema.

**consultas.py**

* Contém todas as operações de comunicação com a API.

**interface.py**

* Responsável pelos menus e interação com o usuário.

---

## Exemplo de Menu

```text
1 - Adicionar Produto
2 - Lista de Pedidos
3 - Buscar Pedidos
4 - Atualizar Pedido
5 - Remover Pedido
6 - Sair
```

### Submenu de Busca

```text
1 - Buscar por ID
2 - Buscar por Cliente
3 - Buscar por Status
4 - Voltar
```

---

## Objetivos de Aprendizado

Durante o desenvolvimento deste projeto foram praticados:

* Estruturas condicionais
* Estruturas de repetição
* Funções
* Modularização
* Manipulação de JSON
* Consumo de APIs REST
* CRUD completo
* Tratamento de erros
* Organização de projetos Python

---

## Melhorias Futuras

* Relatórios de vendas
* Dashboard de pedidos
* Estatísticas por cliente
* Produto mais vendido
* Tratamento de exceções de conexão
* Migração para FastAPI
* Integração com banco de dados SQLite

---

## Autor

Desenvolvido por Matheus Caires como projeto de estudos em Python e APIs REST.

