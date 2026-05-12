# 📝 DIO Blog API

API RESTful para gerenciamento de posts de um blog, desenvolvida com **FastAPI** e **Python** como projeto prático do bootcamp da [DIO (Digital Innovation One)](https://www.dio.me/).

---

## 🚀 Tecnologias

- [Python 3.12](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) — framework web moderno e de alta performance
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM para mapeamento do banco de dados
- [databases](https://www.encode.io/databases/) — suporte a queries assíncronas
- [SQLite](https://www.sqlite.org/) — banco de dados local
- [Poetry](https://python-poetry.org/) — gerenciamento de dependências

---

## 📁 Estrutura do Projeto

```
dio-blog/
├── main.py              # Ponto de entrada da aplicação
├── src/
│   ├── controllers/
│   │   └── post.py      # Rotas e lógica dos endpoints
│   ├── models/
│   │   └── post.py      # Modelo da tabela no banco de dados
│   ├── schemas/
│   │   └── post.py      # Schemas Pydantic para validação
|   ├── views/
|   |   └── post.py
│   └── db.py            # Configuração do banco de dados
├── blog.db              # Banco de dados SQLite
├── pyproject.toml       # Dependências e configurações do projeto
└── poetry.lock
```

---

## ⚙️ Como executar

### Pré-requisitos

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation) instalado

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Thur7798/dio-blog.git
cd dio-blog

# Instale as dependências
poetry install
```

### Executando a API

```bash
PYTHONPATH=. poetry run uvicorn main:app --reload
```

A API estará disponível em: `http://127.0.0.1:8000`

---

## 📖 Documentação

O FastAPI gera documentação interativa automaticamente:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

---

## 🔗 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/posts` | Lista todos os posts |
| `GET` | `/posts/{id}` | Retorna um post pelo ID |
| `POST` | `/posts` | Cria um novo post |
| `PUT` | `/posts/{id}` | Atualiza um post existente |
| `DELETE` | `/posts/{id}` | Remove um post |

---

## 📚 Sobre o Projeto

Este projeto foi desenvolvido durante o bootcamp de **Back-End com Python** da DIO, com foco em:

- Construção de APIs REST com FastAPI
- Organização de projetos em camadas (controllers, models, schemas, views)
- Integração com banco de dados usando SQLAlchemy e queries assíncronas
- Gerenciamento de dependências com Poetry

---

## 👤 Autor

Feito por [Thur7798](https://github.com/Thur7798)
