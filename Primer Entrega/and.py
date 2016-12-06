from random import *
from tkinter import *

def grafico():
	root = 	Tk()
	root.title('Automata No Determinista Grafico') # Nombre de la ventana
	canvas=Canvas(root,width=800,height=200)
	canvas.pack()
	canvas.create_line(10,90,635,90) #Linea
	canvas.create_oval(40, 40, 140, 140, width=1, fill='blue') #Primer Circulo
	canvas.create_oval(340, 40, 440, 140, width=1, fill='blue') #Segundo Circulo
	canvas.create_oval(640, 40, 740, 140, width=1, fill='blue') #Tercer Circulo
	canvas.create_oval(635, 35, 745, 145, width=1) #Tercer Circulo
	canvas.create_arc(80,3,100,90, start=0, extent=180, style='arc') #Ciclo estado 1
	canvas.create_oval(40,85,30,95,fill='red')#Flecha inical
	canvas.create_oval(340,85,330,95,fill='red')#Flecha de 0-1
	canvas.create_oval(635,85,625,95,fill='red')#Flecha de 1-2
	canvas.create_oval(75,35,85,45,fill='red')#Flecha del ciclo
	estado=Label(root,text="Estado 0",bg="blue",font=("Helvetica",12),fg="white") #ESTADO CERO
	estado.place(x = 55, y = 75)
	estado=Label(root,text="Estado 1",bg="blue",font=("Helvetica",12),fg="white") #ESTADO UNO
	estado.place(x = 355, y = 75)
	estado=Label(root,text="Estado 2",bg="blue",font=("Helvetica",12),fg="white") #ESTADO DOS
	estado.place(x = 655, y = 75)
	numero=Label(root,text="0",font=("Helvetica",12))
	numero.place(x = 205, y = 60)
	numero=Label(root,text="1",font=("Helvetica",12))
	numero.place(x = 505, y = 60)
	numero=Label(root,text="0,1",font=("Helvetica",12))
	numero.place(x = 110, y = 10)
	root.mainloop()

def automata(cadena):
	lista = []
	lista.append(['q0'])
	for caracter in cadena:
		if(caracter=='0'):
			entraCero(lista)
		elif(caracter=='1'):
			entraUno(lista)
		else:
			return 0;
	imprimirMatriz(lista,cadena)
	if(lista[-1][-1]=='q2'):
		lista=[]
		return 1
	else:
		lista=[]
		return 2

def entraCero(lista):
	listaAux=lista[-1][:]
	while('q2' in listaAux):
		listaAux.insert(listaAux.index('q2'),' x')
		listaAux.remove('q2')
	while('q1' in listaAux):
		listaAux.insert(listaAux.index('q1'),' x')
		listaAux.remove('q1')
	listaAux.append('q1')
	lista.append(listaAux)

def entraUno(lista):
	listaAux=lista[-1][:]
	while('q2' in listaAux):
		listaAux.insert(listaAux.index('q2'),' x')
		listaAux.remove('q2')
	while('q1' in listaAux):
		listaAux.insert(listaAux.index('q1'),'q2')
		listaAux.remove('q1')
	lista.append(listaAux)

def imprimirMatriz(lista,cadena):
	i=0
	e=0
	rellenarMatriz(lista)
	while(i<len(lista)):
		if(e<len(lista)-1):
			print(str(cadena[e])+"|"+str(lista[i]))
		else:
			print(" |"+str(lista[i]))
		e+=1
		i+=1


def rellenarMatriz(lista):
	for i in lista:
		while(len(i)<len(lista[-1])):
			i.append(' x')

def menu():
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

def manual():
	cadena=input("Ingresa el numero que deseas validar:\n==> ")
	if(automata(cadena)==1):
		print("La cadena "+cadena+" es Valida")
	else:
		print("La cadena "+cadena+" NO es Valida")
	repetir(1)


def auto():
	cadena=generarCadena()
	if(automata(cadena)==1):
		print("La cadena "+cadena+" es Valida")
	else:
		print("La cadena "+cadena+" NO es Valida")
	repetir(2)

def generarCadena():
    longitud=randint(1,10)
    numero=''
    i=0
    while(i<longitud):
	    numero+=choice(['0', '1'])
	    i += 1
    print("El numero generado es: "+numero)
    return numero

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