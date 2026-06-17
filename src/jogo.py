import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    COR_FUNDO,
    PRETO,
    BRANCO,
    VERMELHO,
    CAMINHO_RECORDE,
    ATRASO_REVELACAO,
    TEMPO_PREVIEW
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    tomar_dano,
    verificar_par
)

from src.sprites import (
    criar_tabuleiro
)

from src.dados import (
    salvar_recorde,
    carregar_recorde,
)


def desenhar_interface(tela, fonte, pontos, vidas, recorde):
    """Desenha o HUD (Heads-Up Display) na parte superior."""
    cor_texto = BRANCO
    txt_pontos = fonte.render(f"Pontos: {pontos}", True, cor_texto)
    txt_vidas = fonte.render(f"Vidas: {vidas}", True, cor_texto)
    txt_recorde = fonte.render(f"Recorde: {recorde}", True, cor_texto)
    
    tela.blit(txt_pontos, (50, 20))
    tela.blit(txt_recorde, (LARGURA_TELA // 2 - txt_recorde.get_width() // 2, 20))
    tela.blit(txt_vidas, (LARGURA_TELA - 150, 20))


def executar_jogo():
    pygame.init()
    
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    fonte = pygame.font.SysFont("Arial Black", 30)
    fonte_grande = pygame.font.SysFont("Arial Black", 60)
    
    cartas = criar_tabuleiro()
    selecionadas = []
    aguardando_fechar = False
    tempo_espera = 0
    
    # Estado de preview inicial
    tempo_inicio = pygame.time.get_ticks()
    estado_jogo = "PREVIEW" 
    
    pontos = 0
    vidas = 5
    recorde = carregar_recorde(CAMINHO_RECORDE)

    while rodando:
        relogio.tick(FPS)
        agora = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            # Pular preview com um clique
            if evento.type == pygame.MOUSEBUTTONDOWN and estado_jogo == "PREVIEW":
                estado_jogo = "JOGANDO"
                for carta in cartas:
                    carta.revelada = False

            if evento.type == pygame.MOUSEBUTTONDOWN and not aguardando_fechar and estado_jogo == "JOGANDO":
                for carta in cartas:
                    if carta.rect.collidepoint(evento.pos) and not carta.revelada:
                        carta.revelada = True
                        selecionadas.append(carta)
                        
                        if len(selecionadas) == 2:
                            if verificar_par(selecionadas[0], selecionadas[1]):
                                pontos = calcular_pontos(pontos, 10)
                                selecionadas[0].encontrada = True # Marca a primeira carta como encontrada
                                selecionadas[1].encontrada = True # Marca a segunda carta como encontrada
                                selecionadas = []

                                if all(c.encontrada for c in cartas): # Verifica se todas as cartas foram encontradas
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

        # Lógica do Preview: Revela as cartas por um tempo e depois as esconde
        if estado_jogo == "PREVIEW":
            for carta in cartas:
                carta.revelada = True
            if agora - tempo_inicio > TEMPO_PREVIEW:
                estado_jogo = "JOGANDO"
                for carta in cartas:
                    carta.revelada = False

        tela.fill(COR_FUNDO)
        desenhar_interface(tela, fonte, pontos, vidas, recorde)

        if estado_jogo in ["JOGANDO", "PREVIEW"] or aguardando_fechar:
            for carta in cartas:
                carta.desenhar(tela, fonte)
                
        elif estado_jogo == "VENCEU":
            txt_fim = fonte_grande.render("Você Venceu!", True, BRANCO)
            tela.blit(txt_fim, (LARGURA_TELA // 2 - txt_fim.get_width() // 2, ALTURA_TELA // 2 - 30))
            
        elif estado_jogo == "PERDEU":
            txt_derrota = fonte_grande.render("Game Over!", True, VERMELHO)
            tela.blit(txt_derrota, (LARGURA_TELA // 2 - txt_derrota.get_width() // 2, ALTURA_TELA // 2 - 30))
        pygame.display.flip()

    pygame.quit()