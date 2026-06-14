import pygame
from jogo import InteracaoJogador

pygame.init()

LARGURA = 800
ALTURA = 600
FPS = 60

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Memoria")

clock = pygame.time.Clock()

interacao = InteracaoJogador()

lista_de_cartas = []

rodando = True

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            interacao.processar_clique(evento.pos, lista_de_cartas)

    interacao.atualizar()

    tela.fill((30, 30, 30))

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
