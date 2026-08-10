# Primeiros passos

---
[← Anterior: Paradigmas da Programação](01-Paradigmas.md) | [Próximo: Literais e Variáveis →](03-Literais-e-Variáveis.md)

---

Para desenvolver puramente o python, só precisamos de um editor de texto comum (como o bloco de notas), mas para facilitarmos nossa vida, podemos usar IDE's própria de Python (como Pycharm, Jupyter, etc.) ou editores de texto mais completos (como o Visual Studio Code).
\
Antes de tudo, precisamos instalar tudo que vamos usar: Visual Studio Code e o Python.

## Instalação do Python
O Python é uma linguagem interpretada, ou seja, precisamos de um interpretador!

### Linux
Normalmente, máquinas Linux já vem com o Python instalado. Para verificar, abra o terminal e execute:

```bash
python3 --version
```

Se não estiver instalado, basta rodar:

```bash
sudo apt install python3
```

### Windows
No Windows, o Python não vem instalado por padrão. Acesse [python.org/downloads](https://www.python.org/downloads/) e baixe o instalador.

> ⚠️ Durante a instalação, marque a opção **"Add Python to PATH"** antes de clicar em *Install Now*. Sem isso, o Windows não vai reconhecer o comando `python` no terminal.

Para verificar se a instalação funcionou, abra o PowerShell e execute:

```powershell
python --version
```

## Instalação do VSCode
Acesse [code.visualstudio.com](https://code.visualstudio.com/) e baixe o instalador para o seu sistema operacional.

Após instalar, abra o VSCode e instale a extensão **Python** (da Microsoft) — ela adiciona suporte a sintaxe, depuração e execução de arquivos `.py` diretamente no editor. Para instalá-la, vá em *Extensions* (Ctrl+Shift+X), pesquise por "Python" e clique em *Install*.

## Google Colab
O [Google Colab](https://colab.research.google.com/) é uma alternativa online que não exige instalação de nada. É ideal para:

* Testar snippets rápidos sem precisar abrir o VSCode
* Fazer exercícios pontuais
* Compartilhar código com outras pessoas facilmente

> **Limitações**: precisa de conexão com a internet e o estado das variáveis é perdido ao encerrar a sessão.

## Primeiro Código
Com tudo instalado, crie uma pasta para o curso e, dentro dela, crie um arquivo chamado `hello.py`. Escreva nele:

```python
print("Hello, World!")
```

No terminal integrado do VSCode (atalho: **Ctrl + `**), navegue até a pasta e execute:

```bash
python3 hello.py   # Linux
python hello.py    # Windows
```

Se aparecer `Hello, World!` no terminal, seu ambiente está pronto!

---
[← Anterior: Paradigmas da Programação](01-Paradigmas.md) | [Próximo: Literais e Variáveis →](03-Literais-e-Variáveis.md)

---
