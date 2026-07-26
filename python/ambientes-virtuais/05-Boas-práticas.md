# ✅ Aula 05 — Boas Práticas e `.gitignore`

> **Objetivo:** Aprender o que deve (e o que não deve) ir para o Git, como estruturar um projeto Python profissional e sair com um checklist prático para usar em todos os seus projetos.

---

## O que NÃO subir para o Git

Um dos erros mais comuns de quem está começando é commitar a pasta `venv/` no repositório. Isso é um problema por vários motivos:

- A pasta `venv/` pode ter **centenas de megabytes** de arquivos binários
- Ela é gerada automaticamente — não precisa ser versionada
- Os caminhos absolutos dentro do `venv/` são específicos da sua máquina e não funcionam em outra
- O Git fica lento e o repositório fica enorme sem necessidade

> 💡 **Regra:** A pasta `venv/` nunca vai para o Git. O `requirements.txt` vai.

---

## Configurando o `.gitignore`

O arquivo `.gitignore` diz ao Git quais arquivos e pastas ele deve ignorar.

### Criando o `.gitignore`

Crie um arquivo chamado `.gitignore` na raiz do seu projeto (sem extensão):

```
meu-projeto/
├── .gitignore       ← aqui
├── requirements.txt
├── main.py
└── venv/            ← essa pasta será ignorada
```

### Conteúdo recomendado do `.gitignore` para projetos Python

```gitignore
# Ambiente virtual
venv/
.venv/
env/
.env/

# Arquivos compilados do Python
__pycache__/
*.py[cod]
*.pyo

# Jupyter Notebook
.ipynb_checkpoints/

# Variáveis de ambiente e segredos
.env
*.env

# Sistemas operacionais
.DS_Store          # macOS
Thumbs.db          # Windows

# IDEs
.vscode/
.idea/
*.swp

# Distribuição / build
dist/
build/
*.egg-info/
```

> 💡 **Dica:** O site [gitignore.io](https://www.toptal.com/developers/gitignore) gera um `.gitignore` completo para qualquer combinação de linguagem, sistema operacional e IDE.

---

## O que DEVE ir para o Git

| Arquivo / Pasta | Por quê |
|---|---|
| `requirements.txt` | Permite recriar o ambiente exato |
| `.gitignore` | Protege o repositório de arquivos desnecessários |
| `README.md` | Documenta o projeto |
| Seus scripts `.py` e notebooks `.ipynb` | São o trabalho em si |
| `pyproject.toml` (se usar poetry) | Substitui o `requirements.txt` |

---

## Estrutura de Projeto Python Recomendada

Para projetos de análise de dados e estudos (como os deste repositório):

```
meu-projeto/
├── .gitignore
├── README.md
├── requirements.txt
├── venv/                  ← ignorado pelo Git
├── dados/
│   └── dataset.csv
├── notebooks/
│   ├── 01-exploracao.ipynb
│   └── 02-analise.ipynb
└── src/
    └── utils.py
```

Para projetos maiores (APIs, sistemas):

```
meu-projeto/
├── .gitignore
├── README.md
├── pyproject.toml         ← se usar poetry
├── requirements.txt
├── requirements-dev.txt
├── venv/                  ← ignorado pelo Git
├── src/
│   ├── __init__.py
│   └── main.py
└── tests/
    └── test_main.py
```

---

## Fluxo Completo: Do Zero ao Repositório

Siga este fluxo sempre que iniciar um projeto Python do zero:

```bash
# 1. Crie e entre na pasta do projeto
mkdir meu-projeto && cd meu-projeto

# 2. Inicialize o repositório Git
git init

# 3. Crie o ambiente virtual
python -m venv venv

# 4. Ative o ambiente
source venv/bin/activate          # Linux/macOS
venv\Scripts\Activate.ps1         # Windows PowerShell

# 5. Instale as bibliotecas necessárias
pip install pandas matplotlib

# 6. Gere o requirements.txt
pip freeze > requirements.txt

# 7. Crie o .gitignore (com venv/ listado)
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".ipynb_checkpoints/" >> .gitignore

# 8. Crie o README.md
echo "# Meu Projeto" >> README.md

# 9. Faça o primeiro commit
git add .
git commit -m "feat: estrutura inicial do projeto"
```

---

## Quando outro desenvolvedor clona o projeto

```bash
# 1. Clonar o repositório
git clone https://github.com/usuario/meu-projeto.git
cd meu-projeto

# 2. Criar o ambiente virtual localmente
python -m venv venv

# 3. Ativar
source venv/bin/activate          # Linux/macOS
venv\Scripts\Activate.ps1         # Windows PowerShell

# 4. Instalar as dependências do projeto
pip install -r requirements.txt

# 5. Pronto! O ambiente está idêntico ao original
```

---

## 📋 Checklist do Desenvolvedor Python

Use este checklist antes de qualquer commit:

```
Antes de commitar:
[ ] O arquivo .gitignore existe e contém venv/
[ ] O requirements.txt está atualizado (pip freeze > requirements.txt)
[ ] Não há segredos ou senhas no código (use variáveis de ambiente)
[ ] O README.md descreve como configurar e rodar o projeto
[ ] Rodei o código e está funcionando no ambiente virtual

Antes de subir um projeto para o GitHub pela primeira vez:
[ ] Revisei todos os arquivos com git status
[ ] Verifiquei que venv/ não aparece em git status
[ ] O repositório tem um README.md claro
[ ] O requirements.txt está presente
```

---

## 🧠 Fixando o Conceito

1. Por que commitar a pasta `venv/` é um problema mesmo que o código funcione?
2. O que acontece se você não tiver um `requirements.txt` e um colega clonar seu repositório?
3. Qual é a diferença entre o `.gitignore` e o `requirements.txt` em termos de propósito?
4. Por que variáveis de ambiente (`.env`) também devem estar no `.gitignore`?

---

## ✅ Checklist desta Aula

- [ ] Sei criar e configurar o `.gitignore` para projetos Python
- [ ] Entendo o que deve e o que não deve ser versionado no Git
- [ ] Conheço a estrutura de projeto Python recomendada
- [ ] Sei o fluxo completo do zero ao repositório
- [ ] Sei como um colega recria meu ambiente ao clonar o projeto

---

## 🎉 Fim do Módulo — Ambientes Virtuais

Parabéns! Você concluiu o módulo de Ambientes Virtuais. Agora você sabe:

1. **Por que** ambientes virtuais existem e qual problema resolvem
2. **Como usar** o `venv` no dia a dia (criar, ativar, instalar, desativar)
3. **Como gerenciar** dependências com `pip` e `requirements.txt`
4. **Quais alternativas** existem (`conda`, `pipenv`, `poetry`) e quando usar cada uma
5. **Como organizar** seu projeto como um desenvolvedor profissional

---

## ➡️ Próximo Módulo

[← Voltar ao índice do módulo](./README.md)

[Próximo Módulo: Introdução ao Python →](../00-introducao/00.md)
