import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    PRETO,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
    ATRASO_REVELACAO
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    verificar_par
)

from src.sprites import (
    criar_tabuleiro,
    pegar_sprite
)

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
    
    cartas = criar_tabuleiro()
    selecionadas = []
    aguardando_fechar = False
    tempo_espera = 0
    
    pontos = 0
    vidas = 5
    estado_jogo = "JOGANDO" 
    recorde = carregar_recorde(CAMINHO_RECORDE)

    while rodando:
        relogio.tick(FPS)
        agora = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN and not aguardando_fechar and estado_jogo == "JOGANDO":
                for carta in cartas:
                    if carta.rect.collidepoint(evento.pos) and not carta.revelada:
                        carta.revelada = True
                        selecionadas.append(carta)
                        
                        if len(selecionadas) == 2:
                            if verificar_par(selecionadas[0], selecionadas[1]):
                                pontos = calcular_pontos(pontos, 10)
                                selecionadas = []

                                if all(c.revelada for c in cartas):
                                    estado_jogo = "VENCEU"
                                    if pontos > recorde:
                                        recorde = pontos
                                        salvar_recorde(CAMINHO_RECORDE, recorde)
                            else:

                                vidas = tomar_dano(vidas, 1)
                                aguardando_fechar = True
                                tempo_espera = agora + ATRASO_REVELACAO
                                
                                if jogador_perdeu(vidas):
                                    estado_jogo = "PERDEU"
        if aguardando_fechar and agora >= tempo_espera:
            for carta in selecionadas:
                carta.revelada = False
            selecionadas = []
            aguardando_fechar = False
        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Vidas: {vidas} | Recorde: {recorde}"
        )

        tela.fill(CINZA)
        if estado_jogo == "JOGANDO" or aguardando_fechar:
            for carta in cartas:
                carta.desenhar(tela, fonte)
                
        elif estado_jogo == "VENCEU":
            txt_fim = fonte.render("Você Venceu!", True, PRETO)
            tela.blit(txt_fim, (LARGURA_TELA // 2 - 120, ALTURA_TELA // 2 - 20))
            
        elif estado_jogo == "PERDEU":
            txt_derrota = fonte.render("Game Over!", True, (255, 0, 0))
            tela.blit(txt_derrota, (LARGURA_TELA // 2 - 120, ALTURA_TELA // 2 - 20))
        pygame.display.flip()

    pygame.quit()