import random
import pygame
from src.config import (CORES_CARTAS,
    LARGURA_CARTA, ALTURA_CARTA, BRANCO, PRETO, AZUL_CARTA, LARGURA_TELA, ALTURA_TELA, ESPACAMENTO_CARTAS
)

class Carta:
    """Classe que representa uma única carta no tabuleiro."""
    def __init__(self, x, y, cor):
        self.rect = pygame.Rect(x, y, LARGURA_CARTA, ALTURA_CARTA)
        self.cor = cor
        self.revelada = False
        self.encontrada = False

    def desenhar(self, tela, fonte):
        """Renderiza a carta na tela."""
        sombra_rect = self.rect.inflate(4, 4)
        sombra_rect.topleft = (self.rect.x + 2, self.rect.y + 2)
        pygame.draw.rect(tela, (0, 0, 0, 50), sombra_rect, border_radius=10)
        
        if self.revelada or self.encontrada:
            pygame.draw.rect(tela, BRANCO, self.rect, border_radius=12)
            
            cor_rect_size = int(min(self.rect.width, self.rect.height) * 0.80) 
            cor_rect = pygame.Rect(
                self.rect.centerx - cor_rect_size // 2,
                self.rect.centery - cor_rect_size // 2,
                cor_rect_size,
                cor_rect_size
            )
            pygame.draw.rect(tela, self.cor, cor_rect, border_radius=8)
            pygame.draw.rect(tela, BRANCO, cor_rect, 2, border_radius=8)
        else:
            pygame.draw.rect(tela, AZUL_CARTA, self.rect, border_radius=12)

        pygame.draw.rect(tela, PRETO, self.rect, 4, border_radius=12)


def criar_tabuleiro():
    """Gera a lista de objetos Carta centralizados na tela."""
    cores = CORES_CARTAS * 2
    random.shuffle(cores)

    cartas = []
    colunas = 4
    linhas = 4

    largura_total = colunas * (LARGURA_CARTA + ESPACAMENTO_CARTAS) - ESPACAMENTO_CARTAS
    altura_total = linhas * (ALTURA_CARTA + ESPACAMENTO_CARTAS) - ESPACAMENTO_CARTAS
    offset_x = (LARGURA_TELA - largura_total) // 2
    offset_y = (ALTURA_TELA - altura_total) // 2 + 40

    indice = 0
    for linha in range(linhas):
        for coluna in range(colunas):
            x = offset_x + coluna * (LARGURA_CARTA + ESPACAMENTO_CARTAS)
            y = offset_y + linha * (ALTURA_CARTA + ESPACAMENTO_CARTAS)
            carta = Carta(x, y, cores[indice])
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