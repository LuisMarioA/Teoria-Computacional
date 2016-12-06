from random import *
def generarCadena(n):
	f=open("proceso.txt","a")
	cadena=""
	if(n%2==0):
		rep=0
		while(rep<(n/2)):
			numero=randint(1,2)
			if(numero==1):
				cadena+="0"
				cadenaDos=invertir(cadena)
				#print(" 0P0 | "+cadena+"P"+cadenaDos)
				f.write(" 0P0 | "+cadena+"P"+cadenaDos+"\n")
			if(numero==2):
				cadena+="1"
				cadenaDos=invertir(cadena)
				#print(" 1P1 | "+cadena+"P"+cadenaDos)
				f.write(" 1P1 | "+cadena+"P"+cadenaDos+"\n")
			rep+=1
		cadenaDos=invertir(cadena)
		#print("  e  | "+cadena+"e"+cadenaDos)
		f.write("  e  | "+cadena+"e"+cadenaDos+"\n")
		cadena=cadena+cadenaDos
	else:
		rep=0
		while(rep<(n/2)-0.5):
			numero=randint(1,2)
			if(numero==1):
				cadena+="0"
				cadenaDos=invertir(cadena)
				#print(" 0P0 | "+cadena+"P"+cadenaDos)
				f.write(" 0P0 | "+cadena+"P"+cadenaDos+"\n")
			if(numero==2):
				cadena+="1"
				cadenaDos=invertir(cadena)
				#print(" 1P1 | "+cadena+"P"+cadenaDos)
				f.write(" 1P1 | "+cadena+"P"+cadenaDos+"\n")
			rep+=1
		cadenaDos=invertir(cadena)
		numero=randint(1,2)
		if(numero==1):
			cadena+="0"
			cadena=cadena+cadenaDos
			#print("  0  | "+cadena)
			f.write("  0  | "+cadena+"\n")
		elif(numero==2):
			cadena+="1"
			cadena=cadena+cadenaDos
			#print("  1  | "+cadena)
			f.write("  1  | "+cadena+"\n")
	print("El palindromo binario generado es "+cadena)
	f.write("El palindromo binario generado es "+cadena+"\n\n")
	f.close()

def invertir(cadena):
        return cadena[::-1]

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
	numero=int(input("Ingresa el numero "))
	generarCadena(numero)
	repetir(1)

def auto():
	numero=randint(0,1000)
	print("El numero seleccionado es "+str(numero))
	generarCadena(numero)
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