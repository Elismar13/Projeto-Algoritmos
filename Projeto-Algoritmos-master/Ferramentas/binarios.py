'''
Este arquivo contem as funções referentes as conversoes de diferentes tipos para binario e vice-versa
'''


# Converter de String para Binário
def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ' '
    return binario

# Converter deBinario Para Decimal
def converterBinarioDecimal(binario):
    numero = 0
    pot = len(binario) - 1
    for i in range(0,len(binario)):
        numero += int(binario[i]) * (2 ** pot)
        pot -= 1

    return numero


# Converter de Decimal para Binario sem determinar numero minimo de bits
def converterDecimalBinario(decimal):
    if(decimal // 2 <= 1):
        return str(decimal // 2) + str(decimal % 2)

    return  converterDecimalBinario(decimal//2) + str(decimal % 2)


#Converter de Decimal determinando numeoro minimo de bits
def converterDecimalBinarioMin(decimal,n = 5):
    if(decimal // 2 <= 0 and n <= 0):

        return  str(decimal // 2) + str(decimal % 2)

    return  converterDecimalBinarioMin(decimal//2,n -1) + str(decimal % 2)



# Substitui os bits em um conjunto de 7 bits
def substituirBits(bits):
    codificado = ""
    for bit in bits:
        codificado += bit

    listaBytes = []
    for n in range(0,len(codificado),7):
        byte = ""
        for j in range(n,n+7):
            if(j == len(codificado)):
                break
            byte += codificado[j]

        listaBytes.append(byte)

    return listaBytes

#Converte Byte em caracter
def converterByte(byte):

    caracter = chr(int(byte,2))
    return caracter
