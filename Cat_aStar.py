# -*- coding: utf-8 -*-
'''
*******************Developed by********************************
    
Alfredo Albélis Batista Filho - https://github.com/AlfredoFilho
Brenda Alexsandra Januário - https://github.com/brendajanuario
Cléofas Peres Santos -  https://github.com/CleoPeres
Leonardo Ferrari - https://github.com/LeonardoFerrari
Pedro Bernini - https://github.com/PedroBernini
Vinicius Abrantes - https://github.com/viniciusAbrantes

**************************************************************** 
'''

from dataclasses import dataclass
import Calcular
import GifMaker
import os

tabuleiro = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10),
             (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
             (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
             (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10),
             (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10),
             (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10),
             (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10),
             (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10),
             (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10),
             (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10),
             (10,0), (10,1), (10,2), (10,3), (10,4), (10,5), (10,6), (10,7), (10,8), (10,9), (10,10)]

dark_green = "#4a8e52"
light_green = "#61b76b"

@dataclass
class no:
    def __init__(self, coordenadaenada, total_F, distanciaComeco_G, distanciaAteFinal_H, pai):
        self.coordenadaenada = coordenadaenada
        self.total_F = total_F
        self.distanciaComeco_G = distanciaComeco_G
        self.distanciaAteFinal_H = distanciaAteFinal_H
        self.pai = pai

estadoInicial = (5, 5)

estadoFinal = (10, 10)

bloqueados = [(9, 7), (9, 8), (9, 9), (9, 10)]

def expandirEmVolta(estadoInicial, estadoEscolhido, listaAberta, listaFechada, images, bloqueados, estadoFinal):
    # lista com as nos inicias em volta do pai
    listaExpansaoSuja = []
    
    #Lista expansao limpa (sem bloqueados e dentro do tabuleiro)
    listaExpansao = []
    
    if estadoEscolhido[0] % 2 != 0: #Se a linha do gato for par
        listaExpansaoSuja = [(estadoEscolhido[0], estadoEscolhido[1] + 1),      #Leste
                             (estadoEscolhido[0] + 1, estadoEscolhido[1] + 1),  #Sudeste
                             (estadoEscolhido[0] + 1, estadoEscolhido[1]),      #Sudoeste
                             (estadoEscolhido[0], estadoEscolhido[1] - 1),      #Oeste
                             (estadoEscolhido[0] - 1, estadoEscolhido[1]),      #Noroeste
                             (estadoEscolhido[0] - 1, estadoEscolhido[1] + 1)]  #Nordeste
    else:
        listaExpansaoSuja = [(estadoEscolhido[0], estadoEscolhido[1] + 1),      #Leste
                             (estadoEscolhido[0] + 1, estadoEscolhido[1]),      #Sudeste
                             (estadoEscolhido[0] + 1, estadoEscolhido[1] - 1),  #Sudoeste
                             (estadoEscolhido[0], estadoEscolhido[1] - 1),      #Oeste
                             (estadoEscolhido[0] - 1, estadoEscolhido[1] - 1),  #Noroeste
                             (estadoEscolhido[0] - 1, estadoEscolhido[1])]      #Nordeste
    
    
    #Retirar da lista suja bloqueados e fora do tabuleiro
    for coordenada in listaExpansaoSuja:
        valido = True
        if coordenada not in bloqueados and coordenada in tabuleiro:
            for struc in listaFechada:
                if coordenada == struc.coordenadaenada:
                    valido = False
            if valido == True:
                for struct in listaAberta:
                    if coordenada == struct.coordenadaenada:
                        valido = False
            if valido == True:
                if(coordenada != estadoFinal):
                    images.append(GifMaker.fill_dot(coordenada, "gray", images))
                listaExpansao.append(coordenada)
    
    return listaExpansao


def preencherNo(listaExpansao, estadoInicial, estadoEscolhido, listaAberta, listaFechada):

    for coordenadaenada in listaExpansao:
        distanciaComeco_G = Calcular.G(estadoInicial, estadoEscolhido, listaFechada, listaAberta) + 1
        distanciaAteFinal_H = Calcular.H(coordenadaenada, estadoFinal)
        total_F = distanciaComeco_G + distanciaAteFinal_H

        listaAberta.append(no(coordenadaenada, total_F, distanciaComeco_G, distanciaAteFinal_H, estadoEscolhido))
        
    return listaAberta


def ordenarNoPorHeuristica(listaAberta):

    elementos = len(listaAberta) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if listaAberta[i].total_F > listaAberta[i + 1].total_F:
                listaAberta[i], listaAberta[i + 1] = listaAberta[i + 1], listaAberta[i]
                ordenado = False
    return listaAberta

def aStar(estadoInicial, estadoFinal):
    estadoEscolhido = estadoInicial
    images = []
    
    #Fazer imagem inicial do gif - cat, bloqueios e estadoFinal
    images.append(GifMaker.compute_initial_image(estadoInicial, bloqueados, estadoFinal, images))
    
    listaFechada = [] #lista visitados
    listaAberta = []  #lista não visitados
    
    contadorEscolhasPai = 0

    #estrutura para a coordenadaenada inicial
    distanciaComeco_G = 0
    distanciaAteFinal_H = Calcular.H(estadoEscolhido, estadoFinal)
    total_F = distanciaComeco_G + distanciaAteFinal_H
    listaAberta.append(no(estadoEscolhido, total_F, distanciaComeco_G, distanciaAteFinal_H, None))

#-----------------------------------------------------------------------
    while estadoEscolhido != estadoFinal:

        contadorEscolhasPai = contadorEscolhasPai + 1

        listaExpansao = expandirEmVolta(estadoInicial, estadoEscolhido, listaAberta, listaFechada, images, bloqueados, estadoFinal)
        listaAberta = preencherNo(listaExpansao, estadoInicial, estadoEscolhido, listaAberta, listaFechada)
        listaAberta = ordenarNoPorHeuristica(listaAberta)
        
        #encontrar na lista aberta coordenadaenada expandida e colocar na lista fechada
        cont = 0
        for struct in listaAberta:
            if struct.coordenadaenada == estadoEscolhido:
                listaFechada.append(struct)
                listaAberta.pop(cont)
                break
            cont = cont + 1

        estadoEscolhido = listaAberta[0].coordenadaenada
        
        images.append(GifMaker.fill_dot(estadoEscolhido, "black" , images))
#-----------------------------------------------------------------------
    
    #Adicionar estadoFinal na lista fechada
    cont = 0
    for struct in listaAberta:
        if struct.coordenadaenada == estadoFinal:
            listaFechada.append(struct)
            listaAberta.pop(cont)
            break
        cont = cont + 1
    
    listaComMelhorCaminho = []
    listaComMelhorCaminho.append(estadoFinal)
    
    #Fazer caminho inverso pela lista fechada até a coordenadaenada inicial(cat)
    aux = True
    while aux:
        for struct in listaFechada:
            if struct.coordenadaenada == estadoEscolhido:
                estadoEscolhido = struct.pai
                listaComMelhorCaminho.append(estadoEscolhido)
                if estadoEscolhido == estadoInicial:
                    aux = False
    
    #Fazer parte do gif que volta da estadoFinal até o inicio
    for coordenadaenada in listaComMelhorCaminho:
        images.append(GifMaker.fill_dot(coordenadaenada, dark_green, images))
    
    #inverter a lista
    listaComMelhorCaminho.reverse()

    #Fazer parte do gif que anda até o fim
    for coordenadaenada in listaComMelhorCaminho:
        images.append(GifMaker.fill_dot(coordenadaenada, light_green, images))
    
    #salvar gif
    images[0].save('aStar.gif',
                       save_all=True,
                       append_images=images[1:],
                       duration=200,
                       loop=0)
    
    print("\nGif Gerado")
    print("\n")
    print("Inicio", estadoInicial)
    print("\n")
    print("Bloqueios", bloqueados)
    print("\n")
    print("Quantidade de nós visitados:", contadorEscolhasPai)
    print("\n")
    print("Lista melhor caminho: ", listaComMelhorCaminho)
    
    os.remove("ImagemTemp.png")
    
aStar(estadoInicial, estadoFinal)