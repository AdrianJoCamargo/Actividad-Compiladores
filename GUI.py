import tkinter as tk
import tkinter.font as tkFont
from array import array
from asyncio.windows_events import NULL
from pickle import TRUE
from alfabeto import Alfabeto
from lenguaje import Lenguaje
import random
alfabeto1=''
alfabeto2=''
palabras=''
palabras2=''
coun=0

class App:
    def __init__(self, root):
        root.title("undefined")
        width=1200
        height=650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.palTemp1 = tk.StringVar()
        self.palTemp2 = tk.StringVar()
        self.cerrTemp = tk.IntVar()
        self.cerrTemp2 = tk.IntVar()
        self.creacionLen = tk.IntVar()
        self.creacionLen2 = tk.IntVar()


        self.lbl1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        self.lbl1["font"] = ft
        self.lbl1["fg"] = "#333333"
        self.lbl1["justify"] = "center"
        self.lbl1["text"] = "Primero ingrese dos alfabetos"
        self.lbl1.place(x=0,y=10,width=340,height=30)

        self.btn = tk.Button(root)
        self.btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.btn["font"] = ft
        self.btn["fg"] = "#000000"
        self.btn["justify"] = "center"
        self.btn["text"] = "Crear Alfabetos"
        self.btn.place(x=350, y=10, width=95, height=30)
        self.btn["command"] = self.CrearAlfabeB

        self.lbl2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        self.lbl2["font"] = ft
        self.lbl2["fg"] = "#333333"
        self.lbl2["justify"] = "center"
        self.lbl2["text"] = "Alfabeto A"
        self.lbl2.place(x=30,y=50,width=73,height=25)

        self.lbl3=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        self.lbl3["font"] = ft
        self.lbl3["fg"] = "#333333"
        self.lbl3["justify"] = "center"
        self.lbl3["text"] = "Alfabeto B"
        self.lbl3.place(x=30,y=90,width=73,height=25)

        self.ent1=tk.Entry(root)
        self.ent1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.ent1["font"] = ft
        self.ent1["fg"] = "#333333"
        self.ent1["justify"] = "center"
        self.ent1["textvariable"] = self.palTemp1
        self.ent1.place(x=120,y=50,width=461,height=30)

        self.ent2=tk.Entry(root)
        self.ent2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.ent2["font"] = ft
        self.ent2["fg"] = "#333333"
        self.ent2["justify"] = "center"
        self.ent2["textvariable"] = self.palTemp2
        self.ent2.place(x=120,y=90,width=462,height=30)

        self.lbl4=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl4["font"] = ft
        self.lbl4["fg"] = "#333333"
        self.lbl4["text"] = "Union"
        self.lbl4["justify"] = "left"
        self.lbl4.place(x=30,y=170,width=70,height=25)

        self.lbl5=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl5["font"] = ft
        self.lbl5["fg"] = "#333333"
        self.lbl5["justify"] = "left"
        self.lbl5["text"] = "Diferencia"
        self.lbl5.place(x=30,y=200,width=70,height=25)

        self.lbl6=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl6["font"] = ft
        self.lbl6["fg"] = "#333333"
        self.lbl6["justify"] = "left"
        self.lbl6["text"] = "Intersección"
        self.lbl6.place(x=30,y=230,width=70,height=25)

        self.lbl7=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl7["font"] = ft
        self.lbl7["fg"] = "#333333"
        self.lbl7["justify"] = "left"
        self.lbl7["text"] = "Cerradura"
        self.lbl7.place(x=30,y=260,width=70,height=25)

        self.btn1=tk.Button(root)
        self.btn1["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.btn1["font"] = ft
        self.btn1["fg"] = "#000000"
        self.btn1["justify"] = "center"
        self.btn1["text"] = "ClickU"
        self.btn1.place(x=120,y=170,width=70,height=25)
        self.btn1["command"] = self.UnionF

        self.btn2=tk.Button(root)
        self.btn2["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.btn2["font"] = ft
        self.btn2["fg"] = "#000000"
        self.btn2["justify"] = "center"
        self.btn2["text"] = "ClickD"
        self.btn2.place(x=120,y=200,width=70,height=25)
        self.btn2["command"] = self.DiferenciaF

        self.btn3=tk.Button(root)
        self.btn3["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.btn3["font"] = ft
        self.btn3["fg"] = "#000000"
        self.btn3["justify"] = "center"
        self.btn3["text"] = "ClickI"
        self.btn3.place(x=120,y=230,width=70,height=25)
        self.btn3["command"] = self.InterF

        self.btn4=tk.Button(root)
        self.btn4["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.btn4["font"] = ft
        self.btn4["fg"] = "#000000"
        self.btn4["justify"] = "center"
        self.btn4["text"] = "ClickC"
        self.btn4.place(x=120,y=260,width=70,height=25)
        self.btn4["command"] = self.CerraF

        self.btn5=tk.Button(root)
        self.btn5["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.btn5["font"] = ft
        self.btn5["fg"] = "#000000"
        self.btn5["justify"] = "center"
        self.btn5["text"] = "A - B"
        self.btn5.place_forget()
        self.btn5["command"] = self.AmenosB

        self.btn6=tk.Button(root)
        self.btn6["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.btn6["font"] = ft
        self.btn6["fg"] = "#000000"
        self.btn6["justify"] = "center"
        self.btn6["text"] = "B - A"
        self.btn6.place_forget()
        self.btn6["command"] = self.BmenosA

        self.btn7=tk.Button(root)
        self.btn7["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.btn7["font"] = ft
        self.btn7["fg"] = "#000000"
        self.btn7["justify"] = "center"
        self.btn7["text"] = "A"
        self.btn7.place_forget()
        self.btn7["command"] = self.CerraOpA

        self.lbl8=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl8["font"] = ft
        self.lbl8["fg"] = "#333333"
        self.lbl8["justify"] = "left"
        self.lbl8["text"] = "Elija que Alfabeto aplicar cerradura de estrella"
        self.lbl8.place_forget()

        self.btn8=tk.Button(root)
        self.btn8["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.btn8["font"] = ft
        self.btn8["fg"] = "#000000"
        self.btn8["justify"] = "center"
        self.btn8["text"] = "B"
        self.btn8.place_forget()
        self.btn8["command"] = self.CerraOpB

        self.lbl9=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl9["font"] = ft
        self.lbl9["fg"] = "#333333"
        self.lbl9["justify"] = "center"
        self.lbl9["text"] = "¿Cuantas palabras quiere generar?"
        self.lbl9.place_forget()

        self.ent3=tk.Entry(root)
        self.ent3["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.ent3["font"] = ft
        self.ent3["fg"] = "#333333"
        self.ent3["justify"] = "center"
        self.ent3["textvariable"] = self.cerrTemp
        self.ent3.place_forget()

        self.lbl10=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl10["font"] = ft
        self.lbl10["fg"] = "#333333"
        self.lbl10["justify"] = "center"
        self.lbl10["text"] = "Caracteres maximo por palabra"
        self.lbl10.place_forget()

        self.ent4=tk.Entry(root)
        self.ent4["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.ent4["font"] = ft
        self.ent4["fg"] = "#333333"
        self.ent4["justify"] = "center"
        self.ent4["textvariable"] = self.cerrTemp2
        self.ent4.place_forget()

        self.lbl11=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        self.lbl11["font"] = ft
        self.lbl11["fg"] = "#333333"
        self.lbl11["justify"] = "left"
        self.lbl11["text"] = "Resultado de los alfabetos:"
        self.lbl11.place(x=30,y=360,width=193,height=30)

        self.lbl12=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl12["font"] = ft
        self.lbl12["fg"] = "#333333"
        self.lbl12["anchor"] = "w"
        self.lbl12.place(x=30,y=400,width=540,height=170)


        self.Lenlbl1 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        self.Lenlbl1["font"] = ft
        self.Lenlbl1["fg"] = "#333333"
        self.Lenlbl1["justify"] = "center"
        self.Lenlbl1["text"] = "Generar Lenguajes"
        self.Lenlbl1.place(x=518, y=10, width=340, height=30)

        self.Lenlbl = tk.Label(root)
        ft = tkFont.Font(family='Times', size=15)
        self.Lenlbl["font"] = ft
        self.Lenlbl["fg"] = "#333333"
        self.Lenlbl["justify"] = "center"
        self.Lenlbl["text"] = "¿De que Alfabeto?"
        self.Lenlbl.place_forget()

        self.Len2lbl = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        self.Len2lbl["font"] = ft
        self.Len2lbl["fg"] = "#333333"
        self.Len2lbl["justify"] = "center"
        self.Len2lbl["text"] = "¿Cuantas palabras?"
        self.Len2lbl.place_forget()

        self.Len2lbleEn = tk.Entry(root)
        self.Len2lbleEn["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.Len2lbleEn["font"] = ft
        self.Len2lbleEn["fg"] = "#333333"
        self.Len2lbleEn["justify"] = "center"
        self.Len2lbleEn["textvariable"] = self.creacionLen
        self.Len2lbleEn.place_forget()


        self.Len2lbl2 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        self.Len2lbl2["font"] = ft
        self.Len2lbl2["fg"] = "#333333"
        self.Len2lbl2["justify"] = "center"
        self.Len2lbl2["text"] = "¿Maximo de caracteres?"
        self.Len2lbl2.place_forget()

        self.Len2lbleEn2 = tk.Entry(root)
        self.Len2lbleEn2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.Len2lbleEn2["font"] = ft
        self.Len2lbleEn2["fg"] = "#333333"
        self.Len2lbleEn2["justify"] = "center"
        self.Len2lbleEn2["textvariable"] = self.creacionLen2
        self.Len2lbleEn2.place_forget()

        self.Lenbtn = tk.Button(root)
        self.Lenbtn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lenbtn["font"] = ft
        self.Lenbtn["fg"] = "#000000"
        self.Lenbtn["justify"] = "center"
        self.Lenbtn["text"] = "Crear Lenguajes"
        self.Lenbtn.place(x=800, y=10, width=95, height=30)
        self.Lenbtn["command"] = self.GenerarLeng

        self.Lenbtn1 = tk.Button(root)
        self.Lenbtn1["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lenbtn1["font"] = ft
        self.Lenbtn1["fg"] = "#000000"
        self.Lenbtn1["justify"] = "center"
        self.Lenbtn1["text"] = "A"
        self.Lenbtn1.place_forget()
        self.Lenbtn1["command"] = self.GenerarLengA

        self.Lenbtn2 = tk.Button(root)
        self.Lenbtn2["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lenbtn2["font"] = ft
        self.Lenbtn2["fg"] = "#000000"
        self.Lenbtn2["justify"] = "center"
        self.Lenbtn2["text"] = "B"
        self.Lenbtn2.place_forget()
        self.Lenbtn2["command"] = self.GenerarLengB


        self.Lenlbl2 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=13)
        self.Lenlbl2["font"] = ft
        self.Lenlbl2["fg"] = "#333333"
        self.Lenlbl2["justify"] = "center"
        self.Lenlbl2["text"] = "Lenguaje 1"
        self.Lenlbl2.place_forget()

        self.Lenlbl3 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=13)
        self.Lenlbl3["font"] = ft
        self.Lenlbl3["fg"] = "#333333"
        self.Lenlbl3["justify"] = "center"
        self.Lenlbl3["text"] = "Lenguaje 2"
        self.Lenlbl3.place_forget()

        self.Lenlbl4 = tk.Label(root)
        self.Lenlbl4["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.Lenlbl4["font"] = ft
        self.Lenlbl4["fg"] = "#333333"
        self.Lenlbl4["justify"] = "center"
        self.Lenlbl4.place_forget()

        self.Lenlbl5 = tk.Label(root)
        self.Lenlbl5["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.Lenlbl5["font"] = ft
        self.Lenlbl5["fg"] = "#333333"
        self.Lenlbl5["justify"] = "center"
        self.Lenlbl5.place_forget()

        self.Llbl4 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.Llbl4["font"] = ft
        self.Llbl4["fg"] = "#333333"
        self.Llbl4["text"] = "Union"
        self.Llbl4["justify"] = "left"
        self.Llbl4.place_forget()

        self.Llbl5 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.Llbl5["font"] = ft
        self.Llbl5["fg"] = "#333333"
        self.Llbl5["justify"] = "left"
        self.Llbl5["text"] = "Diferencia"
        self.Llbl5.place_forget()

        self.Llbl6 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.Llbl6["font"] = ft
        self.Llbl6["fg"] = "#333333"
        self.Llbl6["justify"] = "left"
        self.Llbl6["text"] = "Intersección"
        self.Llbl6.place_forget()

        self.Llbl7 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.Llbl7["font"] = ft
        self.Llbl7["fg"] = "#333333"
        self.Llbl7["justify"] = "left"
        self.Llbl7["text"] = "Concatenacion"
        self.Llbl7.place_forget()

        self.Llblca = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.Llblca["font"] = ft
        self.Llblca["fg"] = "#333333"
        self.Llblca["justify"] = "left"
        self.Llblca["text"] = "Cardinalidad"
        self.Llblca.place_forget()

        self.Llblin = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.Llblin["font"] = ft
        self.Llblin["fg"] = "#333333"
        self.Llblin["justify"] = "left"
        self.Llblin["text"] = "Inversa"
        self.Llblin.place_forget()

        self.Lbtn1 = tk.Button(root)
        self.Lbtn1["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtn1["font"] = ft
        self.Lbtn1["fg"] = "#000000"
        self.Lbtn1["justify"] = "center"
        self.Lbtn1["text"] = "ClickLU"
        self.Lbtn1.place_forget()
        self.Lbtn1["command"] = self.UnionFL

        self.Lbtn2 = tk.Button(root)
        self.Lbtn2["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtn2["font"] = ft
        self.Lbtn2["fg"] = "#000000"
        self.Lbtn2["justify"] = "center"
        self.Lbtn2["text"] = "ClickLD"
        self.Lbtn2.place_forget()
        self.Lbtn2["command"] = self.DiferenciaFL

        self.Lbtn3 = tk.Button(root)
        self.Lbtn3["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtn3["font"] = ft
        self.Lbtn3["fg"] = "#000000"
        self.Lbtn3["justify"] = "center"
        self.Lbtn3["text"] = "ClickLI"
        self.Lbtn3.place_forget()
        self.Lbtn3["command"] = self.InterFL

        self.Lbtn4 = tk.Button(root)
        self.Lbtn4["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtn4["font"] = ft
        self.Lbtn4["fg"] = "#000000"
        self.Lbtn4["justify"] = "center"
        self.Lbtn4["text"] = "ClickLC"
        self.Lbtn4.place_forget()
        self.Lbtn4["command"] = self.ConcaFL

        self.Lbtn5 = tk.Button(root)
        self.Lbtn5["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtn5["font"] = ft
        self.Lbtn5["fg"] = "#000000"
        self.Lbtn5["justify"] = "center"
        self.Lbtn5["text"] = "A - B"
        self.Lbtn5.place_forget()
        self.Lbtn5["command"] = self.LAmenosB
        self.Lbtn6 = tk.Button(root)
        self.Lbtn6["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtn6["font"] = ft
        self.Lbtn6["fg"] = "#000000"
        self.Lbtn6["justify"] = "center"
        self.Lbtn6["text"] = "B - A"
        self.Lbtn6.place_forget()
        self.Lbtn6["command"] = self.LBmenosA

        self.Lbtn7 = tk.Button(root)
        self.Lbtn7["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtn7["font"] = ft
        self.Lbtn7["fg"] = "#000000"
        self.Lbtn7["justify"] = "center"
        self.Lbtn7["text"] = "A*B"
        self.Lbtn7.place_forget()
        self.Lbtn7["command"] = self.ConcaAB

        self.Lbtn8 = tk.Button(root)
        self.Lbtn8["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtn8["font"] = ft
        self.Lbtn8["fg"] = "#000000"
        self.Lbtn8["justify"] = "center"
        self.Lbtn8["text"] = "B*A"
        self.Lbtn8.place_forget()
        self.Lbtn8["command"] = self.ConcaBA

        self.LbtnCa = tk.Button(root)
        self.LbtnCa["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.LbtnCa["font"] = ft
        self.LbtnCa["fg"] = "#000000"
        self.LbtnCa["justify"] = "center"
        self.LbtnCa["text"] = "ClickLCA"
        self.LbtnCa.place_forget()
        self.LbtnCa["command"] = self.Cardinalidad

        self.Lbtn10 = tk.Button(root)
        self.Lbtn10["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtn10["font"] = ft
        self.Lbtn10["fg"] = "#000000"
        self.Lbtn10["justify"] = "center"
        self.Lbtn10["text"] = "A"
        self.Lbtn10.place_forget()
        self.Lbtn10["command"] = self.CardinalidadA

        self.Lbtn11 = tk.Button(root)
        self.Lbtn11["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtn11["font"] = ft
        self.Lbtn11["fg"] = "#000000"
        self.Lbtn11["justify"] = "center"
        self.Lbtn11["text"] = "B"
        self.Lbtn11.place_forget()
        self.Lbtn11["command"] = self.cardinalidadB

        self.Lbtn9 = tk.Button(root)
        self.Lbtn9["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtn9["font"] = ft
        self.Lbtn9["fg"] = "#000000"
        self.Lbtn9["justify"] = "center"
        self.Lbtn9["text"] = "ClickLI"
        self.Lbtn9.place_forget()
        self.Lbtn9["command"] = self.Inversa

        self.Lbtni1 = tk.Button(root)
        self.Lbtni1["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtni1["font"] = ft
        self.Lbtni1["fg"] = "#000000"
        self.Lbtni1["justify"] = "center"
        self.Lbtni1["text"] = "A"
        self.Lbtni1.place_forget()
        self.Lbtni1["command"] = self.inverA

        self.Lbtni2 = tk.Button(root)
        self.Lbtni2["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.Lbtni2["font"] = ft
        self.Lbtni2["fg"] = "#000000"
        self.Lbtni2["justify"] = "center"
        self.Lbtni2["text"] = "B"
        self.Lbtni2.place_forget()
        self.Lbtni2["command"] = self.inverB

        self.Llbl11 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=13)
        self.Llbl11["font"] = ft
        self.Llbl11["fg"] = "#333333"
        self.Llbl11["justify"] = "left"
        self.Llbl11["text"] = "Resultado de los alfabetos:"
        self.Llbl11.place_forget()

        self.Llbl12 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.Llbl12["font"] = ft
        self.Llbl12["fg"] = "#333333"
        self.Llbl12["anchor"] = "w"
        self.Llbl12.place_forget()

        self.lblIdio = tk.Label(root)
        ft = tkFont.Font(family='Times', size=13)
        self.lblIdio["font"] = ft
        self.lblIdio["fg"] = "#333333"
        self.lblIdio["justify"] = "left"
        self.lblIdio["text"] = "Cambiar idioma:"
        self.lblIdio.place(x=900,y=620,width=110,height=30)

        self.btnIdio = tk.Button(root)
        self.btnIdio["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.btnIdio["font"] = ft
        self.btnIdio["fg"] = "#000000"
        self.btnIdio["justify"] = "center"
        self.btnIdio["text"] = "Español"
        self.btnIdio.place(x=1020,y=620,width=70,height=30)
        self.btnIdio["command"] = self.idiomaES

        self.btnIdio2 = tk.Button(root)
        self.btnIdio2["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.btnIdio2["font"] = ft
        self.btnIdio2["fg"] = "#000000"
        self.btnIdio2["justify"] = "center"
        self.btnIdio2["text"] = "Ingles"
        self.btnIdio2.place(x=1097, y=620, width=70, height=30)
        self.btnIdio2["command"] = self.idiomaIN

    def CrearAlfabeB(self):
        global alfabeto1
        global alfabeto2
        alfabeto1 = Alfabeto()
        alfabeto2 = Alfabeto()
        global palabras
        global palabras2

        palabras = self.palTemp1.get()
        palabras2 = self.palTemp2.get()

        palabras = palabras.split(' ')
        palabras2 = palabras2.split(' ')
        print(palabras,palabras2)

    def UnionF(self):
        if(palabras=='' or palabras2=='' or len(palabras)==1 or len(palabras2)==1):
            self.lbl12["text"] = 'No hay palabras o suficientes palabras por alfabeto'
        else:
            self.lbl12["text"] = alfabeto1.union(palabras,palabras2)



    def DiferenciaF(self):
        self.btn5.place(x=200,y=200,width=70,height=25)
        self.btn6.place(x=280,y=200,width=70,height=25)

    def AmenosB(self):
        if (palabras == '' or palabras2 == '' or len(palabras) == 1 or len(palabras2) == 1):
            self.lbl12["text"] = 'No hay palabras o suficientes palabras por alfabeto'
        else:
            self.lbl12["text"] = alfabeto1.diferencia(palabras,palabras2)
        self.btn5.place_forget()
        self.btn6.place_forget()


    def BmenosA(self):
        if (palabras == '' or palabras2 == '' or len(palabras) == 1 or len(palabras2) == 1):
            self.lbl12["text"] = 'No hay palabras o suficientes palabras por alfabeto'
        else:
            self.lbl12["text"] = alfabeto1.diferencia(palabras2, palabras)
        self.btn5.place_forget()
        self.btn6.place_forget()


    def InterF(self):
        if (palabras == '' or palabras2 == '' or len(palabras) == 1 or len(palabras2) == 1):
            self.lbl12["text"] = 'No hay palabras o suficientes palabras por alfabeto'
        else:
            if (len(alfabeto1.interseccion(palabras, palabras2))):
                self.lbl12["text"] = alfabeto1.interseccion(palabras, palabras2)
            else:
                self.lbl12["text"] = 'no hay elementos comunes entre los 2 alfabetos'


    def CerraF(self):
        self.lbl8.place(x=200,y=260,width=268,height=30)
        self.btn7.place(x=230,y=300,width=70,height=25)
        self.btn8.place(x=330,y=300,width=70,height=25)
        self.lbl9.place(x=470,y=260,width=206,height=30)
        self.ent3.place(x=530,y=300,width=81,height=30)
        self.lbl10.place(x=468,y=331,width=213,height=30)
        self.ent4.place(x=530,y=361,width=81,height=30)

    def CerraOpA(self):
        if (palabras == '' or palabras2 == '' or len(palabras) == 1 or len(palabras2) == 1):
            self.lbl12["text"] = 'No hay palabras o suficientes palabras por alfabeto'
        else:
            array=alfabeto1.cerraduraDeEstrella(palabras,self.cerrTemp.get(),self.cerrTemp2.get())
            self.lbl12["text"] = array
            array.clear()

        self.lbl8.place_forget()
        self.btn7.place_forget()
        self.btn8.place_forget()
        self.lbl9.place_forget()
        self.ent3.place_forget()
        self.lbl10.place_forget()
        self.ent4.place_forget()

    def CerraOpB(self):
        if (palabras == '' or palabras2 == '' or len(palabras) == 1 or len(palabras2) == 1):
            self.lbl12["text"] = 'No hay palabras o suficientes palabras por alfabeto'
        else:
            array = alfabeto1.cerraduraDeEstrella(palabras2, self.cerrTemp.get(), self.cerrTemp2.get())
            self.lbl12["text"] = array
            array.clear()

        self.lbl8.place_forget()
        self.btn7.place_forget()
        self.btn8.place_forget()
        self.lbl9.place_forget()
        self.ent3.place_forget()
        self.lbl10.place_forget()
        self.ent4.place_forget()


    def GenerarLeng(self):
        self.Len2lbl2.place(x=808,y=80,width=340,height=30)
        self.Lenlbl.place(x=808, y=10, width=340, height=30)
        self.Lenbtn1.place(x=1068, y=10, width=30, height=30)
        self.Lenbtn2.place(x=1110, y=10, width=30, height=30)
        self.Len2lbl.place(x=808,y=50,width=340,height=30)
        self.Len2lbleEn.place(x=1070,y=50,width=30,height=30)
        self.Len2lbl2.place(x=808, y=80, width=340, height=30)
        self.Len2lbleEn2.place(x=1070, y=80, width=30, height=30)
        self.Lenlbl2.place_forget()
        self.Lenlbl3.place_forget()
        self.Lenlbl4.place_forget()
        self.Lenlbl5.place_forget()

    def GenerarLengA(self):
        global lenguaje1
        global lenguaje2
        lenguaje1 = Lenguaje(palabras, self.creacionLen.get(), self.creacionLen2.get())
        lenguaje2 = Lenguaje(palabras, self.creacionLen.get(), self.creacionLen2.get())
        self.Lenlbl4["text"]=lenguaje1.getPalabrasDelLenguaje()
        self.Lenlbl5["text"]=lenguaje2.getPalabrasDelLenguaje()
        self.Lenlbl.place_forget()
        self.Lenbtn1.place_forget()
        self.Lenbtn2.place_forget()
        self.Lenlbl2.place(x=600, y=50, width=75, height=25)
        self.Lenlbl3.place(x=600, y=90, width=75, height=25)
        self.Lenlbl4.place(x=690, y=50, width=455, height=30)
        self.Lenlbl5.place(x=690, y=90, width=455, height=30)
        self.Len2lbl.place_forget()
        self.Len2lbl2.place_forget()
        self.Len2lbleEn.place_forget()
        self.Len2lbleEn2.place_forget()
        self.Llbl4.place(x=1075, y=170, width=70, height=25)
        self.Llbl5.place(x=1075, y=200, width=70, height=25)
        self.Llbl6.place(x=1075, y=230, width=70, height=25)
        self.Llbl7.place(x=1070, y=260, width=80, height=25)
        self.Llblca.place(x=1070, y=290, width=80, height=25)
        self.Llblin.place(x=1070, y=320, width=80, height=25)
        self.Lbtn1.place(x=980, y=170, width=70, height=25)
        self.Lbtn2.place(x=980, y=200, width=70, height=25)
        self.Lbtn3.place(x=980, y=230, width=70, height=25)
        self.Lbtn4.place(x=980, y=260, width=70, height=25)
        self.LbtnCa.place(x=980, y=290, width=70, height=25)
        self.Lbtn9.place(x=980, y=320, width=70, height=25)
        self.Llbl11.place(x=600, y=360, width=193, height=30)
        self.Llbl12.place(x=600, y=400, width=540, height=170)

    def GenerarLengB(self):
        global lenguaje1
        global lenguaje2
        lenguaje1 = Lenguaje(palabras2, self.creacionLen.get(), self.creacionLen2.get())
        lenguaje2 = Lenguaje(palabras2, self.creacionLen.get(), self.creacionLen2.get())
        self.Lenlbl4["text"] = lenguaje1.getPalabrasDelLenguaje()
        self.Lenlbl5["text"] = lenguaje2.getPalabrasDelLenguaje()

        self.Lenlbl.place_forget()
        self.Lenbtn1.place_forget()
        self.Lenbtn2.place_forget()
        self.Lenlbl2.place(x=600, y=50, width=75, height=25)
        self.Lenlbl3.place(x=600, y=90, width=75, height=25)
        self.Lenlbl4.place(x=690, y=50, width=455, height=30)
        self.Lenlbl5.place(x=690, y=90, width=455, height=30)
        self.Len2lbl.place_forget()
        self.Len2lbl2.place_forget()
        self.Len2lbleEn.place_forget()
        self.Len2lbleEn2.place_forget()
        self.Llbl4.place(x=1075, y=170, width=70, height=25)
        self.Llbl5.place(x=1075, y=200, width=70, height=25)
        self.Llbl6.place(x=1075, y=230, width=70, height=25)
        self.Llbl7.place(x=1070, y=260, width=80, height=25)
        self.Llblca.place(x=1070, y=290, width=80, height=25)
        self.Llblin.place(x=1070, y=320, width=80, height=25)
        self.Lbtn1.place(x=980, y=170, width=70, height=25)
        self.Lbtn2.place(x=980, y=200, width=70, height=25)
        self.Lbtn3.place(x=980, y=230, width=70, height=25)
        self.Lbtn4.place(x=980, y=260, width=70, height=25)
        self.LbtnCa.place(x=980, y=290, width=70, height=25)
        self.Lbtn9.place(x=980, y=320, width=70, height=25)
        self.Llbl11.place(x=600, y=360, width=193, height=30)
        self.Llbl12.place(x=600, y=400, width=540, height=170)

    def UnionFL(self):
        self.Llbl12["text"] = lenguaje1.union(lenguaje2)

    def DiferenciaFL(self):
        self.Lbtn5.place(x=900, y=200, width=70, height=25)
        self.Lbtn6.place(x=820, y=200, width=70, height=25)

    def LAmenosB(self):
        self.Llbl12["text"] = lenguaje1.diferencia(lenguaje1.getPalabrasDelLenguaje(), lenguaje2.getPalabrasDelLenguaje())
        self.Lbtn5.place_forget()
        self.Lbtn6.place_forget()

    def LBmenosA(self):
        self.Llbl12["text"] = lenguaje2.diferencia(lenguaje2.getPalabrasDelLenguaje(), lenguaje1.getPalabrasDelLenguaje())
        self.Lbtn5.place_forget()
        self.Lbtn6.place_forget()

    def ConcaFL(self):
        self.Lbtn7.place(x=900, y=260, width=70, height=25)
        self.Lbtn8.place(x=820, y=260, width=70, height=25)

    def ConcaAB(self):
        self.Llbl12["text"] =lenguaje1.concatenacion(lenguaje2)
        self.Lbtn7.place_forget()
        self.Lbtn8.place_forget()

    def ConcaBA(self):
        self.Llbl12["text"] =lenguaje2.concatenacion(lenguaje1)
        self.Lbtn7.place_forget()
        self.Lbtn8.place_forget()

    def Cardinalidad(self):
        self.Lbtn10.place(x=900, y=290, width=70, height=25)
        self.Lbtn11.place(x=820, y=290, width=70, height=25)

    def CardinalidadA(self):
        self.Llbl12["text"] = lenguaje1.cardinalidad()
        self.Lbtn10.place_forget()
        self.Lbtn11.place_forget()

    def cardinalidadB(self):
        self.Llbl12["text"] = lenguaje2.cardinalidad()
        self.Lbtn10.place_forget()
        self.Lbtn11.place_forget()

    def InterFL(self):
        l1 = lenguaje1.getPalabrasDelLenguaje()
        l2 = lenguaje2.getPalabrasDelLenguaje()
        self.Llbl12["text"] = lenguaje1.interseccion(l1, l2)

    def Inversa(self):
        self.Lbtni1.place(x=900,y=320,width=70,height=25)
        self.Lbtni2.place(x=820, y=320, width=70, height=25)

    def inverA(self):
        self.Llbl12["text"] =lenguaje1.inversa()
        self.Lbtni1.place_forget()
        self.Lbtni2.place_forget()
    def inverB(self):
        self.Llbl12["text"] =lenguaje2.inversa()
        self.Lbtni2.place_forget()
        self.Lbtni1.place_forget()

    def idiomaES(self):
        self.lbl1["text"] = "Primero ingrese dos alfabetos"
        self.btn["text"] = "Crear Alfabetos"
        self.lbl2["text"] = "Alfabeto A"
        self.lbl3["text"] = "Alfabeto B"
        self.lbl4["text"] = "Union"
        self.lbl5["text"] = "Diferencia"
        self.lbl6["text"] = "Intersección"
        self.lbl7["text"] = "Cerradura"
        self.lbl8["text"] = "Elija que Alfabeto aplicar cerradura de estrella"
        self.lbl9["text"] = "¿Cuantas palabras quiere generar?"
        self.lbl10["text"] = "Caracteres maximo por palabra"
        self.lbl11["text"] = "Resultado de los alfabetos:"
        self.Lenlbl1["text"] = "Generar Lenguajes"
        self.Lenlbl["text"] = "¿De que Alfabeto?"
        self.Len2lbl["text"] = "¿Cuantas palabras?"
        self.Len2lbl2["text"] = "¿Maximo de caracteres?"
        self.Lenbtn["text"] = "Crear Lenguajes"
        self.Lenlbl2["text"] = "Lenguaje 1"
        self.Lenlbl3["text"] = "Lenguaje 2"
        self.Llbl4["text"] = "Union"
        self.Llbl5["text"] = "Diferencia"
        self.Llbl6["text"] = "Intersección"
        self.Llbl7["text"] = "Concatenacion"
        self.Llblca["text"] = "Cardinalidad"
        self.Llblin["text"] = "Inversa"
        self.Llbl11["text"] = "Resultado de los alfabetos:"
        self.lblIdio["text"] = "Cambiar idioma:"
        self.btnIdio["text"] = "Español"
        self.btnIdio2["text"] = "Ingles"

    def idiomaIN(self):
        self.lbl1["text"] = "First enter two alphabets"
        self.btn["text"] = "Create Alphabets"
        self.lbl2["text"] = "Alphabet A"
        self.lbl3["text"] = "Alphabet B"
        self.lbl4["text"] = "Union"
        self.lbl5["text"] = "Difference"
        self.lbl6["text"] = "Intersection"
        self.lbl7["text"] = "Star Lock"
        self.lbl8["text"] = "Choose which Alphabet to apply Star Lock"
        self.lbl9["text"] = "Words to generate?"
        self.lbl10["text"] = "Maximum characters per word"
        self.lbl11["text"] = "Result of the alphabets:"
        self.Lenlbl1["text"] = "Generate Languages"
        self.Lenlbl["text"] = "Which Alphabet?"
        self.Len2lbl["text"] = "How many words?"
        self.Len2lbl2["text"] = "Max characters?"
        self.Lenbtn["text"] = "Create Language"
        self.Lenlbl2["text"] = "Language 1"
        self.Lenlbl3["text"] = "Language 2"
        self.Llbl4["text"] = "Union"
        self.Llbl5["text"] = "Difference"
        self.Llbl6["text"] = "Intersection"
        self.Llbl7["text"] = "Concatenation"
        self.Llblca["text"] = "Cardinality"
        self.Llblin["text"] = "Reverse"
        self.Llbl11["text"] = "Result of the alphabets:"
        self.lblIdio["text"] = "language:"
        self.btnIdio["text"] = "Spanish"
        self.btnIdio2["text"] = "English"


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
