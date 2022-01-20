# Carregar as bibliotecas DesignScript e padrão do Python
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
import math as m

# As entradas para este nó serão armazenadas como uma lista nas variáveis IN.
Cabos = IN[0][2:]
Curvas = IN[1]
Eletrodutos = IN[2][2:]

# Insira o código abaixo desta linha

# Calcula o comprimento do caminho de eletroduto entre o trafo e 
# o cubículo de medição e proteção

Tam_Ali = 0 # tamanho total do caminho de alimentação
Tam_Aterr = 0 # tamanho total do caminho de aterramento

L = []

# Comprimento das curvas

for curva in Curvas:
	if curva.GetParameterValueByName("Tipo de serviço") == "Alimentação":
		Tam_Ali += float(curva.GetParameterValueByName("Raio de curvatura"))
	elif curva.GetParameterValueByName("Tipo de serviço") == "Aterramento":
		Tam_Aterr += float(curva.GetParameterValueByName("Raio de curvatura"))
		
Tam_Ali *= 1e-3*m.pi/2
Tam_Aterr *= 1e-3*m.pi/2
		
# Comprimento dos eletrodutos

for elet in Eletrodutos:
	if elet[4] == "Alimentação":
		Tam_Ali += float(elet[2])
	elif elet[4] == "Aterramento":
		Tam_Aterr += float(elet[2])

# Faz a alteração no comprimento dos cabos

Cabos_corr = Cabos[:] # cria uma cópia da lista de cabos

for cabo in Cabos_corr:
	comp_revit = float(cabo[2])
	if cabo[5] == ".Trafo saída BT":
	   	# Trata-se da alimentação.
		comp_cabo = (comp_revit + Tam_Ali) * int(cabo[4])
		cabo[2] = comp_cabo
	elif cabo[5] == ".Aterramento Subestação":
		comp_cabo = comp_revit + Tam_Aterr
		cabo[2] = comp_cabo
		
# Atribua a sua saída para a variável OUT.
OUT = Cabos_corr