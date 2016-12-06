from random import *

def automata(c):
	c.append('B')
	pos=0
	f=open("proceso.txt","a")
	estado=0
	mov=' '
	while(pos<len(c)):
		f.write("(q"+str(estado)+","+c[pos]+","+mov+")\n")
		f.write(pasarCadena(c.copy(),pos,estado)+"\n")
		if(estado==0):
			if(c[pos]=='0'):
				estado=1
				c[pos]='X'
				pos+=1
				mov='R'
			elif(c[pos]=='Y'):
				estado=3
				c[pos]='Y'
				pos+=1
				mov='R'
			else:
				return 0
		elif(estado==1):
			if(c[pos]=='0'):
				estado=1
				c[pos]='0'
				pos+=1
				mov='R'
			elif(c[pos]=='1'):
				estado=2
				c[pos]='Y'
				pos-=1
				mov='L'
			elif(c[pos]=='Y'):
				estado=1
				c[pos]='Y'
				pos+=1
				mov='R'
			else:
				return 0
		elif(estado==2):
			if(c[pos]=='0'):
				estado=2
				c[pos]='0'
				pos-=1
				mov='L'
			elif(c[pos]=='X'):
				estado=0
				c[pos]='X'
				pos+=1
				mov='R'
			elif(c[pos]=='Y'):
				estado=2
				c[pos]='Y'
				pos-=1
				mov='L'
			else:
				return 0
		elif(estado==3):
			if(c[pos]=='Y'):
				estado=3
				c[pos]='Y'
				pos+=1
				mov='R'
			elif(c[pos]=='B'):
				estado=4
				c[pos]='B'
				return 1
			else:
				return 0
	f.write("Termina Proceso\n\n")
	f.close()

def pasarLista(cadena):
	lista=[]
	for c in cadena:
		lista.append(c)
	return lista

def pasarCadena(lista,pos,estado):
	q=" q"+str(estado)+" "
	lista.insert(pos,q)
	cad=""
	for elemento in lista:
		cad+=elemento
	return cad

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
	cadena=input("Ingresa la cadena ")
	lista=pasarLista(cadena)
	if(automata(lista)==1):
		print("La cadena "+cadena +" es Valida")
	else:
		print("La cadena" +cadena +" es Invalida")
	repetir(1)

def auto():
	n=0
	cad=""
	numero=randint(1,1000)
	while(n<numero):
		cad+=choice(['0','1'])
		n+=1
	print("La cadena generada es "+cad)
	lista=pasarLista(cad)
	if(automata(lista)==1):
		print("La cadena "+str(numero) +" es Valida")
	else:
		print("La cadena" +str(numero) +" es Invalida")
	repetir(2)

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