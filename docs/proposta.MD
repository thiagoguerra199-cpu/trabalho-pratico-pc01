# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Escreva aqui o nome provisório do jogo.

> Emoji Match

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1:Alexandre de Souza Freitas Martins
- Nome 2:Gabriel Cédric Carvalho Damazio
- Nome 3:Thiago Guerra de Araujo


## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

> Jogo da Memória

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

> O jogo consiste em um tabuleiro com cartas viradas para baixo, cada uma contendo um emoji escondido. O jogador controla a partida escolhendo duas cartas por vez para revelar seus emojis. O objetivo é encontrar todos os pares iguais utilizando o menor número possível de tentativas.

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

> Acertar todos os pares de emojis com o menor número de tentativas

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: O jogador começa com 0 tentativas e 0 pontos
- Regra 2: A cada duas cartas em que o jogador clicar será equivalente a uma tentativa
- Regra 3: Cada duas cartas iguais vale 1 ponto
- Regra 4: Se as cartas forem diferentes, elas são viradas novamente para baixo.
- Regra 5: O jogo termina quando todos os pares de cartas foram encontrados. 

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> O jogador vence ao encontrar todos os pares de emojis do tabuleiro. Ao final da partida, o sistema exibe a quantidade de tentativas realizadas. Quanto menor o número de tentativas, melhor o desempenho do jogador.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

> A partida termina quando o jogador encontra todos os pares de emojis presentes no tabuleiro. Como o jogo não possui vidas nem limite de tempo, não há uma condição de derrota.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> Um tabuleiro contendo cartas com emojis

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> O desafio é memorizar a posição dos emojis para encontrar os pares com menos tentativas.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> As cartas com emojis

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> O jogador começa com 0 tentativas, o jogo registra o número de tentativas e o progresso é medido pela quantidade de pares encontrados.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando: Botão esquerdo do mouse: Revelar o emoji da carta


## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> * `main.py`: inicia a execução do jogo;
* `src/jogo.py`: contém a lógica principal da partida;
* `src/sprites.py`: gerencia os emojis e elementos visuais do jogo;
* `src/config.py`: armazena configurações do jogo;
* `src/funcoes.py`: reúne funções auxiliares;
* `src/dados.py`: realiza a leitura e gravação de dados;
* `tests/test_logica.py`: contém testes da lógica do jogo.



## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> Emojis utilizados nas cartas do jogo ou imagens dos emojis

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: Implementar a lógica para verificar se duas cartas formam um par.
- Dificuldade 2: Embaralhar as cartas e organizar o tabuleiro corretamente.
- Dificuldade 3: Controlar as tentativas e exibir as informações na tela.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> A versão mínima do jogo terá um tabuleiro com cartas contendo pares de emojis, sistema de seleção de cartas pelo jogador, verificação de pares, contador de tentativas e tela de vitória ao encontrar todos os pares.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: Sistema de níveis, em que a dificuldade aumenta após cada vitória.
- Melhoria 2: Diminuir gradualmente o tempo de exibição das cartas conforme o jogador avança de nível.
- Melhoria 3: Adicionar uma tela inicial e uma tela de vitória mais elaborada.