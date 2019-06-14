from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

def main_screen():
    root=Tk()
    
    root.title("Metodo de la secante")
    root.resizable(False,False)
   
    frame_ecuacion=Frame(root,height="100", width="548")
    frame_ecuacion.pack()
    frame_ecuacion.config(bd="1", relief="sunken")
    
    #ecuacion 
    Label(frame_ecuacion,text="función", font=("quicksand",13)).place(x=0,y=0)
    
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
    
   
    
    #intervalo
    
    frame_datos_argumento=Frame(root,height="60", width="548")
    frame_datos_argumento.pack()
      
    Label(frame_datos_argumento,text="Intervalo",font=("quicksand",12)).place(x=0,y=0)
    Label(frame_datos_argumento,text="[",font=("quicksand",12)).place(x=0,y=32)
    #rango a
    rango_a=StringVar()
    Entry(frame_datos_argumento,width="3",font=("quicksand",12),textvariable=rango_a).place(x=20,y=30)
    rango_a.set(-1)
    Label(frame_datos_argumento,text=".",font=("quicksand",12)).place(x=56,y=30)
    #rango b
    rango_b=StringVar()
    Entry(frame_datos_argumento,width="3",font=("quicksand",12),textvariable=rango_b).place(x=70,y=30)
    rango_b.set(1)
    Label(frame_datos_argumento,text="]",font=("quicksand",12)).place(x=110,y=32)
    
    #error y numero de decimales 
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
      
      #intervalo
      variables=[rango_a.get(),rango_b.get()]
      print('rango: '+str(variables[0:]))
      aux_boolean=False
      for x in range(2):
        try:
          float(variables[x])
          print('todo bien, valor:'+ variables[x])
          aux_boolean=True
        except :
          print('error')
          if(x<1):
            messagebox.showinfo("ERROR", "Se ingresó un tipo de dato no valido en el intervalo 'a'")
            return 0
          else:
            messagebox.showinfo("ERROR", "Se ingresó un tipo de dato no valido en el intervalo 'b'")
            return 0
          aux_boolean=False
          break
          return 0
      if(aux_boolean):
        if(variables[0]>=variables[1]):
          messagebox.showinfo("ERROR", "el intervalo 'a' debe ser menor que 'b'")
          return 0
      
      #porcentaje error
      variables=[error.get(),decimales.get()]
      print('porcentaje error y decimales: '+str(variables[0:]))
      for x in range(2):
        try:
          float(variables[x])
        except:
          if(x==0):
            messagebox.showinfo("ERROR", "se ingresó un dato no válido en el porcentaje de error")
          else:
            messagebox.showinfo("ERROR", "se ingresó un dato no válido en la cantidad de decimales")
            
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
      variables=[c.get(),x1.get(),x2.get(),x3.get(),x4.get(),x5.get(),x6.get()]
      #variables=list(filter(lambda s: not '0', variables))
      variables=[float(i) for i in variables]
      
      print("valores" + str(variables[0:]))
      
      i1=float(str(rango_b.get()))
      i_menos_1=float(str(rango_a.get()))
      x=0
      error_obtenido=100
      while(error_obtenido>float(str(error.get()))):
        x+=1
        funcion_i1=0
        funcion_i_menos_1=0
        for j in range(len(variables)):
          if(j<1):
            funcion_i1 += variables[j]
            funcion_i_menos_1 += variables[j]  
          else:
            funcion_i1 += (variables[j])*(i1**j)
            funcion_i_menos_1 += (variables[j])*(i_menos_1**j)
        valor_x1=i1-(funcion_i1*(i_menos_1 - i1)/(funcion_i_menos_1 - funcion_i1))
        print('valor de x'+str(x)+'='+str(valor_x1))
        i_menos_1=i1
        i1=valor_x1
        error_obtenido=abs(((i1 - i_menos_1)/i1)*100)
        if(x>50):
            messagebox.showinfo("ERROR", "se excedieron las 50 iteraciones")
            return 0
        if(error_obtenido<float(str(error.get()))):
          return 0
        
        print('error: '+str(error_obtenido))
        mostrar_error.insert(x, "X"+str(x)+"= "+str(round(error_obtenido, int(str(decimales.get())))))
        mostrar_resultado.insert(x, "X"+str(x)+"= "+str(round(valor_x1, int(str(decimales.get())))))
        print('['+str(i_menos_1)+','+str(i1)+']')
        
      print('f(xi-1)= '+str(funcion_i_menos_1))  
      print('f(xi1)= '+str(funcion_i1))
      
      
    mostrar_error.place(x=0,y=40)
    mostrar_resultado.place(x=280,y=40)
    
    root.mainloop()

main_screen()