# Configurações centrais do jogo (tela, cores e caminhos de arquivos).
# Dimensões da janela e taxa de quadros (Frames Per Second)
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60

TITULO_JOGO = "Jogo da Memória - Grupo X"

# Cores
BRANCO     = (236, 240, 241)
PRETO      = (44, 62, 80)
CINZA      = (149, 165, 166)
AZUL_CARTA = (52, 152, 219)
VERDE      = (46, 204, 113)
VERMELHO   = (231, 76, 60)
COR_FUNDO  = (52, 73, 94)

# Cores para as cartas (8 pares)
COR_CARTA_1 = (0, 0, 0)       # Preto
COR_CARTA_2 = (60, 179, 113)  # MediumSeaGreen
COR_CARTA_3 = (255, 215, 0)   # Gold
COR_CARTA_4 = (106, 90, 205)  # SlateBlue
COR_CARTA_5 = (255, 160, 122) # LightSalmon
COR_CARTA_6 = (0, 206, 209)   # DarkTurquoise
COR_CARTA_7 = (138, 43, 226)  # BlueViolet
COR_CARTA_8 = (255, 140, 0)   # DarkOrange

CORES_CARTAS = [COR_CARTA_1, COR_CARTA_2, COR_CARTA_3, COR_CARTA_4, COR_CARTA_5, COR_CARTA_6, COR_CARTA_7, COR_CARTA_8]
# Configurações das Cartas
# Define o tamanho visual de cada carta e os tempos de animação/espera
LARGURA_CARTA = 90
ALTURA_CARTA = 120
ATRASO_REVELACAO = 1000  # Milissegundos (1 segundo)
TEMPO_PREVIEW = 2000    # Tempo que as cartas ficam abertas no início

# Configurações de Pontuação por Tempo
PONTOS_BASE_PAR = 100    # Pontuação máxima inicial por par
PENALIDADE_TEMPO = 2     # Pontos perdidos a cada segundo que passa
PONTOS_MINIMOS_PAR = 10  # Pontuação mínima garantida ao acertar um par

# Caminhos para arquivos externos (persistência de dados e imagens)
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"