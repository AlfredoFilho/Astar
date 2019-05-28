def funcaoH(pai, saida) :
    diference = saida[1] - pai [1] # Diferenca de colunas
    if(pai[0] == saida[0]) :
        return abs(diference)

    if(pai[0] % 2 == 1) : # Caso o pai estiver em linha ímpar
        if(abs(pai[0] - saida[0]) == 1) : # Diferenca de 1 linha
            if(diference <= 0) :
                return abs(diference) + 1
            else :
                return abs(diference)
            
        if(abs(pai[0] - saida[0]) == 2) : # Diferenca de 2 linhas
            if(diference == 0) :
                return 2
            else :
                return abs(diference) + 1
            
        if(abs(pai[0] - saida[0]) == 3) : # Diferenca de 3 linhas
            if(diference >= -1 and diference <= 2) :
                return 3
            elif(diference > 0) :
                return abs(diference) + 1
            elif(diference < 0) :
                return abs(diference) + 2
               
        if(abs(pai[0] - saida[0]) == 4) : # Diferenca de 4 linhas
            if(diference >= -2 and diference <= 2) :
                return 4
            else :
                return abs(diference) + 2
           
        if(abs(pai[0] - saida[0]) == 5) : # Diferenca de 5 linhas
            if(diference >= -2 and diference <= 3) :
                return 5
            elif(diference > 0) :
                return abs(diference) + 2
            elif(diference < 0) :
                return abs(diference) + 3
           
        if(abs(pai[0] - saida[0]) == 6) : # Diferenca de 6 linhas
            if(diference >= -3 and diference <= 3) :
                return 6
            else :
                return abs(diference) + 3
            
        if(abs(pai[0] - saida[0]) == 7) : # Diferenca de 7 linhas
            if(diference >= -3 and diference <= 4) :
                return 7
            elif(diference > 0) :
                return abs(diference) + 3
            elif(diference < 0) :
                return abs(diference) + 4
           
        if(abs(pai[0] - saida[0]) == 8) : # Diferenca de 8 linhas
            if(diference >= -4 and diference <= 4) :
                return 8
            else :
                return abs(diference) + 4
            
        if(abs(pai[0] - saida[0]) == 9) : # Diferenca de 9 linhas
            if(diference >= -4 and diference <= 5) :
                return 9
            elif(diference > 0) :
                return abs(diference) + 4
            elif(diference < 0) :
                return abs(diference) + 5
           
    else : # Caso o pai estiver em linha par
        if(abs(pai[0] - saida[0]) == 1) : # Diferenca de 1 linha
            if(diference >= 0) :
                return abs(diference) + 1
            else :
                return abs(diference)
            
        if(abs(pai[0] - saida[0]) == 2) : # Diferenca de 2 linhas
            if(diference == 0) :
                return 2
            else :
                return abs(diference) + 1
            
        if(abs(pai[0] - saida[0]) == 3) : # Diferenca de 3 linhas
            if(diference >= -2 and diference <= 1) :
                return 3
            elif(diference > 0) :
                return abs(diference) + 2
            elif(diference < 0) :
                return abs(diference) + 1
               
        if(abs(pai[0] - saida[0]) == 4) : # Diferenca de 4 linhas
            if(diference >= -2 and diference <= 2) :
                return 4
            else :
                return abs(diference) + 2
           
        if(abs(pai[0] - saida[0]) == 5) : # Diferenca de 5 linhas
            if(diference >= -3 and diference <= 2) :
                return 5
            elif(diference > 0) :
                return abs(diference) + 3
            elif(diference < 0) :
                return abs(diference) + 2
           
        if(abs(pai[0] - saida[0]) == 6) : # Diferenca de 6 linhas
            if(diference >= -3 and diference <= 3) :
                return 6
            else :
                return abs(diference) + 3
            
        if(abs(pai[0] - saida[0]) == 7) : # Diferenca de 7 linhas
            if(diference >= -4 and diference <= 3) :
                return 7
            elif(diference > 0) :
                return abs(diference) + 4
            elif(diference < 0) :
                return abs(diference) + 3
           
        if(abs(pai[0] - saida[0]) == 8) : # Diferenca de 8 linhas
            if(diference >= -4 and diference <= 4) :
                return 8
            else :
                return abs(diference) + 4
            
        if(abs(pai[0] - saida[0]) == 9) : # Diferenca de 9 linhas
            if(diference >= -5 and diference <= 4) :
                return 9
            elif(diference > 0) :
                return abs(diference) + 5
            elif(diference < 0) :
                return abs(diference) + 4
           
        if(abs(pai[0] - saida[0]) == 10) : # Diferenca de 10 linhas
            if(diference >= -5 and diference <= 5) :
                return 10
            else :
                return abs(diference) + 5

def funcaoG(inicio, atual, listaFechada) :
    G = 0
    aux = True
    lista = []
    while aux:
        for struct in listaFechada:
            if struct.coordenada == atual:
                atual = struct.caminho
                G = G + 1
                if volta == inicio:
                    aux = False
    return G