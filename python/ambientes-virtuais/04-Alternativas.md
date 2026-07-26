# 🔀 Aula 04 — Alternativas ao `venv`

> **Objetivo:** Conhecer as principais ferramentas de gerenciamento de ambientes e dependências do ecossistema Python, entender quando cada uma se aplica e sair com uma recomendação clara.

---

## Por que existem alternativas?

O `venv` + `pip` funciona muito bem, mas tem algumas limitações:

- O `pip freeze` captura **todas** as dependências (diretas e indiretas), tornando o `requirements.txt` verboso e difícil de manter manualmente.
- Ele não gerencia a versão do Python em si — apenas as bibliotecas.
- Em projetos maiores e equipes, surgiu a necessidade de ferramentas mais robustas.

Por isso, a comunidade criou alternativas. Vamos conhecer as principais.

---

## Comparativo Geral

| Ferramenta | Gerencia Ambiente | Gerencia Deps | Gerencia Versão do Python | Arquivo de config | Melhor para |
|---|---|---|---|---|---|
| `venv` + `pip` | ✅ | ✅ | ❌ | `requirements.txt` | Iniciantes, projetos simples |
| `virtualenv` | ✅ | ❌ | ❌ | `requirements.txt` | Alternativa mais antiga ao `venv` |
| `conda` | ✅ | ✅ | ✅ | `environment.yml` | Ciência de Dados, bibliotecas C/C++ |
| `pipenv` | ✅ | ✅ | ❌ | `Pipfile` / `Pipfile.lock` | Projetos web e APIs |
| `poetry` | ✅ | ✅ | ❌ | `pyproject.toml` | Projetos modernos, bibliotecas, equipes |

---

## `virtualenv`

O `virtualenv` foi o predecessor do `venv` — tanto que o `venv` é basicamente uma versão simplificada dele, incorporada ao Python padrão.

Hoje, a maioria dos projetos usa `venv` diretamente. O `virtualenv` ainda é relevante em contextos legados ou quando se precisa de recursos extras (como suporte a versões muito antigas do Python).

```bash
# Instalar
pip install virtualenv

# Criar ambiente
virtualenv venv

# Ativar (Linux/macOS)
source venv/bin/activate
```

> 📌 **Recomendação:** Se você está começando, use `venv`. O `virtualenv` não oferece vantagens relevantes para casos de uso iniciantes.

---

## `conda`

O `conda` é uma ferramenta da empresa Anaconda, muito popular no mundo de **Ciência de Dados e Machine Learning**. Ele vai além do Python: consegue instalar bibliotecas escritas em C, C++ e Fortran — o que é essencial para pacotes como `numpy`, `scipy` e `tensorflow`.

### Diferenciais do `conda`
- Gerencia a versão do Python por ambiente (você pode ter Python 3.9 em um env e 3.11 em outro)
- Resolve conflitos de dependências de forma mais inteligente que o `pip`
- Possui um canal próprio de pacotes otimizados (`conda-forge`)

### Comandos básicos
```bash
# Criar ambiente com Python 3.11
conda create -n meu-projeto python=3.11

# Ativar
conda activate meu-projeto

# Instalar biblioteca
conda install pandas

# Exportar ambiente
conda env export > environment.yml

# Recriar ambiente a partir do arquivo
conda env create -f environment.yml

# Desativar
conda deactivate
```

> 📌 **Recomendação:** Use `conda` se você trabalha com Ciência de Dados, Machine Learning ou precisa gerenciar múltiplas versões do Python. Para os módulos deste repositório (análise de dados com pandas, visualização), o `conda` é uma escolha excelente.

---

## `pipenv`

O `pipenv` combina `venv` e `pip` em uma única ferramenta, com a proposta de simplificar o fluxo de trabalho. Ele cria dois arquivos:

- `Pipfile` — lista as dependências que você declarou explicitamente
- `Pipfile.lock` — registra as versões exatas de tudo (incluindo indiretas), garantindo reprodutibilidade

### Comandos básicos
```bash
# Instalar
pip install pipenv

# Criar ambiente e instalar biblioteca
pipenv install pandas

# Ativar o shell do ambiente
pipenv shell

# Instalar deps de desenvolvimento
pipenv install pytest --dev

# Instalar a partir do Pipfile
pipenv install
```

> 📌 **Recomendação:** O `pipenv` resolve bem o problema do `requirements.txt` verboso, mas perdeu popularidade para o `poetry`. É uma opção válida, mas não é mais o padrão da indústria.

---

## `poetry`

O `poetry` é a ferramenta mais moderna e completa da lista. Ele gerencia ambientes, dependências, versões do projeto e até a publicação de bibliotecas no PyPI — tudo em um único comando.

Usa o `pyproject.toml` como arquivo de configuração, que é o padrão oficial moderno do Python.

### Comandos básicos
```bash
# Instalar o poetry
pip install poetry

# Criar um novo projeto
poetry new meu-projeto

# Adicionar uma dependência
poetry add pandas

# Adicionar dep de desenvolvimento
poetry add pytest --group dev

# Ativar o ambiente virtual gerenciado pelo poetry
poetry shell

# Instalar dependências do pyproject.toml
poetry install
```

Exemplo de `pyproject.toml` gerado pelo `poetry`:
```toml
[tool.poetry]
name = "meu-projeto"
version = "0.1.0"
description = ""

[tool.poetry.dependencies]
python = "^3.11"
pandas = "^2.2.1"

[tool.poetry.group.dev.dependencies]
pytest = "^8.1.1"
```

> 📌 **Recomendação:** Use `poetry` em projetos novos, especialmente se você trabalha em equipe ou pretende publicar uma biblioteca. É a tendência atual do mercado.

---

## Qual usar?

```
Estou começando com Python
└─→ venv + pip  ✅

Trabalho com Ciência de Dados / ML
└─→ conda  ✅

Quero algo mais organizado que o pip, mas simples
└─→ pipenv ou poetry  ✅

Vou criar uma biblioteca ou trabalhar em equipe
└─→ poetry  ✅
```

> 💡 **Para este curso:** Continue com `venv` + `pip`. Quando chegar nos módulos de Pandas e Visualização de Dados, considere migrar para `conda`.

---

## 🧠 Fixando o Conceito

1. Por que o `conda` é especialmente popular em Ciência de Dados?
2. Qual é a diferença entre o `Pipfile` e o `Pipfile.lock` no `pipenv`?
3. O `poetry` e o `pipenv` resolvem um problema que o `venv` + `pip` tem — qual é esse problema?
4. Em que situação você escolheria `conda` em vez de `poetry`?

---

## ✅ Checklist desta Aula

- [ ] Conheço as principais ferramentas de gerenciamento de ambientes Python
- [ ] Entendo quando usar `conda` vs `venv`
- [ ] Sei o que é o `pyproject.toml` e para que serve
- [ ] Consigo recomendar a ferramenta certa dependendo do contexto do projeto

---

## ➡️ Próxima Aula

[Aula 05 — Boas Práticas e `.gitignore` →](./05.md)

Agora que você domina ambientes virtuais e suas alternativas, vamos fechar o módulo com as boas práticas para organizar seu projeto Python como um profissional.
