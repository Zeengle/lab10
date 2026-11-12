from fila import Fila
import pytest

def test_fila_vazia_inicial():
    fila = Fila()
    assert fila.aguardando() == 0

def test_emitir_senha_normal():
    fila = Fila()
    senha = fila.emitir("normal")
    assert senha == "N1"
    assert fila.aguardando() == 1

def test_emitir_senhas_normais_sequenciais():
    fila = Fila()
    assert fila.emitir("normal") == "N1"
    assert fila.emitir("normal") == "N2"
    assert fila.emitir("normal") == "N3"
    assert fila.aguardando() == 3

def test_emitir_senha_prioritaria():
    fila = Fila()
    senha = fila.emitir("prioritaria")
    assert senha == "P1"
    assert fila.aguardando() == 1

def test_emitir_tipo_invalido():
    fila = Fila()
    with pytest.raises(ValueError):
        fila.emitir("vip")

def test_chamar_fila_vazia():
    fila = Fila()
    with pytest.raises(IndexError):
        fila.chamar()