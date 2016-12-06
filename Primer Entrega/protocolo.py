from random import *
from time import *
from tkinter import *
def crearTrama():
	f = open("trama.txt","w")
	cadena=""
	f.write("(")
	for i in range(0,50):
		cadena=""
		for c in range(0,32):
			caracter=str(randint(0,1))
			cadena+=caracter
		f.write(cadena)
		if(i<49):
			f.write(",")
	f.write(")")
	f.close()

def interruptor():
	return randint(0,1)

def crearArchivos():
	cadenas=open("cadenasValidas.txt","w")
	cadenas.close()
	archivo=open("estadosA.txt","w")
	archivo.close()

def guardarPalabra(cadena):
	filtro = open("cadenasValidas.txt","a")
	filtro.write(cadena+",")
	filtro.close()

def seccionarArchivo(num):
	filtro = open("cadenasValidas.txt","a")
	filtro.write("\nTrama " + str(num+1) + "\n")
	filtro.close()

def validar():
	cadena = ""
	estado = 0
	palabra = ""
	f = open("trama.txt","r")
	for cadena in f.readlines():
		for x in range(0,len(cadena)):
			if(estado==0):
				if(cadena[x]=='0'):
					palabra+=cadena[x]
					estado=1
				elif(cadena[x]=='1'):
					palabra=palabra+cadena[x]
					estado=2
				elif(cadena[x]==',' or cadena[x]==')'):
					guardarPalabra(palabra)
					palabra=""
					estado=0
			elif(estado==1):
				if(cadena[x]=='0'):
					palabra=palabra+cadena[x]
					estado=0
				elif(cadena[x]=='1'):
					palabra=palabra+cadena[x]
					estado=3
				elif(cadena[x]==','or cadena[x]==')'):
					palabra=""
					estado=0
			elif(estado==2):
				if(cadena[x]=='0'):
					palabra=palabra+cadena[x]
					estado=3
				elif(cadena[x]=='1'):
					palabra=palabra+cadena[x]
					estado=0
				elif(cadena[x]==','or cadena[x]==')'):
					palabra=""
					estado=0
			elif(estado==3):
				if(cadena[x]=='0'):
					palabra=palabra+cadena[x]
					estado=2
				elif(cadena[x]=='1'):
					palabra=palabra+cadena[x]
					estado=1
				elif(cadena[x]==','or cadena[x]==')'):
					palabra=""
					estado=0
	f.close()


def grafico():
	f=open("estadosA.txt","a")
	root = 	Tk()
	root.title('Protocolo') # Nombre de la ventana
	canvas=Canvas(root,width=600,height=200)
	canvas.pack()
	canvas.create_arc(90,50,320,150, start=0, extent=180, style='arc') #arco 1-2 arriba
	canvas.create_arc(90,60,320,160, start=360, extent=-180, style='arc') #arco 1-2 abajo
	canvas.create_oval(10, 50, 100, 150, width=1, fill='yellow') #Primer Circulo
	canvas.create_oval(7, 47, 103, 153, width=1)
	canvas.create_oval(310, 50, 400, 150, width=1, fill='yellow') #Segundo Circulo
	canvas.create_oval(305,75,315,85,fill="cyan") #Flecha 0-1
	canvas.create_oval(90,120,100,130,fill="cyan") #Flecha 1-0
	estado=Label(root,text="Validacion",bg="black",font=("Helvetica",12),fg="white") #VALIDACION
	estado.place(x=170,y=150)
	estado=Label(root,text="Estado 0",bg="yellow",font=("Helvetica",12)) #ESTADO CERO
	estado.place(x = 20, y = 80)
	estado=Label(root,text="Estado 1",bg="yellow",font=("Helvetica",12)) #ESTADO UNO
	estado.pack()
	estado.place(x = 320, y = 80)
	encendido=Label(root,text="Encendido",font=("Helvetica",12))
	encendido.pack()
	encendido.place(x = 170, y = 40)
	estado=Label(root,text="Enviando Trama y Validando",font=("Helvetica",10)) #Enviando Trama
	estado.place(x = 430, y = 75)
	estado=Label(root,text="Interruptor",font=("Helvetica",10)) #Interruptor
	estado.pack()
	estado.place(x=430,y=45)
	canvas.create_oval(410,50,425,65,fill="blue") #Encendido/Apagado
	canvas.create_oval(410,80,425,95,width=1,fill="blue") #Enviando Trama
	estado=interruptor()
	crearArchivos()
	rep=0
	sleep(1)
	while(estado==1):
		root.update()
		canvas.create_oval(410,50,425,65,fill="red") #Encendido/Apagado
		f.write("q0=Encendido\n")
		crearTrama()
		seccionarArchivo(rep)
		validar()
		canvas.create_oval(410,80,425,95,fill="red") #Enviando Trama
		f.write("q1=Generacion y Validacion de Trama\n")
		sleep(1)
		root.update()
		canvas.create_oval(410,80,425,95) #Enviando Trama
		estado=interruptor()
		root.update()
		canvas.create_oval(410,50,425,65,fill="blue") #Encendido/Apagado
		canvas.create_oval(410,80,425,95,width=1,fill="blue") #Enviando Trama
		sleep(1)
		rep+=1
	root.update()
	f.write("q0=Apagado")
	canvas.create_oval(410,50,425,65,fill="black") #Encendido/Apagado
	canvas.create_oval(410,80,425,95,width=1,fill="white") #Enviando Trama
	root.mainloop()

grafico()