# Meu blog — Templates Django

Atividade do módulo 53 do curso Full Stack Python da EBAC.

Criei o template base.html com cabeçalho, navegação e rodapé. A página
index.html utiliza essa estrutura por meio da herança de templates.
O CSS fica separado na pasta de arquivos estáticos da aplicação.

## Executar no Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Abra http://127.0.0.1:8000/.

## Arquivos principais

- blog/templates/blog/base.html: estrutura compartilhada.
- blog/templates/blog/index.html: conteúdo da página inicial.
- blog/views.py: renderização da página.
- blog/urls.py: endereço da página inicial.
- blog/static/blog/css/style.css: estilos.

O projeto é independente dos módulos anteriores e usa a branch templates
para as alterações desta atividade.
