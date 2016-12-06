from tkinter import *
from random import *

def validacion(num):
	if(num>=97 and num<=122):
		return 1
	else:
		return 0

def auto():
	f = open("archivo.html","r")
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
				guardarPalabra(pos,cadena,1)
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
	f=open("estados.txt","a")
	f.write("\n\n")
	f.close()
	f=open("cadenas.txt","a")
	f.write("\n\n")
	f.close()	
	repetir(1)


def automata(cadena):
	f=open("estados.txt","a")
	estado=0
	if(cadena==''):
		return 0
	else:
		for c in cadena:
			if(estado==0):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='e'):
					estado=1
			elif(estado==1):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='r'):
					estado=2
				elif(c=='e'):
					estado=1
				else:
					estado=0
			elif(estado==2):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='e'):
					estado=3
				else:
					estado=0
			elif(estado==3):
				f.write("Estado "+str(estado)+" "+ c+" ")
				if(c=='e'):
					estado=1
				elif(c=='r'):
					estado=2
				else:
					estado=0
	if(estado==3):
		f.write("Estado "+str(estado)+"   ")
		return 1
	f.close()

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

def grafico():
	root = 	Tk()
	root.title('Automata Terminacion "ere" Grafico') # Nombre de la ventana
	canvas=Canvas(root,width=800,height=200)
	canvas.pack()
	canvas.create_arc(80,15,110,50, start=0, extent=180, style='arc') #arco 0-0
	canvas.create_arc(290,15,310,50, start=0, extent=180, style='arc') #arco 1-1
	canvas.create_arc(130,25,260,115, start=0, extent=180, style='arc') #arco 1-0 arriba
	canvas.create_arc(300,25,660,115, start=0, extent=180, style='arc') #arco 3-2 arriba
	canvas.create_arc(100,150,500,100, start=0, extent=-180, style='arc') #arco 3-1 abajo
	canvas.create_arc(90,200,700,70, start=0, extent=-180, style='arc') #arco 4-1 abajo
	canvas.create_arc(500,130,690,70, start=0, extent=-180, style='arc') #arco 4-3 abajo
	canvas.create_line(5,75,50,75) #Linea 1
	canvas.create_line(150,75,250,75) #Linea 2
	canvas.create_line(350,75,450,75) #Linea 3
	canvas.create_line(550,75,645,75) #Linea 4
	canvas.create_oval(50, 30, 150, 130, width=1, fill='green') #Primer Circulo
	canvas.create_oval(250, 30, 350, 130, width=1, fill='blue') #Segundo Circulo
	canvas.create_oval(450, 30, 550, 130, width=1, fill='green') #Tercer Circulo
	canvas.create_oval(650, 30, 750, 130, width=1, fill='blue') #Cuarto Circulo
	canvas.create_oval(645, 25, 755, 135, width=1) #Cuarto Circulo
	canvas.create_oval(40,70,50,80,fill="red") #Flecha 0-0
	canvas.create_oval(135,43,145,53,fill="red") #Flecha 1-0
	canvas.create_oval(240,70,250,80,fill="red") #Flecha 0-1
	canvas.create_oval(440,70,450,80,fill="red") #Flecha 1-2
	canvas.create_oval(635,70,645,80,fill="red") #Flecha 0-1
	canvas.create_oval(335,40,345,50,fill="red") #Flecha 3-1
	canvas.create_oval(100,125,110,135,fill="red") #Flecha 2-0
	canvas.create_oval(85,125,95,135,fill="red") #Flecha 3-0
	canvas.create_oval(75,25,85,35,fill="red") #Flecha 0-0
	canvas.create_oval(285,25,295,35,fill="red") #Flecha 1-1
	canvas.create_oval(525,115,535,125,fill="red") #Flecha 3-2
	estado=Label(root,text="Estado 0",bg="green",font=("Helvetica",12),fg="white") #ESTADO CERO
	estado.place(x = 60, y = 60)
	estado=Label(root,text="Estado 1",bg="blue",font=("Helvetica",12),fg="white") #ESTADO UNO
	estado.place(x = 270, y = 60)
	estado=Label(root,text="Estado 2",bg="green",font=("Helvetica",12),fg="white") #ESTADO DOS
	estado.place(x = 470, y = 60)
	estado=Label(root,text="Estado 3",bg="blue",font=("Helvetica",12),fg="white") #ESTADO TRES
	estado.pack()
	estado.place(x = 670, y = 60)
	letra=Label(root,text="e",font=("Helvetica",12)) # 
	letra.place(x = 190, y = 60)
	letra=Label(root,text="e",font=("Helvetica",12)) # 
	letra.place(x = 310, y = 5)
	letra=Label(root,text="no es e",font=("Helvetica",12)) # 0-0
	letra.place(x = 15, y = 5)
	letra=Label(root,text="e",font=("Helvetica",12)) # 
	letra.place(x = 450, y = 5)
	letra=Label(root,text="no es e ni r",font=("Helvetica",12)) # 1-0
	letra.place(x = 140, y = 5)
	letra=Label(root,text="no es e",font=("Helvetica",12)) # 1-0
	letra.place(x = 280, y = 150)
	letra=Label(root,text="no es e ni r",font=("Helvetica",12)) # 3-0
	letra.place(x = 500, y = 180)
	letra=Label(root,text="r",font=("Helvetica",12)) # 3-0
	letra.place(x = 600, y = 120)
	letra=Label(root,text="r",font=("Helvetica",12)) #  
	letra.place(x = 390, y = 60)
	letra=Label(root,text="e",font=("Helvetica",12)) #
	letra.pack()
	letra.place(x=590,y=60)
	root.mainloop()

menu()