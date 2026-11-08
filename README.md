# CS50x — Introduction to Computer Science

Resolução dos problem sets do curso **CS50x: Harvard's Introduction to Computer Science**.

![C](https://img.shields.io/badge/C-A8B9CC?logo=c&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-003B57?logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20andamento-yellow)

## Sobre

Repositório com as minhas soluções do CS50x, curso de introdução à ciência da computação que passa por algoritmos, estruturas de dados, gerenciamento de memória, Python, SQL e desenvolvimento web.

O foco do início do curso é a linguagem **C**, que ajuda a entender como o computador funciona por baixo das abstrações.

## Conteúdo

| Semana | Tema | Linguagem | Status |
|:------:|------|-----------|:------:|
| 0 | Scratch | Scratch | ⬜ |
| 1 | C | C | ⬜ |
| 2 | Arrays | C | ⬜ |
| 3 | Algorithms | C | ⬜ |
| 4 | Memory | C | ⬜ |
| 5 | Data Structures | C | ⬜ |
| 6 | Python | Python | ⬜ |
| 7 | SQL | SQL | ⬜ |
| 8 | HTML, CSS, JavaScript | Web | ⬜ |
| 9 | Flask | Python | ⬜ |
| 10 | Final Project | — | ⬜ |

> Troque ⬜ por ✅ conforme for concluindo cada semana.

## Estrutura

```
.
├── week1/
│   ├── hello/
│   │   └── hello.c
│   └── mario/
│       └── mario.c
├── week2/
├── ...
└── README.md
```

## Tópicos praticados

- Lógica de programação e fundamentos de C
- Compilação com `make` / `clang` e depuração com `debug50`
- Arrays, strings e ponteiros
- Algoritmos de busca e ordenação, e análise de complexidade
- Alocação dinâmica de memória (`malloc` / `free`) e `valgrind`
- Estruturas de dados: listas encadeadas, tabelas hash, *tries*
- Python, SQL e desenvolvimento web com Flask

## Como compilar e executar (C)

```bash
# clonar o repositório
git clone https://github.com/BrunoSpindola/CS50x-Harvard.git
cd CS50x-Harvard

# compilar e executar um problema
cd week1/hello
make hello
./hello
```

> Algumas tarefas usam a biblioteca `cs50.h`. Para compilar fora do ambiente do CS50, é preciso [instalá-la](https://github.com/cs50/libcs50) e linkar com `-lcs50`.

## Aviso de honestidade acadêmica

Este repositório documenta meu aprendizado. Se você estiver cursando o CS50x, resolva os problemas por conta própria: copiar soluções viola a [política de honestidade acadêmica do CS50](https://cs50.harvard.edu/x/honesty/).

## Autor

**Bruno Spindola**
[LinkedIn](https://linkedin.com/in/bruno-spindola) · [GitHub](https://github.com/BrunoSpindola)

## Referências

- [CS50x — Harvard](https://cs50.harvard.edu/x/)
