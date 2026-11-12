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

def test_espacos_e_quebras_de_linha():
    assert contar_palavras("bom\ndia") == {"bom": 1, "dia": 1}
    assert contar_palavras("Três espaços entre bom e dia dão dois itens") == {
        "três": 1, "espaços": 1, "entre": 1, "bom": 1, 
        "e": 1, "dia": 1, "dão": 1, "dois": 1, "itens": 1
    }