from random import *

def eliminarFinales(listas):
	x=0
	for lista in listas:
		if(lista[0]==0 and lista[1]==0):
			del(listas[x])
		elif(lista[0]==0 and lista[2]==0):
			del(listas[x])
		elif(lista[2]==0 and lista[1]==0):
			del(listas[x])
		x+=1

def generarCombinaciones(listas,n):
	for x in range(0,n+1):
		for y in range(0,n+1):
			for z in range(0,n+1):
				if((x+y+z)==n):
					listas.append([x,y,z])
	eliminarFinales(listas)

def falla(lista):
	if(lista[0]==0 and lista[1]==0):
		return 1
	elif(lista[0]==0 and lista[2]==0):
		return 1
	elif(lista[2]==0 and lista[1]==0):
		return 1
	else:
		return 0

def enRuta(lista,ruta):
	if(ruta==[]):
		return 0
	for casilla in ruta:
		if(casilla==lista):
			return 1
	return 0

def proceso(especie,lista,ruta):
	nueva=lista.copy()
	if(enRuta(nueva,ruta)==1):
		f=open("NoTerminan.txt","a")
		ruta.append(especie)
		ruta.append(lista.copy())
		del(ruta[0])
		f.writelines(str(ruta[0])+" No Termina "+str(ruta)+"\n")
		f.close()
	elif(falla(nueva)==1):
		f=open("Terminan.txt","a")
		ruta.append(especie)
		ruta.append(lista.copy())
		del(ruta[0])
		f.writelines(str(ruta[0])+" TERMINA "+str(ruta)+"\n")
		f.close()
	else:
		ruta.append(especie)
		ruta.append(nueva.copy())
		if(nueva[0]==0):
			nueva[0]+=2
			nueva[1]-=1
			nueva[2]-=1
			proceso("A",nueva.copy(),ruta.copy())
		elif(nueva[1]==0):
			nueva[1]+=2
			nueva[0]-=1
			nueva[2]-=1
			proceso("B",nueva.copy(),ruta.copy())
		elif(nueva[2]==0):
			nueva[2]+=2
			nueva[0]-=1
			nueva[1]-=1
			proceso("C",nueva.copy(),ruta.copy())
		else:
			nueva1=nueva.copy()
			nueva2=nueva.copy()
			nueva3=nueva.copy()
			nueva1[0]+=2
			nueva1[1]-=1
			nueva1[2]-=1
			proceso("A",nueva1.copy(),ruta.copy())
			nueva2[1]+=2
			nueva2[0]-=1
			nueva2[2]-=1
			proceso("B",nueva2.copy(),ruta.copy())
			nueva3[2]+=2
			nueva3[0]-=1
			nueva3[1]-=1
			proceso("C",nueva3.copy(),ruta.copy())

def crearArchivo():
	f=open("Terminan.txt","w")
	f.close()
	f=open("NoTerminan.txt","w")
	f.close()

def manual():
	listas=[]
	habitantes=0
	habitantes=int(input("Ingresa el numero de habitantes en el planeta (2-15) ==>  "))
	while(habitantes>15 or habitantes<2):
		print("Opcion Invalida")
		habitantes=int(input("Ingresa el numero de habitantes en el planeta (2-15) ==>  "))
	f=open("Terminan.txt","a")
	g=open("NoTerminan.txt","a")
	generarCombinaciones(listas,habitantes)
	for lista in listas:
		ruta=[]
		proceso("A",lista,ruta)
	f.write("Termina Ejecucion\n")
	g.write("Termina Ejecucion\n")
	f.close()
	g.close()
	repetir(1)

def auto():
	listas=[]
	habitantes=randint(2,15)
	f=open("Terminan.txt","a")
	g=open("NoTerminan.txt","a")
	print("El numero seleccionado es " +str(habitantes))
	generarCombinaciones(listas,habitantes)
	f.write("Termina Ejecucion\n")
	g.write("Termina Ejecucion\n")
	for lista in listas:
		ruta=[]
		proceso("A",lista,ruta)
	f.close()
	g.close()
	repetir(2)

def menu():
	eleccion=0
	crearArchivo()
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