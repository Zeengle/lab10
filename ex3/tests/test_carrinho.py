import pytest
from src.carrinho import Carrinho

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








'''
Questoes:

a) Quais testes atuais contradizem as regras? O que fazer com eles antes
de mudar o código?
    R: o cupom "DEZ" funcionava para qualquer valor. Agora, com a regra nova, o cupom "DEZ" so aplica desconto se o subtotal for >= 10000. Alem disso, ganhamos a regra de quantidade inteira e >= 1.
'''