import random
import pygame
from src.config import (
    LARGURA_CARTA, ALTURA_CARTA, BRANCO, PRETO, AZUL_CARTA, LARGURA_TELA, ALTURA_TELA
)

class Carta:
    def __init__(self, x, y, emoji):
        self.rect = pygame.Rect(x, y, LARGURA_CARTA, ALTURA_CARTA)
        self.emoji = emoji
        self.revelada = False
        self.encontrada = False

    def desenhar(self, tela, fonte):
        if self.revelada or self.encontrada:
            pygame.draw.rect(tela, BRANCO, self.rect, border_radius=10)

            texto = fonte.render(self.emoji, True, PRETO)

            tela.blit(
                texto,
                (
                    self.rect.centerx - texto.get_width() // 2,
                    self.rect.centery - texto.get_height() // 2
                )
            )
        else:
            pygame.draw.rect(tela, AZUL_CARTA, self.rect, border_radius=10)

        # Borda da carta
        pygame.draw.rect(tela, PRETO, self.rect, 3, border_radius=10)


def criar_tabuleiro():
    letras = ["A", "B", "C", "D", "E", "F", "G", "H"] * 2
    random.shuffle(letras)

    cartas = []
    colunas = 4
    linhas = 4
    espacamento = 20

    # Centralizar o tabuleiro
    largura_total = colunas * (LARGURA_CARTA + espacamento) - espacamento
    altura_total = linhas * (ALTURA_CARTA + espacamento) - espacamento
    offset_x = (LARGURA_TELA - largura_total) // 2
    offset_y = (ALTURA_TELA - altura_total) // 2 + 30

    indice = 0
    for linha in range(linhas):
        for coluna in range(colunas):
            x = offset_x + coluna * (LARGURA_CARTA + espacamento)
            y = offset_y + linha * (ALTURA_CARTA + espacamento)
            carta = Carta(x, y, letras[indice])
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