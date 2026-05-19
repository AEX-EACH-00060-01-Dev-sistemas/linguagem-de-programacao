# 🧰 Ambientes Virtuais em Python

## O que é um Ambiente Virtual?

Imagine que você tem dois projetos no mesmo computador:

- **Projeto A** precisa da versão `1.5` de uma biblioteca.
- **Projeto B** precisa da versão `2.0` da mesma biblioteca.

Se você instalar bibliotecas diretamente no Python do seu sistema, os dois projetos vão brigar pela mesma versão — e um deles vai quebrar.

Um **ambiente virtual** resolve isso criando uma **cópia isolada do Python** para cada projeto. Cada ambiente tem suas próprias bibliotecas, na versão exata que aquele projeto precisa, sem interferir nos outros.

> 💡 **Regra de ouro:** Todo projeto Python profissional usa um ambiente virtual. É o primeiro passo antes de escrever qualquer linha de código.

---

## Por que usar?

| Sem ambiente virtual | Com ambiente virtual |
|---|---|
| Bibliotecas instaladas globalmente | Bibliotecas isoladas por projeto |
| Conflitos de versão entre projetos | Cada projeto tem suas próprias versões |
| Difícil de replicar em outra máquina | Fácil de replicar com `requirements.txt` |
| Bagunça ao longo do tempo | Ambiente limpo e controlado |

---

## Como criar um Ambiente Virtual

O Python já vem com a ferramenta `venv` embutida — você não precisa instalar nada extra.

### Passo 1 — Abra o terminal na pasta do seu projeto

No VS Code, use o menu **Terminal → Novo Terminal**.

### Passo 2 — Crie o ambiente virtual

```bash
python -m venv venv
```

> Isso cria uma pasta chamada `venv/` dentro do seu projeto. Ela contém o Python e o `pip` isolados.  
> O segundo `venv` é o **nome da pasta** — por convenção usa-se `venv`, mas você pode dar outro nome.

### Passo 3 — Ative o ambiente virtual

A ativação "aponta" o terminal para usar o Python e o `pip` do ambiente isolado.

**No Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**No Windows (Prompt de Comando):**
```cmd
venv\Scripts\activate.bat
```

**No Linux / macOS:**
```bash
source venv/bin/activate
```

Após ativar, você verá o nome do ambiente entre parênteses no terminal:
```
(venv) C:\MeuProjeto>
```

### Passo 4 — Instale as bibliotecas que precisar

Com o ambiente ativo, qualquer instalação ficará restrita a ele:

```bash
pip install pandas numpy matplotlib
```

### Passo 5 — Salve as dependências do projeto

Para que outra pessoa (ou você mesmo em outro computador) possa recriar o mesmo ambiente, gere um arquivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Para instalar a partir desse arquivo depois:
```bash
pip install -r requirements.txt
```

### Passo 6 — Desative o ambiente quando terminar

```bash
deactivate
```

---

## Resumo dos comandos

```bash
# Criar
python -m venv venv

# Ativar (Linux/macOS)
source venv/bin/activate

# Ativar (Windows PowerShell)
venv\Scripts\Activate.ps1

# Instalar biblioteca
pip install <nome-da-biblioteca>

# Salvar dependências
pip freeze > requirements.txt

# Reinstalar dependências (em outra máquina)
pip install -r requirements.txt

# Desativar
deactivate
```

---

## Boas práticas

- **Nunca suba a pasta `venv/` para o Git.** Adicione `venv/` ao seu `.gitignore`.
- **Sempre suba o `requirements.txt`.** É ele que permite recriar o ambiente.
- Ative o ambiente virtual toda vez que for trabalhar no projeto.

---
