funcion=[[1,0],[4,1],[2,2],[4,3],[6,4]]
#el exponente del primer valor es cero, significa que es una constante


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

print(derivada_simple(funcion))