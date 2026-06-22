# 🧰 Ambientes Virtuais em Python

Imagine que você tem dois projetos no mesmo computador:

- **Projeto A** precisa da versão `1.5` de uma biblioteca.
- **Projeto B** precisa da versão `2.0` da mesma biblioteca.

Se você instalar bibliotecas diretamente no Python do seu sistema, os dois projetos vão brigar pela mesma versão — e um deles vai quebrar.

Um **ambiente virtual** resolve isso criando uma **cópia isolada do Python** para cada projeto. Cada ambiente tem suas próprias bibliotecas, na versão exata que aquele projeto precisa, sem interferir nos demais.

> 💡 **Regra de ouro:** Todo projeto Python profissional usa um ambiente virtual. É o primeiro passo antes de escrever qualquer linha de código.

---

## 📚 Índice do Módulo

| Aula | Título | Descrição |
|------|--------|-----------|
| [01](./01.md) | Por que usar Ambientes Virtuais? | O problema dos conflitos de versão, comparativo e analogias |
| [02](./02.md) | `venv` na Prática | Criar, ativar, instalar pacotes e desativar o ambiente |
| [03](./03.md) | `pip` e Gerenciamento de Dependências | `requirements.txt`, versionamento e boas práticas de pacotes |
| [04](./04.md) | Alternativas ao `venv` | Comparativo entre `venv`, `conda`, `pipenv` e `poetry` |
| [05](./05.md) | Boas Práticas e `.gitignore` | O que commitar, estrutura de projeto e checklist profissional |

---

## 🚀 Por onde começar?

Se você nunca usou ambientes virtuais, comece pela **Aula 01** e siga a ordem. Cada aula se apoia na anterior.

Se já sabe o básico de `venv` e quer avançar, pule direto para a **Aula 03** ou **Aula 04**.
