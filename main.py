import pygame
from jogo import InteracaoJogador

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Memoria")

interacao = InteracaoJogador()

lista_de_cartas = []

rodando = True

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            interacao.processar_clique(evento.pos, lista_de_cartas)

    interacao.atualizar()

    tela.fill((30, 30, 30))

    pygame.display.update()

pygame.quit()