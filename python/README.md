# 🐍 Python

Bem-vindo à seção dedicada à linguagem **Python**! Este material foi desenvolvido para transformar o seu conhecimento básico em uma habilidade prática voltada para o mercado de **Dados e Automação**.

---

## 🎯 Por que Python?
Conforme observado em nossa pesquisa com os alunos, o Python é a linguagem com maior interesse de aprendizado. No mundo real, ela é a ferramenta nº 1 para:
* **Ciência de Dados:** Analisar grandes volumes de informação.
* **Automação:** Substituir tarefas repetitivas em planilhas por scripts rápidos.
* **IA:** Base para os modelos de Inteligência Artificial.

---

## 📖 O que você vai aprender aqui?

Nesta pasta, o conteúdo está organizado em três pilares fundamentais:

### 1. 🛠️ O Jeito Profissional de Trabalhar
Antes do código, a organização. Aprenda a isolar seus projetos para evitar conflitos.
* [**Uso de Ambientes Virtuais (`venv`)**](./ambientes-virtuais/README.md) — Isole suas dependências por projeto.
* Gerenciamento de bibliotecas com **Pip**.

### 2. 📊 As Ferramentas Essenciais (Stack de Dados)
Focaremos nas bibliotecas que são o padrão da indústria:
* **Pandas:** Para manipulação de tabelas e arquivos (Excel, CSV, SQL).
* **NumPy:** Para cálculos matemáticos de alta performance.
* **Matplotlib & Seaborn:** Para criação de gráficos e visualização de dados.

### 3. 🧪 Prática com Notebooks
Utilizaremos arquivos `.ipynb` (Jupyter Notebooks) para que você possa ver o resultado do seu código linha por linha, facilitando o aprendizado.

---

## 🚀 Como Preparar seu Notebook

### ⚙️ Instalar e Executar o Jupyter Notebook

**Passo 1: Abra o terminal**
No Windows: Pressione as teclas Win + R, digite CMD e aperte Enter. Você também pode buscar por PowerShell no menu Iniciar do sistema.
No Linux: Pressione as teclas Ctrl + Alt + T em conjunto para abrir o Terminal.

**Passo 2: Instale o Jupyter**
Digite o comando abaixo na tela preta e pressione Enter para iniciar a instalação:
```bash
pip install notebook
```

**Passo 3: Atualize o gerenciador de pacotes (opcional, mas recomendado)**
Após a instalação, caso o próprio terminal peça para atualizar o pip, rode o comando abaixo e aguarde a conclusão:
```bash
python.exe -m pip install --upgrade pip
```
(no Linux modifique o começo do comando trocando python.exe por python3).

**Passo 4: Inicie o programa**
Por fim, para executar a interface do Jupyter no seu navegador, digite o comando:
```bash
jupyter notebook
```
Caso não abra de imediato no navegador copie um dos dois caminhos URL's que aparecerão no terminal após executar o comando. 
![Terminal Jupyter](imagens/comando%20jupyter%20notebook.png)

⚠️ **Solução de Problemas e Erros Comuns:**

* **Erros no Windows:** Caso surja algum erro de permissão negada durante a execução, feche a janela atual, busque pelo CMD no menu Iniciar, clique com o botão direito do mouse e selecione a opção "Executar como administrador" antes de rodar o programa.
* **Erros no Linux:** Se receber mensagens de acesso negado durante a instalação, adicione a palavra sudo antes do comando para rodar com privilégios de superusuário (exemplo: `sudo pip install notebook`).



