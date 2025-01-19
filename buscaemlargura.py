class Estado:
    def __init__(self, n):
        self.n = n


def estadoInicial():
    return Estado(1)

def mostraEstado(s):
    print(s.n)

def expand(s):
    if s.n >= 4:
        return []
    ret = []
    ret.append(Estado(2*s.n))
    ret.append(Estado(2*s.n + 1))
    return ret

fila = []

def filaEstaVazia():
    return len(fila) == 0

def enfileirar(s):
    fila.append(s)

def desenfileirar():
    ret = fila[0]
    del fila[0]
    return ret


s = estadoInicial()

enfileirar(s)

while not filaEstaVazia():
    atual = desenfileirar()
    mostraEstado(atual)
    filhos = expand(atual)
    for filho in filhos:
        enfileirar(filho)