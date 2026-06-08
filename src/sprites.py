

import pygame


LARGURA_CARTA = 100
ALTURA_CARTA = 100

class Carta:
    def __init__(self, x, y, emoji):
        self.rect = pygame.Rect(x, y, LARGURA_CARTA, ALTURA_CARTA)
        self.emoji = emoji
        self.revelada = False

    def desenhar(self, tela, fonte):
        if self.revelada:
            pygame.draw.rect(tela, (255, 255, 255), self.rect)
            texto = fonte.render(self.emoji, True, (0, 0, 0))
            tela.blit(
                texto,
                (
                    self.rect.centerx - texto.get_width() // 2,
                    self.rect.centery - texto.get_height() // 2
                )
            )
        else:
            pygame.draw.rect(tela, (100, 100, 255), self.rect)

        pygame.draw.rect(tela, (0, 0, 0), self.rect, 2)


def criar_tabuleiro():
    emojis = ["😀", "😎", "🐱", "🎮"]

    cartas = []

    indice = 0

    for linha in range(2):
        for coluna in range(2):

            x = 150 + coluna * 150
            y = 150 + linha * 150

            carta = Carta(x, y, emojis[indice])

            cartas.append(carta)

            indice += 1

    return cartas