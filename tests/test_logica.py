from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor, verificar_par


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


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
    """Deve retornar True quando os emojis forem iguais."""
    class MockCarta: emoji = "A"
    c1, c2 = MockCarta(), MockCarta()
    assert verificar_par(c1, c2) is True

def test_verificar_par_falha():
    """Deve retornar False quando os emojis forem diferentes."""
    class MockCarta1: emoji = "A"
    class MockCarta2: emoji = "B"
    assert verificar_par(MockCarta1(), MockCarta2()) is False