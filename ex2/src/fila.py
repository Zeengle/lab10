class Fila:
    def __init__(self):
        self.normais = []
        self.prioritarias = []

    def aguardando(self) -> int:
        return len(self.normais) + len(self.prioritarias)