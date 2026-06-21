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


def desenhar_interface(tela, fonte, pontos, vidas, recorde, tempo):
    """Desenha as informações de texto (HUD) no topo da tela com estilo elegante."""
    barra_altura = 70
    pygame.draw.rect(tela, (20, 35, 60), (0, 0, LARGURA_TELA, barra_altura))
    pygame.draw.line(tela, BRANCO, (0, barra_altura), (LARGURA_TELA, barra_altura), 2)
    
    cor_texto = BRANCO
    cor_destaque = (52, 211, 153)
    
    txt_pontos = fonte.render(f"Pontos: {pontos}", True, cor_destaque)
    txt_vidas = fonte.render(f"Vidas: {vidas}", True, cor_texto)
    txt_recorde = fonte.render(f"Recorde: {recorde}", True, cor_destaque)
    txt_tempo = fonte.render(f"Tempo: {tempo}s", True, cor_texto)
    
    tela.blit(txt_pontos, (30, 12))
    tela.blit(txt_recorde, (30, 40))
    tela.blit(txt_tempo, (LARGURA_TELA // 2 - txt_tempo.get_width() // 2, 25))
    tela.blit(txt_vidas, (LARGURA_TELA - txt_vidas.get_width() - 30, 25))


def executar_jogo():
    """Função principal que inicializa o Pygame e gerencia o loop de eventos."""
    pygame.init()
    
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    fonte = pygame.font.SysFont("Segoe UI", 20, bold=True)
    fonte_grande = pygame.font.SysFont("Segoe UI", 70, bold=True)
    
    cartas = criar_tabuleiro()
    selecionadas = []
    aguardando_fechar = False
    tempo_espera = 0
    tempo_decorrido = 0
    
    tempo_inicio = pygame.time.get_ticks()
    tempo_inicio_partida = 0
    estado_jogo = "PREVIEW" 
    
    pontos = 0
    vidas = 8
    recorde = carregar_recorde(CAMINHO_RECORDE)

    while rodando:
        relogio.tick(FPS)
        agora = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN and estado_jogo == "PREVIEW":
                estado_jogo = "JOGANDO"
                tempo_inicio_partida = pygame.time.get_ticks()
                for carta in cartas:
                    carta.revelada = False

            # Lógica de clique nas cartas durante o jogo
            if evento.type == pygame.MOUSEBUTTONDOWN and not aguardando_fechar and estado_jogo == "JOGANDO":
                for carta in cartas:
                    if carta.rect.collidepoint(evento.pos) and not carta.revelada:
                        carta.revelada = True
                        selecionadas.append(carta)
                        
                        if len(selecionadas) == 2:
                            if verificar_par(selecionadas[0], selecionadas[1]):
                                tempo_segundos = (agora - tempo_inicio_partida) // 1000
                                pontos += calcular_pontos(tempo_segundos)
                                selecionadas[0].encontrada = True
                                selecionadas[1].encontrada = True
                                selecionadas = []

                                if all(c.encontrada for c in cartas):
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
        
        pygame.display.set_caption(TITULO_JOGO)

        if estado_jogo == "PREVIEW":
            for carta in cartas:
                carta.revelada = True
            if agora - tempo_inicio > TEMPO_PREVIEW:
                estado_jogo = "JOGANDO"
                tempo_inicio_partida = pygame.time.get_ticks()
                for carta in cartas:
                    carta.revelada = False

        if estado_jogo == "JOGANDO" or aguardando_fechar:
            tempo_decorrido = (agora - tempo_inicio_partida) // 1000

        tela.fill(COR_FUNDO)
        desenhar_interface(tela, fonte, pontos, vidas, recorde, tempo_decorrido)

        if estado_jogo in ["JOGANDO", "PREVIEW"] or aguardando_fechar:
            for carta in cartas:
                carta.desenhar(tela, fonte)
        
        elif estado_jogo == "VENCEU":
            fundo_overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
            fundo_overlay.set_alpha(200)
            fundo_overlay.fill((20, 35, 60))
            tela.blit(fundo_overlay, (0, 0))
            
            txt_fim = fonte_grande.render("Você Venceu!", True, (52, 211, 153))
            tela.blit(txt_fim, (LARGURA_TELA // 2 - txt_fim.get_width() // 2, ALTURA_TELA // 2 - 80))
            
            txt_pontos_final = pygame.font.SysFont("Segoe UI", 40, bold=True).render(f"Pontuação: {pontos}", True, BRANCO)
            tela.blit(txt_pontos_final, (LARGURA_TELA // 2 - txt_pontos_final.get_width() // 2, ALTURA_TELA // 2 + 20))
            
        elif estado_jogo == "PERDEU":
            fundo_overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
            fundo_overlay.set_alpha(200)
            fundo_overlay.fill((60, 20, 20))
            tela.blit(fundo_overlay, (0, 0))
            
            txt_derrota = fonte_grande.render("Game Over!", True, VERMELHO)
            tela.blit(txt_derrota, (LARGURA_TELA // 2 - txt_derrota.get_width() // 2, ALTURA_TELA // 2 - 80))
            
            txt_pontos_final = pygame.font.SysFont("Segoe UI", 40, bold=True).render(f"Pontuação: {pontos}", True, BRANCO)
            tela.blit(txt_pontos_final, (LARGURA_TELA // 2 - txt_pontos_final.get_width() // 2, ALTURA_TELA // 2 + 20))
        pygame.display.flip()

    pygame.quit()