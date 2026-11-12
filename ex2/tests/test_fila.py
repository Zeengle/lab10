from fila import Fila

def test_fila_vazia_inicial():
    fila = Fila()
    assert fila.aguardando() == 0