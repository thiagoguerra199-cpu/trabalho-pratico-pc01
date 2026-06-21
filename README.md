# Match Memory

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Rafael Lima Pais
- Alexandre de Souza Freitas Martins
- Thiago Guerra de Araújo
- Gabriel Cédric Carvalho Damazio

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

O jogo consiste em um tabuleiro com cartas viradas para baixo, cada uma contendo uma figura escondida. O jogador controla a partida escolhendo duas cartas por vez para revelar o conteúdo das cartas. O objetivo é encontrar todos os pares iguais utilizando o menor número possível de tentativas.

## Objetivo do jogador

Acertar todos os pares de cartas com o menor número de tentativas possível.

## Regras do jogo

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 0 tentativas.
- A cada duas cartas clicadas, uma tentativa é contabilizada.
- Se os itens revelados forem iguais, as cartas permanecem visíveis e descobertas.
- Se os itens forem diferentes, as cartas são viradas novamente para baixo após um breve intervalo.
- O jogo termina quando todos os pares de cartas foram encontrados.
- O vencedor é aquele que conseguir descobrir todos os pares com o menor número de tentativas

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
