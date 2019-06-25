import os
import sys
no = {
    "quantidade" : 0,
    "caracter" : "",
    "direita": None,
    "esquerda": None
}

import json

'''
Calcular quantos bits sao necessarios
Juntar os bits
Substituir os bits
ArmezanrCodificação
'''
#
# print(os.path.getsize("a.ale"))
# print(os.path.getsize("a.txt"))
#

#
arq = open("imgJogador.ale","wb")
# b = ord("é")
# a = chr(b)
# c = bytes(a,encoding="utf-8")
# d = c.decode()
# print(a,b,c,d,sep="\n")
# arq.write(bytes(169))
# arq.close()
from Ferramentas.ferramentasArquivos import *

# print("texto", texto)
'''
# print(chr(int.from_bytes(b'\xc3\xa9\n', byteorder=sys.byteorder) ))# => 17
print(ord("é"))
arq.write(b'\xc3\xa9\n')
arq.close()

print("Tamanho compac:", os.path.getsize("a.ale"))
print("tamanho Origin:", os.path.getsize("a.txt"))
print("tamanho Gerado:", os.path.getsize("aGer.txt"))

arq1 = open("a.txt", "rb")
arq2 = open("aGer.txt", "rb")

linhas1 = []
for i in arq1:
    linhas1 += [i]

igual = True
cont = 0
for n in arq2:
    if(n != linhas1[cont]):
        print("N", n)
        print("Lista", linhas1[cont])
        print("COnt", cont)
        print("Nao e igual")
        igual = False
        break

    cont += 1


bits ['0110', '1111', '1110', '1101', '1100', '1011', '1010', '1001', '1000', '00111', '00110', '00101', '00100', '00011', '00010', '00001', '00000', '01011', '01010', '01001', '01000', '0111']

0110 1110 11110110111001011101001001100000111001100010100100000110001000000100000001011010100100101000010000011


if(igual):
    print("Igual")
'''
a ="bHAm3}\]&	!%"
for c in a:
    print(bin(ord(c)))
