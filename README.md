# Meu blog — Templates Django

Atividade do módulo 53 do curso Full Stack Python da EBAC.

Criei o template `base.html` com cabeçalho, navegação e rodapé. A página inicial e a página de cada postagem utilizam essa estrutura por meio da herança de templates. O CSS fica separado nos arquivos estáticos da aplicação.

O blog permite cadastrar, editar e excluir postagens pelo painel administrativo do Django. As postagens publicadas aparecem na página inicial com título, autor, data e resumo. Cada publicação tem uma página com o conteúdo completo. Postagens desmarcadas como publicadas ficam disponíveis somente no painel.

## Executar no Windows (PowerShell)

Com Python 3.10 ou mais recente instalado, abra a pasta que contém `manage.py` e execute:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

- Site: http://127.0.0.1:8000/
- Administração: http://127.0.0.1:8000/admin/

Entre no painel com o superusuário criado. Em **Blog → Postagens → Adicionar**, preencha o título e o conteúdo, mantenha **Publicado** marcado e salve. O autor é preenchido automaticamente com o usuário que cadastrou a postagem. Abra a página inicial para conferir a publicação.

O banco SQLite é criado localmente ao executar as migrações. Usuários e senhas não são incluídos no repositório.

## Verificações

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
```

## Arquivos principais

- `blog/models.py`: modelo das postagens.
- `blog/admin.py`: cadastro administrativo.
- `blog/migrations/0001_initial.py`: estrutura do banco para postagens.
- `blog/views.py`: consulta e exibição das publicações.
- `blog/templates/blog/base.html`: estrutura compartilhada.
- `blog/templates/blog/index.html`: página inicial e lista de postagens.
- `blog/templates/blog/detalhe.html`: conteúdo completo da postagem.
- `blog/static/blog/css/style.css`: estilos.
- `blog/tests.py`: testes de cadastro, edição, exclusão e exibição.

As alterações da atividade são mantidas na branch `templates`.

## Autor

Bruno Costa Macedo de Almeida
