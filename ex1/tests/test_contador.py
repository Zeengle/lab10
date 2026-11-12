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


'''
Questoes:

c) Mostre o git log --oneline. Algum GREEN: veio sem um RED:
antes?
    R: 6abdbf7 (HEAD -> main) GREEN: valida suporte nativo do split a quebras de linha e espacos
b449f7a GREEN: confirma suporte a hifen interno
2d3f4de GREEN: remove pontuacao das bordas das palavras
33224d2 RED: adiciona teste para case insensitive com repeticao
35ac7f0 GREEN: retorna contagem para palavra unica
f4f44e6 RED: adiciona teste para palavra unica
ffc8a52 GREEN: IGNORA STRINGS COMPOSTAS APENAS DE PONTUACAO
f9dd6a0 GREEN: Implementa testo apenas pontuacao
bb1ef1d GREEN: implementa retorno para texto vazio
757c22a RED: texto vazio devolve dicionario vazio
540f446 GREEN: Implementa suporte a hífen interno
bb04927 (origin/main, origin/HEAD) Initial commit

d) Quais testes passaram na primeira execução? Explique por que e diga
se eles ficam na suíte.
    R: hifen interno, texto so de pontuacao, suporte hifen interno e suporte de split e quebras de linhas e espacos.

e) Meça a cobertura de ramos e o escore de mutação da suíte final
    R: 16 Mutantes mortos, 2 mutantes sobreviventes. 89% de Score de mutação.

'''