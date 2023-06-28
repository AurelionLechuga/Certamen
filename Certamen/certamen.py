import os
os.system("cls")

opc=0


listaCodigo=[]
#6 digitos
listaNombre=[]
#2-50 caracteres
listaCategoria=[]
#Valida
listaPrecio=[]
#Mayor a 0
listacstock=[]
#n Entero positivo
listacantstock=[]
nomusuario=0
productos=(listaCodigo,listaNombre,listaCategoria,listaPrecio,listacstock)
print("Ingresa tu nombre")
input(nomusuario)


print("-----Bienvenido-----")
print("¿Que accion desea realizar?\n 1.Registrar un producto\n 2.Buscar un producto\n 3.Listar productos disponibles\n 4.Salir")

int(input(opc))
while True:
    if opc==1 and opc<5:
      try:
         print("Ingresar un nuevo producto")
         listaCodigo.append=[]
         listaNombre.append=[]
         listaCategoria.append=[]
         listaPrecio.append=[]
         listacstock.append=[]
         break
      except:   
        print("Error al ingresar opcion")

    elif opc==2 and opc<5:
        try:
           print("Buscar un producto")
           print(listaCodigo,listaNombre,listaCategoria)
           break
        except:
           print("Ha ocurrido una excepcion, la opcion ingresada no es valida")
    elif opc==3 and opc<5:
       try:
          print(listaNombre,listacstock)
          listacstock<5
          listacantstock+1
          break
       except:
          print("La cantidad ingresada no es valida")
    else:
        opc==4
        print("Adios:")
        print(nomusuario)
        print("Version 1.0")
        break
        
input("\n Enter para terminar")


#--------OPC1: Registrar producto--------#
#--------OPC2: Buscar producto--------#
#El producto se busca con el codigo y muestra todos los productos de esa categoria
#--------OPC3: Listar productos--------#
# #Mostrar todos los productos disponibles, agregar productos con stock "MENOR a 5" como STOCK BAJO
#--------OPC4: Salir--------#
#Mostrar MSG de despedida con: Nombre y apellido del usuario y Version del programa