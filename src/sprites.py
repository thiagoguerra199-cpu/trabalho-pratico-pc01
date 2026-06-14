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
        self.encontrada = False

    def desenhar(self, tela, fonte):
        if self.revelada or self.encontrada:
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
    emojis = ["😀", "😎", "🐱", "🎮"] * 2
    random.shuffle(emojis)

    cartas = []

    indice = 0

    for linha in range(2):
        for coluna in range(4):

            x = 100 + coluna * 130
            y = 150 + linha * 130

            carta = Carta(x, y, emojis[indice])

            cartas.append(carta)

            indice += 1

    return cartas


def desenhar_tentativas(tela, fonte, tentativas):
    texto = fonte.render(
        f"Tentativas: {tentativas}",
        True,
        PRETO
    )

    tela.blit(texto, (20, 20))


def desenhar_vitoria(tela, fonte):
    texto = fonte.render(
        "Parabens! Voce venceu!",
        True,
        PRETO
    )

    tela.blit(texto, (150, 50))