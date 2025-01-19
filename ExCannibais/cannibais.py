class Estado:
    def __init__(self, ce, me, cd, md, barco):
        self.ce = ce
        self.ce = cd
        self.me = me
        self.md = md
        self.barco = barco
        

def exibe(estado):
    barco = "* "
    if(estado.barco == 0):
        print(f' {estado.ce} {estado.me}, | {barco} |, {estado.cd}, {estado.md}')

def estado_inicial():
    return Estado(3,3,0,0,0)

def estado_objetivo(estado):
    return estado.ce == 3 and estado.me == 3

def valido(estado):
    if(estado.me > 0):
        if(estado.ce > estado.me):
            return False
        
        if(estado.md > 0):
            if(estado.cd > estado.md):
                return False

        return True
    
def transfere (estado, qtd_canibais, qtd_missionarios):
    #se o barco estiver na direita
    if(estado.barco == 0):
        qtd_canibais = -qtd_canibais
        qtd_missionarios = -qtd_missionarios

    me = estado.me - qtd_missionarios
    ce = estado.ce - qtd_canibais
    md = estado.md + qtd_missionarios
    cd = estado.cd + qtd_canibais

    return Estado(me, ce, md ,cd, 1 - estado.barco)


def transfere_1_cannibal(estado):
    return transfere(estado, 1, 0)


def transfere_1_missionario(estado):
    return transfere(estado, 0, 1)

def transfere_2_cannibais(estado):
    return transfere(estado, 2, 0)

def transfere_2_missionarios(estado):
    return transfere(estado, 0, 2)

def transfere_1_cannibal_1_missionario(estado):
    return transfere(estado, 1, 1)

def expande(estado):
    filhos = []
    filho = transfere_1_cannibal(estado)
    if (valido(filho)):
        filhos.append(filho)

        filho = transfere_1_missionario(estado)
    if (valido(filho)):
        filhos.append(filho)

        filho = transfere_2_cannibais(estado)
    if (valido(filho)):
        filhos.append(filho)

        filho = transfere_2_missionarios(estado)
    if (valido(filho)):
        filhos.append(filho)

        filho = transfere_1_cannibal_1_missionario(estado)
    if (valido(filho)):
        filhos.append(filho)
    
    return filhos

