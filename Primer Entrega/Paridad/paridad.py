from tkinter import *
from random import *

def guardarPalabra(cadena):
	filtro = open("cadenas.txt","a")
	filtro.write(cadena)
	filtro.close()

def crearArchivos():
	cadenas=open("cadenas.txt","w")
	cadenas.close()
	estados=open("estados.txt","w")
	estados.close()

def automata(cadena):
	estado = 0
	estados=open("estados.txt","a")
	x=0
	while(cadena[x]!=' '):
		if(estado==0):
			estados.write('estado'+str(estado)+"-"+cadena[x]+" ")
			if(cadena[x]=='0'):
				estado=1
			elif(cadena[x]=='1'):
				estado=2
			elif(cadena[x+1]==' '):
				estado=0
		elif(estado==1):
			estados.write('estado'+str(estado)+"-"+cadena[x]+" ")
			if(cadena[x]=='0'):
				estado=0
			elif(cadena[x]=='1'):
				estado=3
		elif(estado==2):
			estados.write('estado'+str(estado)+"-"+cadena[x]+" ")
			if(cadena[x]=='0'):
				estado=3
			elif(cadena[x]=='1'):
				estado=0
		elif(estado==3):
			estados.write('estado'+str(estado)+"-"+cadena[x]+" ")
			if(cadena[x]=='0'):
				estado=2
			elif(cadena[x]=='1'):
				estado=1
		x+=1
	estados.write("estado"+str(estado) +" ")
	if(estado==0):
		return 1
	else:
		return 0

def manual():
	cadena=input("Ingresa la cadena ==> ")
	if(automata(cadena+' ')==1):
		guardarPalabra(cadena+' ')
		print ("Cadena valida")
	else:
		print("Cadena invalida")

def auto():
	f = open("archivo.txt","r")
	cadena=""
	linea=f.readline()
	while(linea != ''):
		x=0
		cad=linea+'\n'
		while(cad[x]!='\n'):
			if(cad[x]=='1' or cad[x]=='0' or cad[x]==' '):
				cadena+=cad[x]
				if(cad[x]==' ' and (cad[x-1]=='0' or cad[x-1]=='1')):
					if(automata(cadena)==1):
						guardarPalabra(cadena)
					cadena=""
			else:
				cadena=""
			x+=1
		linea=f.readline()
	f.close()

