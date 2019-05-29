#====================================== BIBLIOTECAS ===============================================
import os
#==================================================================================================

#======================================= ARQUIVOS =================================================

#==================================================================================================


#========================================Estrutura==================================================
#Função para juntar nós do dicionário
def juntarNo(dic1,dic2):

    quantidade1 = dic1["quantidade"]
    quantidade2 = dic2["quantidade"]
    caracter1 = dic1["caracter"]
    caracter2 = dic2["caracter"]


    print(caracter1 + caracter2)
    novoNO = {
        "quantidade":quantidade1 + quantidade2,
        "caracter": caracter1 + caracter2,
        "direita": dic1,
        "esquerda": dic2
    }
    return novoNO


#Ordena a lista em um formato crescente
def ordenarNo(listaNos):
    for i in range(len(listaNos)):
        aux = listaNos[i]
        print(aux)
        for j in range(i,-1,-1):
            if(j == 0):
                listaNos[0] = aux
                break
            if(aux["quantidade"] > listaNos[j - 1]["quantidade"]):
                listaNos[j] = aux
                break

            listaNos[j] = listaNos[j - 1]
    print(listaNos)
    return listaNos


#Crio o nó a partir dos dados do dicionário
def inicializarNo(item):

    quantidade = list(item.values())[0]
    caracter = list(item.keys())[0]
    no = {
        "quantidade":quantidade,
        "caracter": caracter,
        "direita": None,
        "esquerda": None
    }

    return no
#==================================================================================================


#Converter de String para Binário
def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ' '
    return binario

#Função para criar o dicionario e contar as letras
def Criar_Dicionario(palavra):
    letras = {}


    for percorrer in palavra:                   #Criar o dicionario
        letras[percorrer] = 0

    for percorrer_2 in palavra:                 #Adicionar elementos no dicionario
        letras[percorrer_2] += 1

    return letras

#Crio a lista com os dicionários
def Criar_Lista(dicionario):

    listaOrdenada = []
    caracters = list(dicionario.keys())
    qtd = list(dicionario.values())
    for i in range(len(dicionario)):
        listaOrdenada.append({caracters[i]:qtd[i]})

    print(listaOrdenada)

    return listaOrdenada

def OrdenarDicionario_SemFuncao(listaOrdenada):
    for i in range(len(listaOrdenada)):
        aux = listaOrdenada[i]
        print(aux)
        for j in range(i,-1,-1):
            if(j == 0):
                listaOrdenada[0] = aux
                break
            if(list(aux.values())[0] > list(listaOrdenada[j - 1].values())[0]):
                listaOrdenada[j] = aux
                break

            listaOrdenada[j] = listaOrdenada[j - 1]
    print(listaOrdenada)
    return listaOrdenada



#====================================== PROGRAMA PRINCIPAL ===============================================

def main():
    dicionario = Criar_Dicionario("AAAAAABBBBBCCCCDDDEEF")
    listaQuase = Criar_Lista(dicionario)
    listaOrdenada = OrdenarDicionario_SemFuncao(listaQuase)


    listaNos = []

    for item in listaOrdenada:
        listaNos.append(inicializarNo(item))

    print("ANTES")
    for item in listaNos:
        print(item)

    for n in range(0,len(listaNos)):
        if(len(listaNos) > 1):
            newNo = juntarNo(listaNos[0],listaNos[1])
            del listaNos[0]
            del listaNos[0]
            listaNos.append(newNo)

            print("Depois")
            for item in listaNos:
                print(item)





if __name__ == '__main__':
    main()
