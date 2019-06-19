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

if(igual):
    print("Igual")
