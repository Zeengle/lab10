def contar_palavras(texto: str) -> dict:
    if not texto or not texto.strip(".,;:!? "):
        return {}
    return {texto: 1}