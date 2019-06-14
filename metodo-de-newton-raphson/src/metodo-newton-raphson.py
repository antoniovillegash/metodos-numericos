from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

def derivada_simple(funcion):
  
  #se le asignara una lista con la funcion en orden c, x1, x2...
  #la estructura deberá ser funcion [[coeficiente,exponente],[coeficiente,exponente] ]
  
  for i in range(len(funcion)):
    if(funcion[i][1]==0):
      funcion[0][0]=0
    elif(funcion[i][1]==1):
      funcion[0][0]+=funcion[i][0]
      funcion[0][1]=0
    else:
      funcion[i-1][0]=funcion[i][0]*funcion[i][1]
      funcion[i-1][1]=funcion[i][1]-1
  funcion.pop()
  return funcion

def main_screen():
    root=Tk()
    
    root.title("Metodo de Newton-Raphson")
    root.resizable(False,False)
   
    frame_ecuacion=Frame(root,height="100", width="548")
    frame_ecuacion.pack()
    frame_ecuacion.config(bd="1", relief="sunken")
    
    #ecuacion 
    Label(frame_ecuacion,text="Ecuación", font=("quicksand",13)).place(x=0,y=0)
    
    x6=StringVar()
    Entry(frame_ecuacion,width="3",font=("quicksand",12),textvariable=x6).place(x=10,y=30)
    x6.set('0')
    Label(frame_ecuacion,text="x⁶ +",font=("quicksand",12)).place(x=45,y=29)
    
    x5=StringVar()
    Entry(frame_ecuacion,width="3",font=("quicksand",12),textvariable=x5).place(x=90,y=30)
    x5.set('0')
    Label(frame_ecuacion,text="x⁵ +",font=("quicksand",12)).place(x=125,y=29)
    
    x4=StringVar()
    Entry(frame_ecuacion,width="3",font=("quicksand",12),textvariable=x4).place(x=170,y=30)
    x4.set('0')
    Label(frame_ecuacion,text="x⁴ +",font=("quicksand",12)).place(x=205,y=29)
    
    x3=StringVar()
    Entry(frame_ecuacion,width="3",font=("quicksand",12),textvariable=x3).place(x=250,y=30)
    x3.set('0')
    Label(frame_ecuacion,text="x³ +",font=("quicksand",12)).place(x=285,y=29)
    
    x2=StringVar()
    Entry(frame_ecuacion,width="3",font=("quicksand",12),textvariable=x2).place(x=330,y=30)
    x2.set('0')
    Label(frame_ecuacion,text="x² +",font=("quicksand",12)).place(x=365,y=29)
    
    x1=StringVar()
    Entry(frame_ecuacion,width="3",font=("quicksand",12),textvariable=x1).place(x=410,y=30)
    x1.set('0')
    Label(frame_ecuacion,text="x +",font=("quicksand",12)).place(x=445,y=29)
    
    c=StringVar()
    Entry(frame_ecuacion,width="3",font=("quicksand",12),textvariable=c).place(x=490,y=30)
    c.set('0')
    Label(frame_ecuacion,text="C",font=("quicksand",12)).place(x=525,y=29)
     #derivadas
    frame_ecuacion_derivada=Frame(root,height="100", width="548")
    frame_ecuacion_derivada.pack()
    frame_ecuacion_derivada.config(bd="1", relief="sunken")
    
    #ecuacion  derivada
    Label(frame_ecuacion_derivada,text="Función derivada", font=("quicksand",13)).place(x=0,y=0)
    
    x5_derivada=StringVar()
    Entry(frame_ecuacion_derivada,width="3",font=("quicksand",12),textvariable=x5_derivada,state='disabled').place(x=90,y=30)
    x5_derivada.set('0')
    Label(frame_ecuacion_derivada,text="x⁵ +",font=("quicksand",12)).place(x=125,y=29)
    
    x4_derivada=StringVar()
    Entry(frame_ecuacion_derivada,width="3",font=("quicksand",12),textvariable=x4_derivada,state='disabled').place(x=170,y=30)
    x4_derivada.set('0')
    Label(frame_ecuacion_derivada,text="x⁴ +",font=("quicksand",12)).place(x=205,y=29)
    
    x3_derivada=StringVar()
    Entry(frame_ecuacion_derivada,width="3",font=("quicksand",12),textvariable=x3_derivada,state='disabled').place(x=250,y=30)
    x3_derivada.set('0')
    Label(frame_ecuacion_derivada,text="x³ +",font=("quicksand",12)).place(x=285,y=29)
    
    x2_derivada=StringVar()
    Entry(frame_ecuacion_derivada,width="3",font=("quicksand",12),textvariable=x2_derivada,state='disabled').place(x=330,y=30)
    x2_derivada.set('0')
    Label(frame_ecuacion_derivada,text="x² +",font=("quicksand",12)).place(x=365,y=29)
    
    x1_derivada=StringVar()
    Entry(frame_ecuacion_derivada,width="3",font=("quicksand",12),textvariable=x1_derivada,state='disabled').place(x=410,y=30)
    x1_derivada.set('0')
    Label(frame_ecuacion_derivada,text="x +",font=("quicksand",12)).place(x=445,y=29)
    
    c_derivada=StringVar()
    Entry(frame_ecuacion_derivada,width="3",font=("quicksand",12),textvariable=c_derivada,state='disabled').place(x=490,y=30)
    c_derivada.set('0')
    Label(frame_ecuacion_derivada,text="C",font=("quicksand",12)).place(x=525,y=29)
  
    
    #error, numero de decimales y valor inicial
    frame_error_decimales=Frame(root,height="130", width="548")
    frame_error_decimales.pack()
    frame_error_decimales.config(bd="1", relief="sunken")
    
    Label(frame_error_decimales,text="Porcentaje de error",font=("quicksand",12)).place(x=0,y=20)
    error=StringVar()
    Entry(frame_error_decimales,width="9",font=("quicksand",12), textvariable=error).place(x=200,y=20)
    error.set(0)
    Label(frame_error_decimales,text="numero de decimales",font=("quicksand",12)).place(x=0,y=52)
    decimales=StringVar()
    Entry(frame_error_decimales,width="2",font=("quicksand",12), textvariable=decimales).place(x=200,y=52)
    decimales.set(0)
    Label(frame_error_decimales,text="valor inicial",font=("quicksand",12)).place(x=0,y=84)
    valor_inicial=StringVar()
    Entry(frame_error_decimales,width="3",font=("quicksand",12), textvariable=valor_inicial).place(x=200,y=84)
    valor_inicial.set(0)
    
    def run():
      validaciones()
      obtener_resultados()
      #es_grado_seis()
      
    def validaciones():
      #ecuacion
      variables=[c.get(),x1.get(),x2.get(),x3.get(),x4.get(),x5.get(),x6.get()]
      print('ecuacion: '+str(variables[0:]))
      for x in range(7):
        try:
          float(variables[x])
          print('todo bien, valor:'+ variables[x])
        except :
          print('error')
          if(x>0):
            messagebox.showinfo("ERROR", "Se ingresó un tipo de dato no valido en la variable x"+'^'+str(x))
          else:
            messagebox.showinfo("ERROR", "Se ingresó un tipo de dato no valido en la constante")
          break
            
      #porcentaje error, decimales y valor inicial
      variables=[error.get(),decimales.get(),valor_inicial.get()]
      print('porcentaje error y decimales: '+str(variables[0:]))
      for x in range(3):
        try:
          float(variables[x])
        except:
          if(x==0):
            messagebox.showinfo("ERROR", "se ingresó un dato no válido en el porcentaje de error")
          elif(x==1):
            messagebox.showinfo("ERROR", "se ingresó un dato no válido en la cantidad de decimales")
          elif(x==2):
            messagebox.showinfo("ERROR", "se ingresó un dato no válido en el valor inicial")
            
    button=Button(frame_error_decimales, text="Calcular",command=run).place(x=460,y=90)
    
    #resultados
    frame_resultados=Frame(root,height="200", width="548")
    frame_resultados.pack()
    frame_resultados.config(bd="1", relief="sunken")
    
    Label(frame_resultados,text="porcentaje de error",font=("quicksand",12)).place(x=0,y=0)
    mostrar_error=Listbox(frame_resultados)
    
    Label(frame_resultados,text="resultado",font=("quicksand",12)).place(x=280,y=0)
    mostrar_resultado=Listbox(frame_resultados)
    
    def obtener_resultados():
      mostrar_error.delete ( 0, 'end' )
      mostrar_resultado.delete ( 0, 'end' )
      variables=[
          [float(c.get()),0],
          [float(x1.get()),1],
          [float(x2.get()),2],
          [float(x3.get()),3],
          [float(x4.get()),4],
          [float(x5.get()),5],
          [float(x6.get()),6]]
      #asigno los putos valores porque la chingadera de metodo deriva las dos putas listas
      variables_derivadas=[
          [float(c.get()),0],
          [float(x1.get()),1],
          [float(x2.get()),2],
          [float(x3.get()),3],
          [float(x4.get()),4],
          [float(x5.get()),5],
          [float(x6.get()),6]]
  
      variables_derivadas=derivada_simple(variables_derivadas)
      print("valores: \n" + str(variables))
      
      print("valores derivados: \n" + str(variables_derivadas))
      
      c_derivada.set(variables_derivadas[0][0])
      x1_derivada.set(variables_derivadas[1][0])
      x2_derivada.set(variables_derivadas[2][0])
      x3_derivada.set(variables_derivadas[3][0])
      x4_derivada.set(variables_derivadas[4][0])
      x5_derivada.set(variables_derivadas[5][0])
    
      xi=float(valor_inicial.get())
      error_obtenido=100
      x=0
      while(error_obtenido>float(str(error.get()))):
        f_prima_xi=0
        f_xi=0
        x+=1
        for i in range(len(variables)):
          f_xi+=variables[i][0]*(xi**variables[i][1])
        for i in range(len(variables_derivadas)):
          f_prima_xi+=variables_derivadas[i][0]*(xi**variables_derivadas[i][1])
        #imprimir las pendejadas
        print('f(x1)= '+str(f_xi))
        print("f'(x1)= "+str(f_prima_xi))
        #despues de la primera puta iteracion los valores estan pendejos checar xi y xi+1
        try:
          xi_mas_1=xi-(f_xi/f_prima_xi)
          #aqui lanza una puta excepción bien imbecil cuando todos los valores son 1
          error_obtenido=abs(((xi_mas_1-xi)/xi_mas_1)*100)
          xi=xi_mas_1
        except:
          messagebox.showinfo("ERROR", "no se pudo resolver la raíz, intente con otra función")
          return 0
        if(x>50):
            messagebox.showinfo("ERROR", "se excedieron las 50 iteraciones")
            return 0
        if(error_obtenido<float(str(error.get()))):
          return 0
        
        print('error: '+str(error_obtenido))
        mostrar_error.insert(x, "X"+str(x)+"= "+str(round(error_obtenido, int(str(decimales.get())))))
        mostrar_resultado.insert(x, "X"+str(x)+"= "+str(round(xi, int(str(decimales.get())))))
        
      
    mostrar_error.place(x=0,y=40)
    mostrar_resultado.place(x=280,y=40)
    
    root.mainloop()

main_screen()