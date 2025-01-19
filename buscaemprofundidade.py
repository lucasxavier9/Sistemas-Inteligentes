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
    ret.append(Estado(2*s.n + 1))
    ret.append(Estado(2*s.n))
    return ret

def pilhaEstaVazia():
    return len(pilha) == 0


pilha = []

def push(s):
    pilha.append(s)

def pop():
    return pilha.pop()


s = estadoInicial()

push(s)

while not pilhaEstaVazia():
    atual = pop()
    mostraEstado(atual)
    filhos = expand(atual)
    for filho in filhos:
        push(filho)