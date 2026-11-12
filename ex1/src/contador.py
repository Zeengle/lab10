import re

def contar_palavras(texto: str) -> dict:
    if not texto:
        return {}
    
    tokens = texto.split()
    resultado = {}
    
    for token in tokens:
        palavra = token.strip(".,;:!?")
        
        if not palavra:
            continue
            
        palavra = palavra.lower()
        resultado[palavra] = resultado.get(palavra, 0) + 1
        
    return resultado