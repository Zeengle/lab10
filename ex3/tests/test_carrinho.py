import pytest
from carrinho import Carrinho

def test_adicionar_quantidade_invalida():
    carrinho = Carrinho()
    with pytest.raises(ValueError):
        carrinho.adicionar(100, quantidade=0)
        
    with pytest.raises(ValueError):
        carrinho.adicionar(100, quantidade=-1)

def test_adicionar_quantidade_nao_inteira():
    carrinho = Carrinho()
    with pytest.raises(ValueError):
        carrinho.adicionar(100, quantidade=1.5)

def test_cupom_dez_abaixo_do_minimo_nao_da_desconto():
    carrinho = Carrinho()
    carrinho.adicionar(5000)
    carrinho.aplicar_cupom("DEZ")
    assert carrinho.total == 5000

def test_cupom_dez_atinge_minimo():
    carrinho = Carrinho()
    carrinho.adicionar(10000)
    carrinho.aplicar_cupom("DEZ")
    assert carrinho.total == 9000

def test_cupom_vinte_atinge_minimo():
    carrinho = Carrinho()
    carrinho.adicionar(30000)
    carrinho.aplicar_cupom("VINTE")
    assert carrinho.total == 24000


def test_segundo_cupom_substitui_primeiro():
    carrinho = Carrinho()
    carrinho.adicionar(30000)
    
    carrinho.aplicar_cupom("DEZ")
    carrinho.aplicar_cupom("VINTE")
    assert carrinho.total == 24000




'''
Questoes:

a) Quais testes atuais contradizem as regras? O que fazer com eles antes
de mudar o código?
    R: o cupom "DEZ" funcionava para qualquer valor. Agora, com a regra nova, o cupom "DEZ" so aplica desconto se o subtotal for >= 10000. Alem disso, ganhamos a regra de quantidade inteira e >= 1.
'''