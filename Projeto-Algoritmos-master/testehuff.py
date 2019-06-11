import os
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
# arq = open("a.ale","rb")
# b = ord("é")
# a = chr(b)
# c = bytes(a,encoding="utf-8")
# d = c.decode()
# print(a,b,c,d,sep="\n")
# arq.write(bytes(169))
# arq.close()
from Ferramentas.ferramentasArquivos import *

# texto = lerArquivo(arq)
# print("texto", texto)

print(int.from_bytes(b'\x03\011', byteorder=sys.byteorder) ) # => 17
