# Carregar as bibliotecas DesignScript e padrão do Python
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# As entradas para este nó serão armazenadas como uma lista nas variáveis IN.
L1 = IN[0]
L2 = IN[1]

# Insira o código abaixo desta linha

L3 = []

for item in L1:
	if not item in L2:
		L3.append(item)

# Atribua a sua saída para a variável OUT.
OUT = L3