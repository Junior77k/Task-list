# 📝 Task-list

Um projeto simples de **lista de tarefas no terminal**, desenvolvido em Python.
Permite adicionar, listar e remover tarefas de forma interativa.

---

## 📌 Sobre o Projeto

Este projeto foi criado para praticar conceitos básicos de programação, como:

* Estruturas de repetição (`while`)
* Condicionais (`if`, `elif`)
* Listas
* Entrada e saída de dados

---

## ⚙️ Funcionalidades

* ➕ Adicionar tarefas
* 📜 Listar tarefas
* ❌ Remover tarefas
* 🚪 Sair do programa

---

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado
2. Execute o arquivo:

```bash
python nome_do_arquivo.py
```

---

## 🎮 Como Usar

Ao iniciar o programa, você verá o menu:

```
[i]nserir [a]pagar [l]istar [s]air:
```

### ➕ Inserir (`i`)

Adiciona uma nova tarefa à lista.

---

### 📜 Listar (`l`)

Mostra todas as tarefas cadastradas.

---

### ❌ Apagar (`a`)

* Exibe as tarefas existentes
* Você digita o nome da tarefa que deseja remover
* A tarefa é removida se encontrada

---

### 🚪 Sair (`s`)

Encerra o programa.

---

## 📁 Estrutura

```bash
.
└── lista_tarefas.py
```

---

## ⚠️ Limitações

O projeto é funcional, mas possui algumas limitações:

* A remoção é feita pelo **nome da tarefa**, o que pode causar erros se digitado incorretamente
* Não há persistência (as tarefas são perdidas ao fechar o programa)
* Não há validação robusta de entrada
* Tarefas duplicadas podem causar confusão

---

## 🧠 Possíveis Melhorias

* Remover tarefas por número (índice)
* Salvar tarefas em arquivo (ex: `.txt` ou `.json`)
* Criar interface gráfica
* Separar o código em funções
* Adicionar edição de tarefas

---

## 📌 Exemplo de Uso

```
Selecione uma opcao
[i]nserir [a]pagar [l]istar [s]air: i
Adicionar nova tarefa: estudar python
Nova tarefa cadastrada

[i]nserir [a]pagar [l]istar [s]air: l
1 - estudar python
```

---

## 📄 Licença

Este projeto é livre para uso e modificação.
