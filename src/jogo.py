import pygame

class InteracaoJogador:
    def __init__(self):
        self.cartas_selecionadas = [] 
        self.bloqueado = False        
        self.tempo_espera = 0         
        self.atraso = 1000            
    def processar_clique(self, pos_mouse, lista_cartas):
        
        if self.bloqueado:
            return
        for carta in lista_cartas:
            if carta.rect.collidepoint(pos_mouse) and not carta.revelada and not carta.combinada:
                carta.revelada = True
                self.cartas_selecionadas.append(carta)
                if len(self.cartas_selecionadas) == 2:
                    self.bloqueado = True
                    self.tempo_espera = pygame.time.get_ticks() 
    
                break 

    def atualizar(self):

        if self.bloqueado and len(self.cartas_selecionadas) == 2:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_espera >= self.atraso:
                carta1, carta2 = self.cartas_selecionadas
                if carta1.valor == carta2.valor:
                    carta1.combinada = True
                    carta2.combinada = True
                else:
                    carta1.revelada = False
                    carta2.revelada = False

                self.cartas_selecionadas.clear()
                self.bloqueado = False
    
from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    fonte = pygame.font.SysFont("Arial", 40)
    
    # Inicialização do Jogo da Memória
    cartas = criar_tabuleiro()
    selecionadas = []
    aguardando_fechar = False
    tempo_espera = 0
    
    pontos = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)

    while rodando:
        relogio.tick(FPS)
        agora = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            # Lógica de clique (Pessoa 3)
            if evento.type == pygame.MOUSEBUTTONDOWN and not aguardando_fechar:
                for carta in cartas:
                    if carta.rect.collidepoint(evento.pos) and not carta.revelada:
                        carta.revelada = True
                        selecionadas.append(carta)
                        
                        if len(selecionadas) == 2:
                            if verificar_par(selecionadas[0], selecionadas[1]):
                                pontos = calcular_pontos(pontos, 10)
                                selecionadas = []
                                # Verifica se ganhou
                                if all(c.revelada for c in cartas):
                                    if pontos > recorde:
                                        recorde = pontos
                                        salvar_recorde(CAMINHO_RECORDE, recorde)
                            else:
                                # Errou: inicia timer para desvirar (Sua parte de Pessoa 4)
                                aguardando_fechar = True
                                tempo_espera = agora + ATRASO_REVELACAO

        # Lógica de atraso para desvirar as cartas
        if aguardando_fechar and agora >= tempo_espera:
            for carta in selecionadas:
                carta.revelada = False
            selecionadas = []
            aguardando_fechar = False

        # Atualiza o título
        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde}"
        )

        tela.fill(CINZA)

        # Desenha as cartas (Pessoa 2)
        for carta in cartas:
            carta.desenhar(tela, fonte)
            
        # Mensagem se vencer
        if all(c.revelada for c in cartas):
            txt_fim = fonte.render("Você Venceu!", True, PRETO)
            tela.blit(txt_fim, (LARGURA_TELA // 2 - 100, 50))

        pygame.display.flip()

    pygame.quit()