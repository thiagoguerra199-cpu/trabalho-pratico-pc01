from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor, verificar_par


def test_calcular_pontos_rapido():
    """Deve retornar pontuação máxima (100) quando o tempo for 0."""
    assert calcular_pontos(0) == 100

def test_calcular_pontos_lento():
    """Deve retornar a pontuação mínima (10) quando o jogador demorar muito."""
    assert calcular_pontos(100) == 10


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50

def test_verificar_par_sucesso():
    """Deve retornar True quando as cores forem iguais."""
    class MockCarta: cor = "A"
    c1, c2 = MockCarta(), MockCarta()
    assert verificar_par(c1, c2) is True

def test_verificar_par_falha():
    """Deve retornar False quando as cores forem diferentes."""
    class MockCarta1: cor = "A"
    class MockCarta2: cor = "B"
    assert verificar_par(MockCarta1(), MockCarta2()) is False