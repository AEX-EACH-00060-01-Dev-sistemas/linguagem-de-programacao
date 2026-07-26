# 📦 Aula 03 — `pip` e Gerenciamento de Dependências

> **Objetivo:** Aprender a usar o `pip` com proficiência e a gerenciar as dependências do seu projeto de forma organizada e reproduzível.

---

## O que é o `pip`?

O `pip` é o gerenciador de pacotes oficial do Python. Ele conecta o seu projeto ao [PyPI (Python Package Index)](https://pypi.org/) — o repositório público com mais de 500.000 bibliotecas prontas para uso.

Sempre que você executa `pip install pandas`, o pip:
1. Procura a biblioteca no PyPI
2. Baixa a versão mais recente (ou a que você especificou)
3. Instala no ambiente Python ativo (global ou virtual)

> 💡 **Lembre-se:** Com o ambiente virtual ativo, o `pip` instala apenas naquele ambiente. Sem ele ativo, instala globalmente.

---

## Comandos Essenciais do `pip`

### Instalar uma biblioteca
```bash
pip install pandas
```

### Instalar uma versão específica
```bash
pip install pandas==2.1.0
```

### Instalar uma versão mínima
```bash
pip install pandas>=2.0
```

### Atualizar uma biblioteca para a versão mais recente
```bash
pip install --upgrade pandas
```

### Desinstalar uma biblioteca
```bash
pip uninstall pandas
```

### Listar todas as bibliotecas instaladas no ambiente
```bash
pip list
```

Saída esperada:
```
Package    Version
---------- -------
numpy      1.26.4
pandas     2.2.1
pip        24.0
```

### Ver detalhes de uma biblioteca específica
```bash
pip show pandas
```

Saída esperada:
```
Name: pandas
Version: 2.2.1
Summary: Powerful data structures for data analysis
Author: The Pandas Development Team
Location: /meu-projeto/venv/lib/python3.11/site-packages
Requires: numpy, python-dateutil, pytz
```

### Verificar bibliotecas desatualizadas
```bash
pip list --outdated
```

---

## Gerenciando Dependências com `requirements.txt`

O `requirements.txt` é o arquivo que permite que qualquer pessoa recrie o seu ambiente virtual exato — na mesma máquina ou em outra.

### Gerar o arquivo com as dependências atuais
```bash
pip freeze > requirements.txt
```

Exemplo de `requirements.txt` gerado:
```
numpy==1.26.4
matplotlib==3.8.3
pandas==2.2.1
python-dateutil==2.9.0
pytz==2024.1
seaborn==0.13.2
```

> ⚠️ Note que o `pip freeze` lista **todas** as dependências, incluindo as indiretas (bibliotecas que as suas libs precisam). Isso garante reprodutibilidade total.

### Instalar dependências a partir do arquivo
```bash
pip install -r requirements.txt
```

Esse é o comando que um colega roda ao clonar o repositório.

---

## Versionamento de Dependências

Existem diferentes formas de especificar versões no `requirements.txt`:

| Notação | Significado | Quando usar |
|---------|-------------|-------------|
| `pandas==2.1.0` | Exatamente essa versão | Projetos em produção, máxima estabilidade |
| `pandas>=2.0` | Versão 2.0 ou superior | Projetos em desenvolvimento |
| `pandas>=2.0,<3.0` | Entre 2.0 e 3.0 (exclusive) | Bom equilíbrio entre flexibilidade e segurança |
| `pandas` | Qualquer versão | Não recomendado — pode quebrar no futuro |

> 💡 **Boas práticas:** Em projetos de estudo e análise de dados, `>=` funciona bem. Em projetos de produção ou em equipe, use `==` para garantir que todos usam exatamente a mesma versão.

---

## Separando Dependências de Desenvolvimento

Em projetos maiores, é comum ter dois arquivos:

```
requirements.txt          ← bibliotecas necessárias para rodar o projeto
requirements-dev.txt      ← ferramentas usadas apenas durante o desenvolvimento
```

Exemplo de `requirements-dev.txt`:
```
pytest==8.1.1
jupyterlab==4.1.5
black==24.3.0
```

Para instalar apenas as de desenvolvimento:
```bash
pip install -r requirements-dev.txt
```

---

## Menção: `pyproject.toml`

O `pyproject.toml` é o formato moderno de configuração de projetos Python, definido pelo [PEP 518](https://peps.python.org/pep-0518/). Ferramentas como `poetry` e `hatch` o utilizam para substituir o `requirements.txt` com mais recursos:

- Separação automática entre dependências de produção e desenvolvimento
- Gestão de versão do projeto
- Configuração de outras ferramentas (linters, formatadores) no mesmo arquivo

> 📌 Não se preocupe em dominar o `pyproject.toml` agora. Por enquanto, o `requirements.txt` resolve tudo que você precisa. O `pyproject.toml` aparece na **Aula 04**, quando falamos de `poetry`.

---

## 🧠 Fixando o Conceito

1. Qual é a diferença entre `pip install pandas` e `pip install pandas==2.1.0`?
2. Por que o `pip freeze` lista mais bibliotecas do que as que você instalou diretamente?
3. Em que situação você usaria `requirements-dev.txt` separado do `requirements.txt`?
4. O que acontece se um colega clona seu projeto, cria o ambiente virtual, mas não roda `pip install -r requirements.txt`?

---

## ✅ Checklist desta Aula

- [ ] Sei instalar bibliotecas com versão específica
- [ ] Sei listar e inspecionar bibliotecas instaladas
- [ ] Sei gerar o `requirements.txt` com `pip freeze`
- [ ] Sei instalar dependências a partir do `requirements.txt`
- [ ] Entendo as diferenças entre os operadores de versionamento (`==`, `>=`, `<`)

---

## ➡️ Próxima Aula

[Aula 04 — Alternativas ao `venv` →](./04.md)

O `venv` + `pip` é ótimo para começar. Mas existem outras ferramentas no ecossistema Python que resolvem os mesmos problemas com abordagens diferentes. Vamos conhecê-las.
