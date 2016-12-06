from tkinter import *
def grafico():
	root = 	Tk()
	root.title('Automata Terminacion "web/ebay" Grafico') # Nombre de la ventana
	canvas=Canvas(root,width=1000,height=700)
	canvas.pack()

	canvas.create_oval(100, 300, 200, 400) #Circulo 0
	canvas.create_arc(180,340,30,360, start=90, extent=180, style='arc') #arco 0-0
	canvas.create_oval(90,355,100,365,fill="red")
	#canvas.create_line(0,350,100,350)#Linea incial
	canvas.create_line(200,340,300,250)#Linea 0-1
	canvas.create_oval(290,250,300,260,fill="red")
	canvas.create_line(200,360,300,450)#Linea 0-4
	canvas.create_oval(290,440,300,450,fill="red")
	canvas.create_arc(150,700,950,0, start=188, extent=149, style='arc') #arco 0-7
	canvas.create_arc(150,600,800,125, start=188, extent=138, style='arc') #arco 0-6
	canvas.create_arc(150,550,600,180, start=190, extent=125, style='arc') #arco 0-5
	canvas.create_arc(150,495,450,265, start=190, extent=92, style='arc') #arco 0-4
	canvas.create_oval(150,400,160,410,fill="red")

	canvas.create_oval(300, 200, 400, 300) #Circulo 1
	canvas.create_line(400,250,500,250)#Linea 1-2
	canvas.create_oval(490,245,500,255,fill="red")
	canvas.create_arc(150,350,340,200, start=45, extent=150, style='arc') #arco 1-0
	canvas.create_oval(145,290,155,300,fill="red")
	canvas.create_arc(370,205,330,160, start=300, extent=300, style='arc') #arco 1-1
	canvas.create_oval(330,195,340,205,fill="red")
	canvas.create_arc(370,205,330,160, start=300, extent=300, style='arc') #arco 1-1

	canvas.create_oval(500, 200, 600, 300) #Circulo 2
	canvas.create_line(600,250,700,250)#Linea 2-3
	canvas.create_oval(690,245,700,255,fill="red")
	canvas.create_arc(525,200,375,240, start=20, extent=140, style='arc') #arco 2-1
	canvas.create_oval(380,205,390,215,fill="red")
	canvas.create_arc(550,150,150,360, start=28, extent=158, style='arc') #arco 2-0
	canvas.create_line(550,300,370,405)#Linea 2-4

	canvas.create_oval(700, 200, 800, 300, width=3) #Circulo 3
	canvas.create_arc(720,70,150,380, start=5, extent=180, style='arc') #arco 3-0
	canvas.create_arc(725,190,380,240, start=10, extent=150, style='arc') #arco 3-1
	canvas.create_line(750,300,370,405)#Linea 3-4
	canvas.create_oval(370,405,380,395,fill="red")

	canvas.create_oval(300, 400, 400, 500) #Circulo 4
	canvas.create_line(400,450,500,450)#Linea 4-5
	canvas.create_oval(490,445,500,455,fill="red")
	canvas.create_arc(290,460,310,480, start=95, extent=255, style='arc') #arco 4-4
	canvas.create_oval(300,480,310,470,fill="red")
	canvas.create_arc(370,450,520,500, start=210, extent=125, style='arc') #arco 4-5
	canvas.create_arc(370,440,720,550, start=180, extent=185, style='arc') #arco 4-6
	canvas.create_arc(370,400,905,600, start=180, extent=173, style='arc') #arco 4-7
	canvas.create_oval(365,495,375,505,fill="red")
	canvas.create_oval(380,485,390,495,fill="red")
	canvas.create_line(350,400,350,300)#Linea 4-1
	canvas.create_oval(345,300,355,310,fill="red")

	canvas.create_oval(500, 400, 600, 500) #Circulo 5
	canvas.create_line(600,450,700,450)#Linea 5-6
	canvas.create_oval(690,445,700,455,fill="red")
	canvas.create_line(550,400,355,305)#Linea 5-1

	canvas.create_oval(700, 400, 800, 500) #Circulo 6
	canvas.create_line(800,450,900,450)#Linea 6-7
	canvas.create_oval(890,445,900,455,fill="red")
	canvas.create_line(750,400,355,305)#Linea 6-1
	canvas.create_line(750,300,770,408)#Linea 3-6
	canvas.create_oval(765,408,775,398,fill="red")

	canvas.create_oval(900,400,1000,500, width=3)#Circulo 7
	canvas.create_line(950,400,355,305)#Linea 7-1

	#Estados
	letra=Label(root,text="Q0",font=("Helvetica",15))
	letra.place(x=125,y=330)
	letra=Label(root,text="Q1",font=("Helvetica",15))
	letra.place(x=330,y=225)
	letra=Label(root,text="Q2",font=("Helvetica",15))
	letra.place(x=530,y=225)
	letra=Label(root,text="Q3",font=("Helvetica",15))
	letra.place(x=730,y=225)
	letra=Label(root,text="Q4",font=("Helvetica",15))
	letra.place(x=330,y=425)
	letra=Label(root,text="Q5",font=("Helvetica",15))
	letra.place(x=530,y=425)
	letra=Label(root,text="Q6",font=("Helvetica",15))
	letra.place(x=730,y=425)
	letra=Label(root,text="Q7",font=("Helvetica",15))
	letra.place(x=930,y=425)
	#Letras e
	letra=Label(root,text="e")
	letra.place(x=250,y=400)
	letra=Label(root,text="e")
	letra.place(x=390,y=375)
	letra=Label(root,text="e")
	letra.place(x=690,y=295)
	letra=Label(root,text="e")
	letra.place(x=280,y=450)
	letra=Label(root,text="e")
	letra.place(x=430,y=490)
	letra=Label(root,text="e")
	letra.place(x=550,y=540)
	letra=Label(root,text="e")
	letra.place(x=690,y=585)
	letra=Label(root,text="e")
	letra.place(x=450,y=230)
	#Letras b
	letra=Label(root,text="b")
	letra.place(x=650,y=230)
	letra=Label(root,text="b")
	letra.place(x=450,y=430)
	#Letras a
	letra=Label(root,text="a")
	letra.place(x=650,y=430)
	letra=Label(root,text="a")
	letra.place(x=750,y=330)
	#Letras y
	letra=Label(root,text="y")
	letra.place(x=850,y=430)
	#Letras compuestas
	letra=Label(root,text="E-e-w")
	letra.place(x=20,y=330)
	letra=Label(root,text="E-e-w")
	letra.place(x=220,y=180)
	letra=Label(root,text="E-b-e-w")
	letra.place(x=270,y=150)
	letra=Label(root,text="E-a-e-w")
	letra.place(x=430,y=80)
	letra=Label(root,text="E-b-e-w")
	letra.place(x=220,y=475)
	letra=Label(root,text="E-a-e-w")
	letra.place(x=320,y=530)
	letra=Label(root,text="E-y-e-w")
	letra.place(x=340,y=570)
	letra=Label(root,text="E-e-w")
	letra.place(x=450,y=650)
	# Letras w
	letra=Label(root,text="w")
	letra.place(x=650,y=180)
	letra=Label(root,text="w")
	letra.place(x=340,y=160)
	letra=Label(root,text="w")
	letra.place(x=450,y=200)
	letra=Label(root,text="w")
	letra.place(x=420,y=330)
	letra=Label(root,text="w")
	letra.place(x=600,y=360)
	letra=Label(root,text="w")
	letra.place(x=850,y=380)
	letra=Label(root,text="w")
	letra.place(x=340,y=350)
	letra=Label(root,text="w")
	letra.pack()
	letra.place(x=250,y=300)
	root.mainloop()