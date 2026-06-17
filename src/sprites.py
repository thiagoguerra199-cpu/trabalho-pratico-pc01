import random
import pygame
from src.config import (CORES_CARTAS,
    LARGURA_CARTA, ALTURA_CARTA, BRANCO, PRETO, AZUL_CARTA, LARGURA_TELA, ALTURA_TELA
)

class Carta:
    """Classe que representa uma única carta no tabuleiro."""
    def __init__(self, x, y, emoji):
        # Define a posição física (rect) e o conteúdo (letra/emoji)
        self.rect = pygame.Rect(x, y, LARGURA_CARTA, ALTURA_CARTA)
        self.emoji = emoji
        self.revelada = False
        self.encontrada = False

    def desenhar(self, tela, fonte):
        """Renderiza a carta: aberta (branco com letra) ou fechada (azul)."""
        if self.revelada or self.encontrada:
            pygame.draw.rect(tela, BRANCO, self.rect, border_radius=10) # Fundo branco da carta revelada
            
            # Desenha um retângulo colorido no centro da carta
            # Aumentado para 85% para a cor ocupar quase toda a carta
            cor_rect_size = int(min(self.rect.width, self.rect.height) * 0.85) 
            cor_rect = pygame.Rect(
                self.rect.centerx - cor_rect_size // 2,
                self.rect.centery - cor_rect_size // 2,
                cor_rect_size,
                cor_rect_size
            )
            pygame.draw.rect(tela, self.emoji, cor_rect, border_radius=5) # self.emoji agora é a cor
        else:
            pygame.draw.rect(tela, AZUL_CARTA, self.rect, border_radius=10)

        # Borda da carta
        pygame.draw.rect(tela, PRETO, self.rect, 3, border_radius=10)


def criar_tabuleiro():
    """Gera a lista de objetos Carta centralizados na tela."""
    cores = CORES_CARTAS * 2 # Usa a lista de cores definida em config.py
    random.shuffle(cores)

    cartas = []
    colunas = 4
    linhas = 4
    espacamento = 20

    # Centralizar o tabuleiro
    largura_total = colunas * (LARGURA_CARTA + espacamento) - espacamento
    altura_total = linhas * (ALTURA_CARTA + espacamento) - espacamento
    offset_x = (LARGURA_TELA - largura_total) // 2
    # Aumentado o deslocamento Y para 60 para dar mais espaço ao cronômetro no topo
    offset_y = (ALTURA_TELA - altura_total) // 2 + 60

    indice = 0
    for linha in range(linhas):
        for coluna in range(colunas):
            x = offset_x + coluna * (LARGURA_CARTA + espacamento)
            y = offset_y + linha * (ALTURA_CARTA + espacamento)
            carta = Carta(x, y, cores[indice]) # Passa a cor para a carta
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