'''
Arquivo contendo as funções que envolvem os nós da arvore
'''

def juntarNo(dic1,dic2):

    novoNO = {}
    quantidade1 = dic1["quantidade"]
    quantidade2 = dic2["quantidade"]
    caracter1 = dic1["caracter"]
    caracter2 = dic2["caracter"]

    if(quantidade1 < quantidade2):
        novoNO = {
            "quantidade":quantidade1 + quantidade2,
            "caracter": caracter1 + caracter2,
            "direita": dic1,
            "esquerda": dic2
        }
    else:
        novoNO = {
            "quantidade":quantidade1 + quantidade2,
            "caracter": caracter1 + caracter2,
            "direita": dic2,
            "esquerda": dic1
        }

    return novoNO


#Ordena a lista em um formato crescente
def ordenarNo(listaNos):
    for i in range(len(listaNos)):
        aux = listaNos[i]
        for j in range(i,-1,-1):
            if(j == 0):
                listaNos[0] = aux
                break
            if(aux["quantidade"] > listaNos[j - 1]["quantidade"]):
                listaNos[j] = aux
                break

            listaNos[j] = listaNos[j - 1]

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
