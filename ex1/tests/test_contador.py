from contador import contar_palavras

def test_texto_vazio():
    assert contar_palavras("") == {}

def test_apenas_pontuacao():
    assert contar_palavras("... !") == {}

def test_palavra_unica():
    assert contar_palavras("teste") == {"teste": 1}

def test_case_insensitive():
    assert contar_palavras("Dia dia DIA") == {"dia": 3}

def test_hifen_interno():
    assert contar_palavras("guarda-chuva") == {"guarda-chuva": 1}

