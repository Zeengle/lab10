class Fila:
    def __init__(self):
        self.normais = []
        self.prioritarias = []
        self.contador_normal = 0
        self.contador_prioritaria = 0
        self.prioritarias_seguidas = 0

    def aguardando(self):
        return len(self.normais) + len(self.prioritarias)

    def emitir(self, tipo):
        if tipo == "normal":
            self.contador_normal += 1
            senha = f"N{self.contador_normal}"
            self.normais.append(senha)
            return senha
        elif tipo == "prioritaria":
            self.contador_prioritaria += 1
            senha = f"P{self.contador_prioritaria}"
            self.prioritarias.append(senha)
            return senha
        else:
            raise ValueError(f"Tipo de senha inválido: {tipo}")

    def chamar(self):
        if self.aguardando() == 0:
            raise IndexError("Fila vazia")

        if self.prioritarias_seguidas >= 2 and len(self.normais) > 0:
            self.prioritarias_seguidas = 0
            return self.normais.pop(0)

        if len(self.prioritarias) > 0:
            self.prioritarias_seguidas += 1
            return self.prioritarias.pop(0)

        self.prioritarias_seguidas = 0
        return self.normais.pop(0)