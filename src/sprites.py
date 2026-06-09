import random
import pygame
from src.config import (
    LARGURA_CARTA, ALTURA_CARTA, BRANCO, PRETO, AZUL_CARTA
)

class Carta:
    def __init__(self, x, y, emoji):
        self.rect = pygame.Rect(x, y, LARGURA_CARTA, ALTURA_CARTA)
        self.emoji = emoji
        self.revelada = False

    def desenhar(self, tela, fonte):
        if self.revelada:
            pygame.draw.rect(tela, BRANCO, self.rect)
            texto = fonte.render(self.emoji, True, PRETO)
            tela.blit(
                texto,
                (
                    self.rect.centerx - texto.get_width() // 2,
                    self.rect.centery - texto.get_height() // 2
                )
            )
        else:
            pygame.draw.rect(tela, AZUL_CARTA, self.rect)

        pygame.draw.rect(tela, PRETO, self.rect, 2)


def criar_tabuleiro():
    # Criando pares de emojis
    emojis = ["😀", "😎", "🐱", "🎮"] * 2
    random.shuffle(emojis)

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