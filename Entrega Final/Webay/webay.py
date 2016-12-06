from tkinter import *
from random import *
from grafico import *

def validacion(num):
	if(num>=97 and num<=122):
		return 1
	else:
		return 0

def automata(cadena):
	f=open("estados.txt","a")
	estado=0
	control=0
	if(cadena==''):
		return 0
	else:
		for c in cadena:
			if(estado==0):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='w'):
					estado=1
				elif(c=='e'):
					estado=4
				else:
					estado=0
			elif(estado==1):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='e'):
					estado=2
				elif(c=='w'):
					estado=1
				else:
					estado=0
			elif(estado==2):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='b'):
					estado=3
					control+=1
				elif(c=='e'):
					estado=4
				elif(c=='w'):
					estado=1
				else:
					estado=0
			elif(estado==3):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='a'):
					estado=6
				elif(c=='e'):
					estado=4
				elif(c=='w'):
					estado=1
				else:
					estado=0
			elif(estado==4):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='b'):
					estado=5
				elif(c=='e'):
					estado=4
				elif(c=='w'):
					estado=1
			elif(estado==5):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='a'):
					estado=6
				elif(c=='e'):
					estado=4
				elif(c=='w'):
					estado=1
				else:
					estado=0
			elif(estado==6):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='y'):
					estado=7
					control+=1
				elif(c=='e'):
					estado=4
				elif(c=='w'):
					estado=1
				else:
					estado=0
			elif(estado==7):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='w'):
					estado=1
				elif(c=='e'):
					estado=4
	if(control>0):
		return 1
	else:
		return 0

def auto():
	f = open("archivo.txt","r")
	linea=""
	noLinea=1
	control=0
	temporal=''
	linea=f.readline()
	while (linea != ''):
		posTemporal=0
		pos=0
		palabra=linea.lower()
		for c in palabra:
			if(validacion(ord(c))==0):
				control=1
				if(automata(temporal)==1):
					guardarPalabra(pos,linea,noLinea)
				temporal=''
				posTemporal+=1
				pos=posTemporal
			else:
				temporal+=c
				posTemporal+=1
				control=0
		linea=f.readline()
		noLinea+=1
	if(control==0):
		if(automata(temporal)==1):
			guardarPalabra(pos,linea,noLinea)
	f.close()
	f=open("estados.txt","a")
	f.write("\n\n")
	f.close()
	f=open("cadenas.txt","a")
	f.write("\n\n")
	f.close()
	repetir(2)	

def manual():
	control=0
	pos=0
	posTemporal=0
	temporal=''
	cadena=input("Ingresa la cadena ")
	palabra=cadena.lower()
	for c in palabra:
		if(validacion(ord(c))==0):
			control=1
			if(automata(temporal)==1):
				print("Cadena Valida")
				guardarPalabra(pos,cadena,1)
			else:
				print("Cadena Invalida")
			temporal=''
			posTemporal+=1
			pos=posTemporal
		else:
			temporal+=c
			posTemporal+=1
			control=0
	if(control==0):
		if(automata(temporal)==1):
			guardarPalabra(pos,cadena,1)
			print("Cadena Valida")
		else:
			print("Cadena Invalida")
	f=open("estados.txt","a")
	f.write("\n\n")
	f.close()
	f=open("cadenas.txt","a")
	f.write("\n\n")
	f.close()	
	repetir(1)

def guardarPalabra(caracter,cadena,linea):
	f=open("cadenas.txt","a")
	temporal=''
	x=caracter
	while(x<len(cadena) and (validacion(ord(cadena[x].lower()))!=0)):
		temporal+=cadena[x]
		x+=1
	f.write("Fila "+str(linea)+" Caracter "+str(caracter+1)+" "+temporal+" ")
	f.close()

def crearArchivos():
	cadenas=open("cadenas.txt","w")
	cadenas.close()
	estados=open("estados.txt","w")
	estados.close()

def menu():
	crearArchivos()
	eleccion=0
	while (eleccion!=4):
		eleccion=input("Selecciona una opcion\n1.Manual\n2.Automatico\n3.Mostrar Grafico\n4.Salir\n===> ")
		if(eleccion=='1'):
			print("Opcion Manual seleccionada")
			manual()
		elif(eleccion=='2'):
			print("Opcion Automatica seleccionada")
			auto()
		elif(eleccion=='3'):
			print("Visualizar Grafico")
			grafico()
		elif(eleccion=='4'):
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