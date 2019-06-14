from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

def main_screen():
    root=Tk()
    
    root.title("Metodo de la regla falsa")
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
        if(float(str(variables[0]))>=float(str(variables[1]))):
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
      return variables[0],variables[1]
            
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
      mostrar_resultado.delete ( 0, 'end')
      rango_a=float(str(validaciones()[0]))
      rango_b=float(str(validaciones()[1]))
      #tengo que arreglar el puto rango en los decimales 
      print(rango_a)
      print(rango_b)
    
      rango_a_menos_1=0    
      x=0
      error_obtenido=1000000
      variables=[c.get(),x1.get(),x2.get(),x3.get(),x4.get(),x5.get(),x6.get()]
      
      variables=[float(i) for i in variables]
      while(error_obtenido>float(str(error.get()))):
        f_x0=0
        f_x1=0
        for j in range(len(variables)):
          if(j<1):
            f_x0 += variables[j]
            f_x1 += variables[j]  
          else:
            f_x0 += (variables[j])*(rango_a**j)
            f_x1 += (variables[j])*(rango_b**j)
        print("valores" + str(variables[0:]))
      
        print('f(x0): '+str(f_x0))
        print('f(x1): '+str(f_x1))
            
        
        if(x==0):
          rango_a=((f_x0*rango_b)-(f_x1*rango_a))/(f_x0-f_x1)
        else:
          rango_a_menos_1=rango_a
          rango_a=rango_b-((f_x1*rango_a)-(f_x1*rango_b))/(f_x0-f_x1)
          error_obtenido=abs(((rango_a-rango_a_menos_1)/rango_a)*100)
          
        if(x>50):
          messagebox.showinfo("ERROR", "se excedieron las 50 iteraciones")
          return 0
        if(error_obtenido<float(str(error.get()))):
          return 0
        mostrar_error.insert(x, "X"+str(x)+"= "+str(round(error_obtenido, int(str(decimales.get())))))
        mostrar_resultado.insert(x, "X"+str(x)+"= "+str(round(rango_a, int(str(decimales.get())))))
        x+=1
        
    mostrar_error.place(x=0,y=40)
    mostrar_resultado.place(x=280,y=40)
    
    root.mainloop()

main_screen()