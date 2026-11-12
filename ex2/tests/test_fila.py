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

def test_ordem_atendimento_prioritaria_frente():
    fila = Fila()
    fila.emitir("normal")
    fila.emitir("prioritaria")
    fila.emitir("normal")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "N1"
    assert fila.chamar() == "N2"

def test_limite_duas_prioritarias_chama_normal():
    fila = Fila()
    fila.emitir("normal")
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"
    assert fila.chamar() == "N1"
    assert fila.chamar() == "P3"

def test_limite_duas_prioritarias_ignorado_sem_normal():
    fila = Fila()
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"
    assert fila.chamar() == "P3"

def test_zerar_contagem_prioritarias_apos_normal():
    fila = Fila()
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")
    fila.emitir("normal")
    fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"
    assert fila.chamar() == "N1"
    assert fila.chamar() == "P3"


'''
Questoes: 

c) Qual teste obrigou a contar as prioritárias seguidas? Qual obrigou a
zerar a contagem?
    R: O test_limite_duas_prioridades_chama_normal obrigou a introdzir uma variavel de controle de contagem no codigo de produção.
    O teste test_zerar_contagem_prioritarias_apos_normal obrigou a garantir que o contador fosse rersetado para zero assim que a senha fosse atendida.

d) Que teste mostra que o limite de 2 não vale quando nenhuma normal
espera?
    R: o teste: test_limite_duas_prioritarias_ignorado_sem_normal.
    
e) Rode o mutmut. Os mutantes vivos indicam algum comportamento da
especificação sem teste?
    R: 45 Mutantes mortos e 7 mutantes vivos. Não necessariamente, pode ser uma falha de asserção sobre detalhes secundarios ou redundancia logica.
'''
