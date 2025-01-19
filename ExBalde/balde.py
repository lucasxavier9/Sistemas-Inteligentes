class Estado:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

def exibe(estado):
    print(f'V1: {estado.v1} V2: {estado.v2}')

def estado_inicial():
    return Estado(0,0)

def estado_objetivo(estado):
    return estado.v1 + estado.v2 == 3

def encher_1(estado):
    return Estado(5,estado.v2)

def encher_2(estado):
    return Estado(estado.v1, 4)

def esvaziar_1(estado):
    return Estado(0, estado.v2)


def esvaziar_2(estado):
    return Estado(estado.v1, 0)

def transferir_1p2(estado):
    transf = 4 - estado.v2
    if(estado.v1 <= transf):
        transf = estado.v1
    return Estado(estado.v1 - transf, estado.v2 + transf)

def transferir_2p1(estado):
    transf = 5 - estado.v1
    if(estado.v2 <= transf):
        transf = estado.v2
    return Estado(estado.v1 + transf, estado.v2 - transf)

def expande(estado):
    filhos = []
    filhos.append(encher_1(estado))
    filhos.append(encher_2(estado))
    filhos.append(esvaziar_1(estado))
    filhos.append(esvaziar_2(estado))
    filhos.append(transferir_1p2(estado))
    filhos.append(transferir_2p1(estado))
    return filhos
