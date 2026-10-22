# Gerenciador de Chamados Internos — Django

Projeto original ampliado com CRUD, login, filtros, controle de acesso e testes. A pasta `controle_tarefas/` contém a versão anterior em Python, mantida para comparação.

## Executar no Windows (PowerShell)

Abra esta pasta (a mesma que contém `manage.py`) no VS Code e execute:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Abra `http://127.0.0.1:8000/` e entre com o usuário cadastrado. Para cadastrar outro usuário administrador, use `py manage.py createsuperuser` (com o ambiente ativado) ou `.\.venv\Scripts\python.exe manage.py createsuperuser`.

**Dados preservados:** o banco que acompanhava o projeto permanece incluído neste ZIP. A migração 0003 atribui as tarefas antigas ao único superusuário encontrado (usuário `admin` no banco fornecido). Se seu banco tiver mais de um administrador, defina `$env:TAREFAS_USUARIO_LEGADO='admin'` antes de `migrate`. O banco vai continuar local, mas está no `.gitignore` para não publicar dados e senhas no GitHub.

## Funcionalidades

- Autenticação com login/logout Django e proteção de telas.
- Tarefas separadas por usuário.
- Cadastro, listagem, edição, conclusão e exclusão (com confirmação).
- Filtros por situação e categoria, mensagens de sucesso e validação de formulário.
- Cadastro de categorias pelo admin: `http://127.0.0.1:8000/admin/`.
- CSRF nos formulários e ações POST.

## Verificações

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
.\.venv\Scripts\python.exe manage.py makemigrations --check --dry-run
```

As telas e regras são para estudo/local, **não** uma implantação pronta para produção (`DEBUG=True` e chave de desenvolvimento).

## Entrega

Envie o código, migrações, `requirements.txt`, `.gitignore`, README, testes e capturas de tela. Não envie `.venv`, banco `db.sqlite3` nem dados de usuários para o GitHub. O ZIP entregue aqui inclui o banco apenas para permitir continuar o projeto original sem perder os dois registros.
