# Carregar as bibliotecas DesignScript e padrão do Python
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# As entradas para este nó serão armazenadas como uma lista nas variáveis IN.
Cabos = IN[0]
Eletrodutos = IN[1][2:]
SE = IN[2][2:]

# Insira o código abaixo desta linha

Quantitativo = [["Item", "Quantidade"]]

for item in Cabos:
	#cabo = item[0].split(': ')[1]
	Quantitativo.append([item[1], float(item[2])])
	
# Verifica se há itens iguais separados
for i in range(1,len(Quantitativo)-2):
	if Quantitativo[i][0] == Quantitativo[i+1][0]:
		Quantitativo[i][1] += Quantitativo[i+1][1]
		del Quantitativo[i+1]
	
for item in Eletrodutos:
	Quantitativo.append([item[1], float(item[2])])
	
# Aproxima os comprimentos para o inteiro mais próximo e adiciona 
# a unidade 'm' (metro) para melhor leitura da equipe de orçamento

for item in Quantitativo[1:]:
	item[1] = str(round(item[1])) + " m"
	
# Obtém o tamanho da lista contando apenas cabos e eletrodutos
old_len = len(Quantitativo)

for item in SE:
	if "Arame de Aço Galvanizado" in item[0]:
		Quantitativo.append([item[1], "2 kg"])
	else:
		Quantitativo.append([item[1], item[2]])
		
# Verifica se há itens iguais separados
for i in range(old_len,len(Quantitativo)-2):
	if Quantitativo[i][0] == Quantitativo[i+1][0]:
		Quantitativo[i][1] = int(Quantitativo[i][1]) + int(Quantitativo[i+1][1])
		del Quantitativo[i+1]
	

# Atribua a sua saída para a variável OUT.
OUT = Quantitativo