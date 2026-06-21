# Configurações centrais do jogo (tela, cores e caminhos de arquivos).
# Dimensões da janela e taxa de quadros (Frames Per Second)
LARGURA_TELA = 900
ALTURA_TELA = 700
FPS = 60

TITULO_JOGO = "Jogo da Memória - Grupo X "

BRANCO     = (236, 240, 241)
PRETO      = (44, 62, 80)
CINZA      = (149, 165, 166)
AZUL_CARTA = (41, 128, 185)
VERDE      = (46, 204, 113)
VERMELHO   = (231, 76, 60)
COR_FUNDO  = (22, 39, 77)

COR_CARTA_1 = (50, 50, 50)     # Preto
COR_CARTA_2 = (150, 150, 150)  # Cinza
COR_CARTA_3 = (33, 150, 243)   # Azul brilhante
COR_CARTA_4 = (233, 30, 99)    # Rosa intenso
COR_CARTA_5 = (156, 39, 176)   # Roxo/Magenta
COR_CARTA_6 = (255, 193, 7)    # Amarelo ouro
COR_CARTA_7 = (76, 175, 80)    # Verde claro
COR_CARTA_8 = (255, 152, 0)    # Laranja brilhante

CORES_CARTAS = [COR_CARTA_1, COR_CARTA_2, COR_CARTA_3, COR_CARTA_4, COR_CARTA_5, COR_CARTA_6, COR_CARTA_7, COR_CARTA_8]

LARGURA_CARTA = 75
ALTURA_CARTA = 100
ESPACAMENTO_CARTAS = 25
ATRASO_REVELACAO = 1000  # Milissegundos
TEMPO_PREVIEW = 2500    # Tempo que as cartas ficam abertas no início

# Configurações de Pontuação por Tempo
PONTOS_BASE_PAR = 100
PENALIDADE_TEMPO = 2
PONTOS_MINIMOS_PAR = 10

# Caminhos para arquivos externos
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"