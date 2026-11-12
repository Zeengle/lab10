CUPONS = {
    "DEZ": (10, 10000),
    "VINTE": (20, 30000)
}

class Carrinho:
    def __init__(self):
        self._subtotal = 0
        self._desconto_porcentagem = 0
        self._subtotal_minimo = 0

    def adicionar(self, preco, quantidade=1):
        if preco <= 0:
            raise ValueError("preco deve ser positivo")
        if not isinstance(quantidade, int) or quantidade < 1:
            raise ValueError("quantidade deve ser inteira e ao menos 1")
        self._subtotal += preco * quantidade

    def aplicar_cupom(self, codigo):
        if codigo not in CUPONS:
            raise ValueError("cupom desconhecido")
        self._desconto_porcentagem, self._subtotal_minimo = CUPONS[codigo]

    @property
    def total(self):
        if self._subtotal >= self._subtotal_minimo:
            desconto = self._desconto_porcentagem
        else:
            desconto = 0
            
        return self._subtotal * (100 - desconto) // 100