'''
Ferramentas uteis para o funcionamento do codigo
'''

'''
# Exibe o valor percentual e uma barra mostrando o percentual
# Parametros(percentual:float)
# Return()
'''
def exibirPercentual(percentual):

    print("%0.2f" %percentual,"%", sep="")
    qtdBarras = int(percentual // 10)
    qtdPontos = 10 - qtdBarras
    print("| " * qtdBarras, ". " * qtdPontos)



'''
Conta a frequencia de cada caracter em um texto
Parametros(Texto:String)
Return(frequencia:dict)
'''
def Contar_Caracteres(texto):
    frequencia = {}

    for percorrer in texto:                    # Criar o dicionario Com caracter zeradado
        frequencia[percorrer] =  0

    for percorrer_2 in texto:                  # Adicionar 1 para cada momento em que encontrar um caracter
        frequencia[percorrer_2] +=  1

    listFrequencia = []
    for item in frequencia:
        listFrequencia.append({item:frequencia[item]})

    frequencia = ordenarFrequencia(listFrequencia)
    return frequencia

'''
# Ordenar a frequencia pelo valor do caracter
# Parametros(frequencia:dict)
# Return(frequenciaOrdenada:list)
'''
def ordenarFrequencia(lista):
    for i in range(len(lista)):
        aux = lista[i]
        for j in range(i,-1,-1):
            if(j == 0):
                lista[0] = aux
                break
            if(list(aux.keys())[0] > list(lista[j -1].keys())[0]):
                lista[j] = aux
                break
            lista[j] = lista[j - 1]
    return lista


'''
#Crio a lista a a partir  de um dicionario
#Paramentros(dicionarios:dict)
#Return(list)
'''
def Criar_Lista(dicionario):

    lista = []
    caracters = list(dicionario.keys())
    qtd = list(dicionario.values())
    for i in range(len(dicionario)):
        lista.append({caracters[i]:qtd[i]})


    return lista


'''
#Ordena uma lista de dicionarios
#Parametros(lista:list)
#Return(list)
'''
def OrdenarDicionario_SemFuncao(lista):
    for i in range(len(lista)):
        aux = lista[i]
        for j in range(i,-1,-1):
            if(j == 0):
                lista[0] = aux
                break
            if(list(aux.values())[0] > list(lista[j - 1].values())[0]):
                lista[j] = aux
                break

            lista[j] = lista[j - 1]
    return lista


'''
# Remove n caracters do inicio da string
# Parametros(string:string, n:int)
# return(novaString:string)
'''
def ajustaString(string,n):
    novaString = ""
    for n in range(n,len(string)):
        novaString += string[n]

    return novaString


'''
# Exibe o Menu e retorna a opcao selecionada pelo usuario
# Parametros()
# Return(opcao:int)
'''
def exibirMenu():
    print("============Concorreten do WInrar============")
    print("0-Sair;")
    print("1-Compactar;")
    print("2-Descompactar")
    opcao = int(input("Digite a opcao desejada: "))
    return opcao


'''
# Mostra ultimas informacoes antes de encerrar
# Parametros()
# return(0)
'''
def encerrar():
    print("Encerrando...")
    print("===========Obrigado por nos utilizar========")
    print("===========Avalie em 5 estrelas========")
    print("===========#NaoAoWINRAR========")
    return 0

