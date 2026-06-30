# Sistema de Gerenciamento de Ocorrências

Projeto desenvolvido para a disciplina de **Algoritmos e Estruturas de Dados II (AED II)**.

O sistema simula um gerenciamento de ocorrências de suporte técnico, permitindo o cadastro, atendimento, busca e armazenamento das ocorrências utilizando diferentes estruturas de dados estudadas na disciplina.

## Integrantes

- Izadora Calvetti Souza
- Renan Bitencourt Pacheco

## Objetivo

Aplicar, na prática, os conceitos de Estruturas de Dados por meio de um sistema de gerenciamento de ocorrências, utilizando:

- Lista
- Fila
- Pilha
- Tabela Hash
- Algoritmo de Ordenação (Insertion Sort)
- Persistência em arquivo `.txt`

---

## Funcionalidades

-  Cadastro de ocorrências
-  Listagem de ocorrências
-  Atendimento por ordem de chegada (Fila)
-  Histórico de ações (Pilha)
-  Busca por tipo utilizando Tabela Hash
-  Ordenação das ocorrências por ID (Insertion Sort)
-  Salvamento das ocorrências em arquivo `.txt`
-  Carregamento das ocorrências salvas
-  Geração automática de relatório ordenado ao encerrar o sistema

---

## Estruturas de Dados Utilizadas

### Lista

Responsável por armazenar todas as ocorrências cadastradas.

```python
lista_geral = []
```

---

### Fila

Utilizada para controlar a ordem de atendimento das ocorrências (FIFO - First In, First Out).

```python
insercao_fila_chegada = []
```

---

### Pilha

Armazena o histórico das ações realizadas no sistema (LIFO - Last In, First Out).

```python
registro_pilha_historico = []
```

---

### 🔎 Tabela Hash

Utilizada para realizar buscas rápidas por tipo de ocorrência.

```python
tabela_hash_tipo = [[] for _ in range(10)]
```

---

## Algoritmo de Ordenação

Foi implementado o **Insertion Sort** para ordenar as ocorrências pelo ID.

O algoritmo é utilizado em:

- `ordenar_ocorrencias()`
- `gerar_relatorio_ordenado()`

Trecho principal:

```python
while j >= 0 and copia_lista[j]["id"] > variavel_chave["id"]:
    copia_lista[j + 1] = copia_lista[j]
    j -= 1

copia_lista[j + 1] = variavel_chave
```

---

## Persistência dos Dados

As ocorrências são armazenadas no arquivo:

```
ocorrencias.txt
```

Ao encerrar o sistema também é gerado automaticamente:

```
relatorio_ordenado.txt
```

contendo todas as ocorrências organizadas por ID.

---

## Como executar

### Pré-requisitos

- Python 3.10 ou superior

Verifique a instalação:

```bash
python --version
```

ou

```bash
python3 --version
```

---

### Clonando o repositório

```bash
git clone https://github.com/iza416/Trabalho_integrador_aed2.git
```

Entre na pasta do projeto:

```bash
cd Trabalho_integrador_aed2
```

---

### Executando

Windows

```bash
python main.py
```

Linux

```bash
python3 main.py
```

---