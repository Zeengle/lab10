from fila import Fila

def test_fila_vazia_inicial():
    fila = Fila()
    assert fila.aguardando() == 0

def test_emitir_senha_normal():
    fila = Fila()
    senha = fila.emitir("normal")
    assert senha == "N1"
    assert fila.aguardando() == 1