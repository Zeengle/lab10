from contador import contar_palavras

def test_texto_vazio():
    assert contar_palavras("") == {}

def test_apenas_pontuacao():
    assert contar_palavras("... !") == {}

def test_palavra_unica():
    assert contar_palavras("teste") == {"teste": 1}