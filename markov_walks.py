# coding: utf-8
import numpy as np
import random as rm

prob = 1
estadoInicial = ''
#cria um nome para cada estado. Ex: S0, S1,..., Sn
def GeraNomeEstados(numEstados):
	estados = []
	for i in range(0, numEstados):	
		estados.append('S'+str(i))

	return estados

def GeraNomesTransicoes(numEstados):
	if numEstados == 5:
		mtz_nome_trans = [['S0->S0','S0->S1','S0->S2','S0->S3','S0->S4'],['S1->S0','S1->S1','S1->S2','S1->S3','S1->S4'],
						['S2->S0','S2->S1','S2->S2','S2->S3','S2->S4'],['S3->S0','S3->S1','S3->S2','S3->S3','S3->S4'],['S4->S0','S4->S1','S4->S2','S4->S3','S4->S4']]
	elif numEstados == 4:
		mtz_nome_trans = [['S0->S0','S0->S1','S0->S2','S0->S3'],['S1->S0','S1->S1','S1->S2','S1->S3'],
						['S2->S0','S2->S1','S2->S2','S2->S3'],['S3->S0','S3->S1','S3->S2','S3->S3']]
	elif numEstados == 3:
		mtz_nome_trans = [['S0->S0','S0->S1','S0->S2'],['S1->S0','S1->S1','S1->S2'],['S2->S0','S2->S1','S2->S2']]
	elif numEstados == 2:
		mtz_nome_trans = [['S0->S0','S0->S1'],['S1->S0','S1->S1']]
	else:
		mtz_nome_trans = ['S0->S0']

	return mtz_nome_trans

def GeraMtzTransicoes(numEstados):
	if numEstados == 5:
		mtz = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]	
	elif numEstados == 4:
		mtz = [[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]	
	elif numEstados == 3:
		mtz = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
	elif numEstados == 2:
		mtz = [[-1,-1],[-1,-1]]
	else:
		mtz = [-1]

	return mtz

def EntraMatrizTransicoes(mtz):
	n=1
	for i in range(0 , numEstados):
		for j in range(0, numEstados):
			print('Percentual para Transicao',n,':')
			mtz[i][j] = float(input());
			n += 1

#Verifica se a Matriz de Probabilidades foi digitada corretamente. Se a soma  é igual a um.
def VerificaMtz():
	somaProbs = 0
	for i in range(0, numEstados):
		somaProbs = somaProbs + sum(mtz[i])
	
	if somaProbs != numEstados:
		print('Existe algo de errado na Matriz de Probabilidades')
		exit(0)
	else: print('A Matriz de Probabilidades foi Preenchida Corretamente')

def ContaOcorrencias(lista_acoes, _estado):
	cont = 0
	for _lista in lista_acoes:
		if(_lista == _estado):
			cont += 1

	return cont

def PrevisaoDeTransicoes(passos):
	global prob

	acaoAtual = estadoInicial
	listaDeAcoes = [acaoAtual]
	prob = 1
	i = 0   
	while i < passos:    	
		if acaoAtual == "S0":
			troca = np.random.choice(mtz_nome_trans[0],replace=True,p=mtz[0])
			if troca == "S0->S0":
				prob = prob*mtz[0][0]
				acaoAtual = "S0"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S0->S1":
				prob = prob*mtz[0][1]
				acaoAtual = "S1"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S0->S2":
				prob = prob*mtz[0][2]
				acaoAtual = "S2"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S0->S3":
				prob = prob*mtz[0][3]
				acaoAtual = "S3"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S0->S4":
				prob = prob*mtz[0][4]
				acaoAtual = "S4"
				listaDeAcoes.append(acaoAtual)				
#----------------------------------------------------------------------------------------------
		elif acaoAtual == "S1":
			troca = np.random.choice(mtz_nome_trans[1],replace=True,p=mtz[1])
			if troca == "S1->S0":
				prob = prob*mtz[1][0]
				listaDeAcoes.append("S0")
			elif troca == "S1->S1":
				prob = prob*mtz[1][1]
				acaoAtual = "S1"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S1->S2":
				prob = prob*mtz[1][2]
				acaoAtual = "S2"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S1->S3":
				prob = prob*mtz[1][3]
				acaoAtual = "S3"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S1->S4":
				prob = prob*mtz[1][4]
				acaoAtual = "S4"
				listaDeAcoes.append(acaoAtual)
#----------------------------------------------------------------------------------------------
		elif acaoAtual == "S2":
			troca = np.random.choice(mtz_nome_trans[2],replace=True,p=mtz[2])
			if troca == "S2->S0":
				prob = prob*mtz[2][0]
				acaoAtual = "S0"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S2->S1":
				prob = prob*mtz[2][1]
				acaoAtual = "S1"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S2->S2":
				prob = prob*mtz[2][2]
				acaoAtual = "S2"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S2->S3":
				prob = prob*mtz[2][3]
				acaoAtual = "S3"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S2->S4":
				prob = prob*mtz[2][3]
				acaoAtual = "S4"
				listaDeAcoes.append(acaoAtual)
#----------------------------------------------------------------------------------------------
		elif acaoAtual == "S3":
			troca = np.random.choice(mtz_nome_trans[3],replace=True,p=mtz[3])
			if troca == "S3->S0":
				prob = prob*mtz[3][0]
				acaoAtual = "S0"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S3->S1":
				prob = prob*mtz[3][1]
				acaoAtual = "S1"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S3->S2":
				prob = prob*mtz[3][2]
				acaoAtual = "S2"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S3->S3":
				prob = prob*mtz[3][3]
				acaoAtual = "S3"
				listaDeAcoes.append(acaoAtual)
			elif troca == "S3->S4":
				prob = prob*mtz[3][4]
				acaoAtual = "S4"
				listaDeAcoes.append(acaoAtual)
		i = i + 1
	return listaDeAcoes

 
###--------------------------------------MAIN---------------------------------------
numEstados = 0
while numEstados <= 0:
	numEstados = int(input('Entre com o Número de Estados(Máximo de 5 estados): '))

#Entrada da Matriz de Probabilidades (Matriz de Transições)
mtz_nome_trans = GeraNomesTransicoes(numEstados)
mtz = GeraMtzTransicoes(numEstados)
EntraMatrizTransicoes(mtz)
VerificaMtz()
estados = GeraNomeEstados(numEstados)
print('Estes são os estados existentes: ', estados)
# print()

#Permite ao usuário escolher um estado inicial
#estadoInicial = str(input('Escolha o Estado Inicial: ')) 
estadoInicial = str(input('Escolha o Estado Inicial: ')) 

if estadoInicial in estados:
	print('Escolha Válida')
else: 
	print('Escolha Inválida')

print("Entre com o número de passos:")
passos = int(input())
_list = PrevisaoDeTransicoes(passos)
print("Para as entradas fornecidas o sistema obteve esta lista de ações:")
print(_list)							
print('A Probabilidade Estimada para esta sequência de ações: '+str(prob))
print('Estado Final: ', _list[-1])
_estado = str(input("Digite o estado que deseja contar ocorrências: "))
print('O estado \'',_estado,'\' teve',ContaOcorrencias(_list, _estado),'ocorrências pelo modelo probabilístico')

# --------------------------------------FIM MAIN---------------------------------
