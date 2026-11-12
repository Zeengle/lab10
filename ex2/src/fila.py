class Fila:
    def __init__(self):
        self.normais = []
        self.prioritarias = []

    def aguardando(self) -> int:
        return len(self.normais) + len(self.prioritarias)

    def emitir(self, tipo):
        if tipo == "normal":
            self.normais.append(1)
            return f"N{len(self.normais)}"