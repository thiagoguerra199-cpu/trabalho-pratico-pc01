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
    """Desenha as informações de texto (HUD) no topo da tela (Pontos, Recorde, Vidas e Tempo)."""
    cor_texto = BRANCO
    txt_pontos = fonte.render(f"Pontos: {pontos}", True, cor_texto)
    txt_vidas = fonte.render(f"Vidas: {vidas}", True, cor_texto)
    txt_recorde = fonte.render(f"Recorde: {recorde}", True, cor_texto)
    txt_tempo = fonte.render(f"Tempo: {tempo}s", True, cor_texto)
    
    # Posicionamento ajustado para não colidir com as cartas
    tela.blit(txt_pontos, (50, 15))
    tela.blit(txt_recorde, (LARGURA_TELA // 2 - txt_recorde.get_width() // 2, 15))
    tela.blit(txt_vidas, (LARGURA_TELA - 180, 15))
    # Exibe o tempo centralizado, um pouco abaixo do recorde
    tela.blit(txt_tempo, (LARGURA_TELA // 2 - txt_tempo.get_width() // 2, 45))


def executar_jogo():
    """Função principal que inicializa o Pygame e gerencia o loop de eventos."""
    pygame.init()
    
    # Configuração da janela
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    # Diminuindo o tamanho da fonte do HUD de 30 para 22
    fonte = pygame.font.SysFont("Arial Black", 22)
    fonte_grande = pygame.font.SysFont("Arial Black", 60)
    
    cartas = criar_tabuleiro()
    selecionadas = []
    aguardando_fechar = False
    tempo_espera = 0
    tempo_decorrido = 0
    
    # Estado de preview inicial
    tempo_inicio = pygame.time.get_ticks()
    tempo_inicio_partida = 0 # Marcará o início real após o preview
    estado_jogo = "PREVIEW" 
    
    # Inicialização das variáveis de progresso (Vidas aumentadas para 8)
    pontos = 0
    vidas = 8
    recorde = carregar_recorde(CAMINHO_RECORDE)

    while rodando:
        # Mantém a taxa de quadros constante e pega o tempo atual
        relogio.tick(FPS)
        agora = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            # Pular preview com um clique
            if evento.type == pygame.MOUSEBUTTONDOWN and estado_jogo == "PREVIEW":
                estado_jogo = "JOGANDO"
                tempo_inicio_partida = pygame.time.get_ticks()
                for carta in cartas:
                    carta.revelada = False

            # Lógica de clique nas cartas durante o jogo
            if evento.type == pygame.MOUSEBUTTONDOWN and not aguardando_fechar and estado_jogo == "JOGANDO":
                for carta in cartas:
                    # Verifica se o clique foi dentro da carta e se ela já não está aberta
                    if carta.rect.collidepoint(evento.pos) and not carta.revelada:
                        carta.revelada = True
                        selecionadas.append(carta)
                        
                        if len(selecionadas) == 2:
                            # Se encontrou um par
                            if verificar_par(selecionadas[0], selecionadas[1]):
                                # Calcula pontos baseados no tempo atual da partida
                                tempo_segundos = (agora - tempo_inicio_partida) // 1000
                                pontos += calcular_pontos(tempo_segundos)
                                selecionadas[0].encontrada = True # Marca a primeira carta como encontrada
                                selecionadas[1].encontrada = True # Marca a segunda carta como encontrada
                                selecionadas = []

                                # Verifica se todas as cartas do tabuleiro foram achadas
                                if all(c.encontrada for c in cartas): # Verifica se todas as cartas foram encontradas
                                    estado_jogo = "VENCEU"
                                    if pontos > recorde:
                                        recorde = pontos
                                        salvar_recorde(CAMINHO_RECORDE, recorde)
                            else:
                                # Se errou o par, perde vida e inicia tempo para fechar as cartas
                                vidas = tomar_dano(vidas, 1)
                                aguardando_fechar = True
                                tempo_espera = agora + ATRASO_REVELACAO
                                
                                if jogador_perdeu(vidas):
                                    estado_jogo = "PERDEU"
        # Fecha as cartas selecionadas após o tempo de erro passar
        if aguardando_fechar and agora >= tempo_espera:
            for carta in selecionadas:
                carta.revelada = False
            selecionadas = []
            aguardando_fechar = False
        pygame.display.set_caption(TITULO_JOGO) # Título da janela mais limpo

        # Lógica do Preview: Revela as cartas por um tempo e depois as esconde
        if estado_jogo == "PREVIEW":
            for carta in cartas:
                carta.revelada = True
            if agora - tempo_inicio > TEMPO_PREVIEW:
                estado_jogo = "JOGANDO"
                tempo_inicio_partida = pygame.time.get_ticks()
                for carta in cartas:
                    carta.revelada = False

        # Atualiza o cronômetro apenas enquanto o jogador estiver jogando
        if estado_jogo == "JOGANDO" or aguardando_fechar:
            tempo_decorrido = (agora - tempo_inicio_partida) // 1000

        # --- DESENHO NA TELA ---
        tela.fill(COR_FUNDO)
        desenhar_interface(tela, fonte, pontos, vidas, recorde, tempo_decorrido)

        # Desenha as cartas se o jogo estiver ativo ou em modo de visualização
        if estado_jogo in ["JOGANDO", "PREVIEW"] or aguardando_fechar:
            for carta in cartas:
                carta.desenhar(tela, fonte)
        
        # Telas de fim de jogo
        elif estado_jogo == "VENCEU":
            txt_fim = fonte_grande.render("Você Venceu!", True, BRANCO)
            tela.blit(txt_fim, (LARGURA_TELA // 2 - txt_fim.get_width() // 2, ALTURA_TELA // 2 - 30))
            
        elif estado_jogo == "PERDEU":
            txt_derrota = fonte_grande.render("Game Over!", True, VERMELHO)
            tela.blit(txt_derrota, (LARGURA_TELA // 2 - txt_derrota.get_width() // 2, ALTURA_TELA // 2 - 30))
        pygame.display.flip()

    pygame.quit()