def grafico():
	root = 	Tk()
	root.title('Automata Pariedad Grafico') # Nombre de la ventana
	canvas=Canvas(root,width=400,height=400)
	canvas.pack()
	canvas.create_arc(90,5,320,95, start=0, extent=180, style='arc') #arco 1-2 arriba
	canvas.create_arc(90,10,320,100, start=360, extent=-180, style='arc') #arco 1-2 abajo
	canvas.create_arc(90,310,320,400, start=0, extent=180, style='arc') #arco 2-3 arriba
	canvas.create_arc(90,310,320,400, start=360, extent=-180, style='arc') #arco 2-3 abajo
	canvas.create_arc(310,95,400,320, start=90, extent=-180, style='arc') #arco 1-2 derecho
	canvas.create_arc(310,95,400,320, start=90, extent=180, style='arc') #arco 1-2 izquierdo
	canvas.create_arc(10,95,100,320, start=90, extent=-180, style='arc') #arco 2-4 derecho
	canvas.create_arc(10,95,100,320, start=90, extent=180, style='arc') #arco 2-4 izquierdo
	canvas.create_oval(10, 10, 100, 100, width=1, fill='green') #Primer Circulo
	canvas.create_oval(7, 7, 103, 103)
	canvas.create_oval(310, 10, 400, 100, width=1, fill='blue') #Segundo Circulo
	canvas.create_oval(10, 310, 100, 400, width=1, fill='black') #Tercer circulo
	canvas.create_oval(310, 310, 400, 400, width=1, fill='yellow') #Cuarto circulo
	canvas.create_oval(95,30,105,40,fill="red") #Flecha 1-0
	canvas.create_oval(305,70,315,80,fill="red") #Flecha 0-1
	canvas.create_oval(95,330,105,340,fill="red") #Flecha 3-2
	canvas.create_oval(305,370,315,380,fill="red") #Flecha 2-3
	canvas.create_oval(35,98,45,108,fill="red") #Flecha 2-1
	canvas.create_oval(70,305,80,315,fill="red") #Flecha 1-2
	canvas.create_oval(335,98,345,108,fill="red") #Flecha 3-1
	canvas.create_oval(370,305,380,315,fill="red") #Flecha 1-3
	canvas.create_line(0,45,10,45)
	canvas.create_oval(3,42,13,52,fill="red") #Flecha 0-0
	estado=Label(root,text="Estado 0",bg="green",font=("Helvetica",12),fg="white") #ESTADO CERO
	estado.place(x = 20, y = 40)
	estado=Label(root,text="Estado 1",bg="blue",font=("Helvetica",12),fg="white") #ESTADO UNO
	estado.place(x = 320, y = 40)
	estado=Label(root,text="Estado 2",bg="black",font=("Helvetica",12),fg="white") #ESTADO DOS
	estado.place(x = 20, y = 340)
	estado=Label(root,text="Estado 3",bg="yellow",font=("Helvetica",12),fg="black") #ESTADO TRES
	estado.pack()
	estado.place(x = 320, y = 340)
	cero=Label(root,text="0",font=("Helvetica",12)) # CERO 1 ARRIBA
	cero.place(x = 200, y = -2)
	cero=Label(root,text="0",font=("Helvetica",12)) # CERO 1 ABAJO
	cero.place(x = 200, y = 90)
	cero=Label(root,text="0",font=("Helvetica",12)) # CERO 2 ARRIBA
	cero.place(x = 200, y = 300)
	cero=Label(root,text="0",font=("Helvetica",12)) # CERO 1 ABAJO
	cero.pack()
	cero.place(x = 200, y = 380)
	uno=Label(root,text="1",font=("Helvetica",12)) # UNO 1 IZQUIERDA
	uno.place(x = 5, y = 192)
	uno=Label(root,text="1",font=("Helvetica",12)) # UNO 1 DERECHA
	uno.place(x = 90, y = 195)
	uno=Label(root,text="1",font=("Helvetica",12)) # UNO 2 IZQUIERDA
	uno.place(x = 300, y = 195)
	uno=Label(root,text="1",font=("Helvetica",12)) # UNO 2 DERECHA
	uno.pack()
	uno.place(x = 390, y = 195)
	root.mainloop()

def repetir(modo):
	opc=0
	while(opc!=2):
		if(modo==1):
			opc=int(input("Deseas repetir? 1.Si 2.No \n ==> "))
			if(opc==1):
				print("Has seleccionado repetir")
				manual()
			elif(opc==2):
				print ("Adios")
			else:
				print("Opcion incorrecta")
		if(modo==2):
			print("Deseas repetir? 1.Si 2.No \n ==> ")
			opc=randint(1,2)
			if(opc==1):
				print("Has seleccionado repetir")
				auto()
			if(opc==2):
				print ("Adios")

def menu():
	crearArchivos()
	opcion=-1
	while(opcion>2 or opcion<1):
		print ("Selecciona una opcion")
		opcion=int(input("1. Manual\n2. Automatico \n3. Mostrar Grafico \n4. Salir\n ==> "))
		if(opcion==1):
			print("Opcion Manual Seleccionada")
			manual()
			repetir(opcion)
		elif(opcion==2):
			print("Opcion Automatica Seleccionada")
			auto()
			repetir(opcion)
		elif(opcion==3):
			grafico()
		elif(opcion==4):
			break
		else:
			print ("Opcion Equivocada")	

menu()