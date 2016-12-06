#Pila
class Pila:
	lista=[]
	tope=0
	estado=""

	def inicializarPila(self):
		self.lista.append('Zo')
		self.lista.append(None)
		self.tope=1
		self.estado="q"

	def push(self):
		self.lista[self.tope]='X'
		self.lista.append(None)
		self.tope+=1

	def pop(self):
		del(self.lista[self.tope])
		self.tope-=1
		self.lista[self.tope]=None

	def mostrar(self):
		cad=""
		x=len(self.lista)-2
		while(x>=0):
			cad+=str(self.lista[x])
			x-=1
		return cad

	def esVacia(self):
		if(self.tope==1):
			return 1
		else:
			return 0

