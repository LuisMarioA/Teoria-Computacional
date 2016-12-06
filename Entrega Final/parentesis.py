from random import*

def imprimir(lista,c,regla):
	f=open("proceso.txt","a")
	cad=""
	for x in lista:
		cad+=x
	while(len(c)!=20):
		c+=" "
	if(regla==0):
		f.write("Inicio | "+c + " | "+cad+"\n")
	elif(regla==1):
		f.write("B->(RB | "+c + " | "+cad+"\n")
	elif(regla==2):
		f.write("B-> e  | "+c + " | "+cad+"\n")
	elif(regla==3):
		f.write("R->(RR | "+c + " | "+cad+"\n")
	elif(regla==4):
		f.write("R-> )  | "+c + " | "+cad+"\n")
	f.close()

def acomodarCadena(cadena):
	cadenaAux=""
	if(cadena==""):
		return "Resultado"
	for x in range(1,len(cadena)):
		cadenaAux+=cadena[x]
	return cadenaAux

def automata(cadena):
	cadenaAux=cadena
	regla=0
	pasos=['B']
	imprimir(pasos,cadena,regla)
	for c in cadena:
		cadenaAux=acomodarCadena(cadenaAux)
		x=0
		while(pasos[x]=='(' or pasos[x]==')'):
			x+=1
		estado=pasos[x]
		if(estado=='B'):
			if(c=='('):
				pasos.insert(x,'(')
				pasos.remove('B')
				pasos.append('R')
				pasos.append('B')
				regla=1
			elif(c==')'):
				return 0						
		elif(estado=='R'):
			if(c=='('):
				pasos.insert(x-1,'(')
				pasos.insert(x+1,'R')
				regla=3
			if(c==')'):
				pasos.insert(x,')')
				pasos.remove('R')
				regla=4
		imprimir(pasos,cadenaAux,regla)
	if(pasos[-2]==')' and pasos[-1]=='B'):
		pasos.remove('B')
		imprimir(pasos,acomodarCadena(cadenaAux),2)
		return 1
	else:
		return 0

def crearArchivo():
	f=open("proceso.txt","w")
	f.close()

def menu():
	crearArchivo()
	eleccion=0
	while (eleccion!=4):
		eleccion=input("Selecciona una opcion\n1.Manual\n2.Automatico\n3.Salir\n===> ")
		if(eleccion=='1'):
			print("Opcion Manual seleccionada")
			manual()
		elif(eleccion=='2'):
			print("Opcion Automatica seleccionada")
			auto()
		elif(eleccion=='3'):
			print("Adios")
			return 0
		else:
			print("Opcion Invalida, Intentalo de nuevo")

def manual():
	f=open("proceso.txt","a")
	cadena=input("Ingresa la cadena ")
	if(automata(cadena)==1):
		print("La cadena "+cadena+" es Valida")
		f.write("La cadena "+cadena+" es Valida\n\n")
	else:
		print("La cadena "+cadena+" NO esta balanceada")
		f.write("La cadena "+cadena+" NO esta balanceada\n\n")
	f.close()
	repetir(1)


def auto():
	cadena=generarCadena()
	f=open("proceso.txt","a")
	if(automata(cadena)==1):
		print("La cadena "+cadena+" es Valida")
		f.write("La cadena "+cadena+" es Valida\n\n")
	else:
		print("La cadena "+cadena+" NO esta balanceada")
		f.write("La cadena "+cadena+" NO esta balanceada\n\n")
	f.close()
	repetir(2)

def generarCadena():
    longitud=randint(1,20)
    cadena=''
    i=0
    while(i<longitud):
	    cadena+=choice(['(', ')'])
	    i += 1
    print("La cadena generado es: "+cadena)
    return cadena

def repetir(modo):
	rep=''
	if(modo==1):
		while(rep!='1' and rep!='2'):
			rep=input("Deseas Repetir en este modo\n 1. Si \n 2. No\n ==> ")
			if(rep=='1'):
				print("Seleccionaste repetir")
				manual()
			elif(rep=='2'):
				print("Seleccionaste NO repetir")
			else:
				print("Opcion Invalida, Intentalo de nuevo")
	elif(modo==2):
		rep=choice(['1', '2'])
		if(rep=='1'):
			print("Seleccionaste repetir")
			auto()
		elif(rep=='2'):
			print("Seleccionaste NO repetir")

menu()