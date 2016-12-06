from time import *
from Pila import *
from random import *
from tkinter import *

def automata(pila,cadena):
	f=open("historial.txt","a")
	root = 	Tk()
	root.title('Grafico') # Nombre de la ventana
	canvas=Canvas(root,width=510,height=500)
	canvas.pack()
	canvas.create_line(175,150,175,50)
	canvas.create_line(175,300,175,400)
	estado=Label(root,text="     ",bg="black",font=("Helvetica",100))
	estado.place(x = 100, y = 150)
	pila.estado="q"
	cadenaAux=cadena
	f.write("("+pila.estado+","+cadena+","+pila.mostrar()+")|-")
	estado=Label(root,text="                              ",font=("Helvetica",15))
	estado.place(x = 170, y = 35)
	estado=Label(root,text="                              ",font=("Helvetica",15))
	estado.place(x = 170, y = 400)
	estado=Label(root,text=cadenaAux,font=("Helvetica",15))
	estado.place(x = 170, y = 35)
	estado=Label(root,text=pila.mostrar(),font=("Helvetica",15))
	estado.place(x = 170, y = 400)
	estado=Label(root,text=pila.estado+"  ",bg="black",font=("Helvetica",25),fg="white")
	estado.place(x = 175, y = 200)
	root.update()
	sleep(1)
	for x in cadena:
		if(x=='0'):
			pila.estado='q'
			pila.push()
			cadenaAux=eliminarCaracter(cadenaAux)
			f.write("("+pila.estado+","+cadenaAux+","+pila.mostrar()+")|-")
			estado=Label(root,text="                              ",font=("Helvetica",15))
			estado.place(x = 170, y = 35)
			estado=Label(root,text="                              ",font=("Helvetica",15))
			estado.place(x = 170, y = 400)
			estado=Label(root,text=cadenaAux,font=("Helvetica",15))
			estado.place(x = 170, y = 35)
			estado=Label(root,text=pila.mostrar(),font=("Helvetica",15))
			estado.place(x = 170, y = 400)
			estado=Label(root,text=pila.estado+"  ",bg="black",font=("Helvetica",25),fg="white")
			estado.place(x = 175, y = 200)
			root.update()
			sleep(1)
		elif(x=='1'):
			if(pila.tope>1):
				pila.pop()
				pila.estado='p'
				cadenaAux=eliminarCaracter(cadenaAux)
				f.write("("+pila.estado+","+cadenaAux+","+pila.mostrar()+")|-")
				estado=Label(root,text="                              ",font=("Helvetica",15))
				estado.place(x = 170, y = 35)
				estado=Label(root,text="                              ",font=("Helvetica",15))
				estado.place(x = 170, y = 400)
				estado=Label(root,text=cadenaAux,font=("Helvetica",15))
				estado.place(x = 170, y = 35)
				estado=Label(root,text=pila.mostrar(),font=("Helvetica",15))
				estado.place(x = 170, y = 400)
				estado=Label(root,text=pila.estado+"  ",bg="black",font=("Helvetica",25),fg="white")
				estado.place(x = 175, y = 200)
				root.update()
				sleep(1)
			else:
				root.mainloop()
				f.write("\n")
				f.close()
				return 0
	if(pila.esVacia()==1):
		pila.estado='f'
		f.write("("+pila.estado+","+cadenaAux+","+pila.mostrar()+")\n\n")
		estado=Label(root,text="                              ",font=("Helvetica",15))
		estado.place(x = 170, y = 35)
		estado=Label(root,text="                              ",font=("Helvetica",15))
		estado.place(x = 170, y = 400)
		estado=Label(root,text=cadenaAux,font=("Helvetica",15))
		estado.place(x = 170, y = 35)
		estado=Label(root,text=pila.mostrar(),font=("Helvetica",15))
		estado.place(x = 170, y = 400)
		estado=Label(root,text=pila.estado+"  ",bg="black",font=("Helvetica",25),fg="white")
		estado.place(x = 175, y = 200)
		root.update()
		sleep(1)
		root.mainloop()
		f.write("\n")
		f.close()
		return 1

def eliminarCaracter(cadena):
	x=1
	cadenaAux=""
	while(x<len(cadena)):
		cadenaAux+=cadena[x]
		x+=1
	if(cadenaAux==""):
		return "epsilon"
	else:
		return cadenaAux

def manual(pila):
	f=open("cadenas.txt","a")
	cadena=input("Ingresa la cadena ")
	if(automata(pila,cadena)==1):
		print("Cadena Valida")
		f.write(cadena+" Cadena Valida\n\n")
	else:
		print("Cadena Invalida")
		f.write(cadena+" Cadena Invalida\n\n")
	f.close()
	repetir(1,pila)

def auto(pila):
	f=open("cadenas.txt","a")
	cadena=generarCadena()
	if(automata(pila,cadena)==1):
		print("Cadena Valida")
		f.write(cadena+" Cadena Valida\n\n")
	else:
		print("Cadena Invalida")
		f.write(cadena+" Cadena Invalida\n\n")
	f.close()
	repetir(2,pila)

def generarCadena():
    longitud=randint(1,1000)
    numero=''
    i=0
    while(i<longitud):
	    numero+=choice(['0', '1'])
	    i += 1
    print("El numero generado es: "+numero)
    return numero

def repetir(modo,pila):
	rep=''
	if(modo==1):
		while(rep!='1' and rep!='2'):
			rep=input("Deseas Repetir en este modo\n 1. Si \n 2. No\n ==> ")
			if(rep=='1'):
				print("Seleccionaste repetir")
				manual(pila)
			elif(rep=='2'):
				print("Seleccionaste NO repetir")
			else:
				print("Opcion Invalida, Intentalo de nuevo")
	elif(modo==2):
		rep=choice(['1', '2'])
		if(rep=='1'):
			print("Seleccionaste repetir")
			auto(pila)
		elif(rep=='2'):
			print("Seleccionaste NO repetir")

def crearArchivo():
	f=open("historial.txt","w")
	f.close()
	f=open("cadenas.txt","w")
	f.close()

def menu(pila):
	crearArchivo()
	eleccion=0
	while (eleccion!=4):
		eleccion=input("Selecciona una opcion\n1.Manual\n2.Automatico\n3.Salir\n===> ")
		if(eleccion=='1'):
			print("Opcion Manual seleccionada")
			manual(pila)
		elif(eleccion=='2'):
			print("Opcion Automatica seleccionada")
			auto(pila)
		elif(eleccion=='3'):
			print("Adios")
			return 0
		else:
			print("Opcion Invalida, Intentalo de nuevo")

pila=Pila()
pila.inicializarPila()
menu(pila)