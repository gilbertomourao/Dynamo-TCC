# Carregar as bibliotecas DesignScript e padrão do Python
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# As entradas para este nó serão armazenadas como uma lista nas variáveis IN.
Curvas = IN[0]
TabElet = IN[1][2:] # As duas primeiras linhas são ignoradas

# Separa as curvas no número de categorias de diâmetro dos eletrodutos
#diams = [None]*len(TabElet)

for curva in Curvas:
	for elet in TabElet:
		# elet[2] é o diâmetro nominal do eletroduto em forma de texto.
		# O texto é um número seguido do caractere ' ' e logo depois 
		# a unidade. Portanto, a primeira palavra da string elet[2] 
		# é o diâmetro procurado.
		elet_diam = float(elet[3].split()[0])
		if curva.GetParameterValueByName("Diâmetro nominal") == elet_diam:
			curva.SetParameterByName("Tipo de serviço", elet[4])
			break

# Atribua a sua saída para a variável OUT.
OUT = Curvas