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

c) No Refactor, guarde a porcentagem e o mínimo juntos em CUPONS. O
que mostra que nada mudou?
    R: O que prova que nada foi quebrado durante a refatoração é a suíte completa de testes unitários passando em verde (pytest).

d) Que valores de quantidade você testou? Por quê?
    R: quantidade 0 e -1, lançando ValueError conforme exigido pela nova regra
    quantidade 1.5 = verificar a restrição de que a quantidade deve estritamente um numero inteiro
    quantidade 1 = valroes maiores implicitos nos calculos
'''