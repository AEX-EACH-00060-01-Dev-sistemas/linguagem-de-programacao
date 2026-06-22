# 🛠️ Aula 02 — `venv` na Prática

> **Objetivo:** Criar, ativar, usar e desativar um ambiente virtual com `venv`, a ferramenta que já vem embutida no Python.

---

## O que é o `venv`?

O `venv` é um módulo que acompanha o Python a partir da versão **3.3**. Você não precisa instalar nada — ele já está lá, esperando para ser usado.

Ele cria uma pasta dentro do seu projeto com uma cópia isolada do Python e do `pip`, pronta para receber as bibliotecas daquele projeto específico.

---

## Passo a Passo Completo

### Passo 1 — Abra o terminal na pasta do projeto

No VS Code, use o menu **Terminal → Novo Terminal**.
No Windows, você pode também buscar por **PowerShell** ou **CMD** no menu Iniciar e navegar até a pasta com `cd`.

```bash
# Navegando até a pasta do projeto (exemplo)
cd C:\MeusProjetos\projeto-a
```

---

### Passo 2 — Crie o ambiente virtual

```bash
python -m venv venv
```

O que acontece aqui:
- `python -m venv` → chama o módulo venv
- o segundo `venv` → é o **nome da pasta** que será criada (convenção da indústria, mas você pode usar outro nome)

Uma pasta chamada `venv/` aparecerá no seu projeto com esta estrutura:

```
projeto-a/
└── venv/
    ├── Scripts/      ← no Windows
    │   ├── python.exe
    │   ├── pip.exe
    │   └── activate
    ├── bin/          ← no Linux/macOS
    │   ├── python
    │   ├── pip
    │   └── activate
    └── Lib/
        └── site-packages/   ← onde suas bibliotecas serão instaladas
```

> ⚠️ **Nunca edite os arquivos dentro da pasta `venv/` manualmente.** Ela é gerenciada automaticamente.

---

### Passo 3 — Ative o ambiente virtual

Ativar o ambiente faz o terminal "apontar" para o Python e o pip isolados, e não mais para os do sistema.

**Windows — PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

**Windows — Prompt de Comando (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

Após ativar, o nome do ambiente aparece entre parênteses no início do terminal — esse é o sinal de que está funcionando:

```
(venv) C:\MeusProjetos\projeto-a>
```

> 💡 **Dica:** Se o PowerShell bloquear o script com erro de permissão, execute:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> e tente ativar novamente.

---

### Passo 4 — Verifique qual Python está sendo usado

Confirme que o terminal está usando o Python do ambiente virtual, e não o global:

**Windows:**
```powershell
where python
```

**Linux / macOS:**
```bash
which python
```

O caminho retornado deve apontar para dentro da pasta `venv/` do seu projeto. Se apontar para outro lugar, o ambiente não está ativo.

---

### Passo 5 — Instale as bibliotecas necessárias

Com o ambiente ativo, qualquer instalação fica restrita a ele:

```bash
pip install pandas
pip install numpy matplotlib
```

Para instalar uma versão específica:
```bash
pip install pandas==2.1.0
```

Para verificar o que está instalado no ambiente:
```bash
pip list
```

---

### Passo 6 — Salve as dependências com `requirements.txt`

Para que qualquer pessoa possa recriar o seu ambiente exato, gere um arquivo de dependências:

```bash
pip freeze > requirements.txt
```

O `requirements.txt` ficará assim:
```
numpy==1.26.4
matplotlib==3.8.3
pandas==2.2.1
...
```

Para instalar todas as dependências a partir desse arquivo (em outro computador ou após clonar o repositório):
```bash
pip install -r requirements.txt
```

---

### Passo 7 — Desative o ambiente quando terminar

```bash
deactivate
```

O prefixo `(venv)` desaparece do terminal — você voltou ao Python global.

---

## 📋 Resumo de Todos os Comandos

```bash
# 1. Criar o ambiente virtual
python -m venv venv

# 2. Ativar (Linux/macOS)
source venv/bin/activate

# 2. Ativar (Windows PowerShell)
venv\Scripts\Activate.ps1

# 2. Ativar (Windows CMD)
venv\Scripts\activate.bat

# 3. Verificar qual Python está ativo
which python       # Linux/macOS
where python       # Windows

# 4. Instalar biblioteca
pip install <nome-da-biblioteca>

# 5. Listar bibliotecas instaladas
pip list

# 6. Salvar dependências
pip freeze > requirements.txt

# 7. Instalar dependências salvas
pip install -r requirements.txt

# 8. Desativar
deactivate
```

---

## 🔁 Fluxo de Trabalho do Dia a Dia

Depois que o ambiente já está criado, a rotina é simples:

```
1. Abrir o terminal na pasta do projeto
2. Ativar o ambiente virtual
3. Trabalhar no projeto (instalar libs, rodar scripts, etc.)
4. Ao finalizar, desativar o ambiente
```

> 💡 O VS Code detecta automaticamente o ambiente virtual na pasta do projeto e já o ativa para você. Basta abrir a pasta no editor.

---

## ⚠️ Erros Comuns

| Erro | Causa provável | Solução |
|------|---------------|--------|
| `python` não encontrado | Python não está no PATH | Use `python3` no lugar de `python` (Linux/macOS) |
| Erro de permissão no PowerShell | Política de execução restrita | Execute `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `pip` instala globalmente mesmo com venv ativo | Ambiente não foi ativado | Verifique se `(venv)` aparece no terminal |
| Pasta `venv/` aparece no GitHub | `.gitignore` não configurado | Adicione `venv/` ao `.gitignore` (ver Aula 05) |

---

## 🧠 Pratique Agora

Siga os passos abaixo no seu computador:

1. Crie uma pasta chamada `meu-projeto-teste`
2. Abra o terminal nessa pasta
3. Crie um ambiente virtual
4. Ative o ambiente
5. Instale a biblioteca `requests`
6. Rode `pip list` e veja o resultado
7. Gere um `requirements.txt`
8. Desative o ambiente
9. Abra o arquivo `requirements.txt` gerado — o que você vê?

---

## ➡️ Próxima Aula

[Aula 03 — `pip` e Gerenciamento de Dependências →](./03.md)

Agora que você sabe criar e usar ambientes virtuais, vamos nos aprofundar no `pip` e em como gerenciar dependências de forma profissional.
