def contar_palavras(texto: str) -> dict:
    if not texto:
        return {}
    tokens = texto.split()
    if not tokens:
        return {}

    resultado = {}
    for token in tokens:
        palavra = token.strip(".,;:!?").lower()

        if not palavra:
            continue
            
        resultado[palavra] = resultado.get(palavra, 0) + 1
    return resultado