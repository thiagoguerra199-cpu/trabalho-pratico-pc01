from src.config import PONTOS_BASE_PAR, PENALIDADE_TEMPO, PONTOS_MINIMOS_PAR

def calcular_pontos(tempo_segundos):
    """Calcula a pontuação de um par baseada na rapidez (tempo em segundos).
    Quanto mais rápido, maior a pontuação. Existe um valor mínimo garantido."""
    pontos = PONTOS_BASE_PAR - (tempo_segundos * PENALIDADE_TEMPO)
    return max(pontos, PONTOS_MINIMOS_PAR)


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Função utilitária para checar se dois objetos retangulares se encostam."""
    return retangulo_1.colliderect(retangulo_2)

def verificar_par(carta1, carta2):
    """Compara duas cartas para verificar se são iguais."""
    return carta1.emoji == carta2.emoji