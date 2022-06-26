from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products

no_login = 1

while no_login:
  usuario = input("Ingresa el usuario ")
  contra = input("Ingresa la contraseña ")

  if usuario == 'emtech' and contra == 'caso1':
    no_login = 0
  else:
    print("Usuario o contraseña invalidos")


contador = 0
total_ventas_producto = []

for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0] == venta[1]:
      contador += 1

  formato = [producto[0],producto[1],contador]
  total_ventas_producto.append(formato)
  contador = 0

ordenados = sorted(total_ventas_producto, key=lambda total : 
 total[2], reverse=True)

mostrar = 0
print("\n 5 productos mas vendidos: \n")
while mostrar < 5 :
  print("Producto: " + str(ordenados[mostrar][1]) + " cantidad de ventas: " + str(ordenados[mostrar][2]))
  mostrar += 1
  








contador = 0
total_busquedas = []
for producto in lifestore_products:
  for busqueda in lifestore_searches:
      if producto[0] == busqueda[1]:
        contador += 1
        
  formato = [producto[0],producto[1],contador]
  total_busquedas.append(formato)
  contador = 0

ordenados = sorted(total_busquedas, key=lambda total : 
total[2], reverse=True)

mostrar = 0
print("\n 10 productos mas buscados: \n")
while mostrar < 10 :
  print("Producto: " + str(ordenados[mostrar][1]) + " cantidad de busquedas: " + str(ordenados[mostrar][2]))
  mostrar += 1






categorias = []
categoria = ""
for producto in lifestore_products:
  if producto[3] != categoria:
    categoria = producto[3]
    categorias.append(categoria)







    
for categoria_producto in categorias:
  
  contador = 0
  total_ventas_producto = []
  for producto in lifestore_products:
    if producto[3] == categoria_producto:
      for venta in lifestore_sales:
        if producto[0] == venta[1]:
          contador += 1
    
      formato = [producto[0],producto[1],contador]
      total_ventas_producto.append(formato)
      contador = 0
  
  ordenados = sorted(total_ventas_producto, key=lambda total : 
   total[2])
  
  mostrar = 0

  if len(ordenados) >= 5:
    print("\n 5 productos menos vendidos de categoria: " + categoria_producto + " \n")
    while mostrar < 5 :
      print("Producto: " + str(ordenados[mostrar][1]) + " cantidad de ventas: " + str(ordenados[mostrar][2]))
      mostrar += 1
  else:
    print("\n" + str(len(ordenados)) +  " productos menos vendidos de categoria: " + categoria_producto + " \n")
    while mostrar < len(ordenados) :
      print("Producto: " + str(ordenados[mostrar][1]) + " cantidad de ventas: " + str(ordenados[mostrar][2]))
      mostrar += 1

    print("\n No se pueden mostrar los 5 menos vendidos de esa categoria porque existen menos de 5 elementos en esa categoria")







for categoria_producto in categorias:
  contador = 0
  total_busquedas_prod = []
  for producto in lifestore_products:
    if producto[3] == categoria_producto:
      for busqueda in lifestore_searches:
        if producto[0] == busqueda[0]:
          contador += 1
    
      formato = [producto[0],producto[1],contador]
      total_busquedas_prod.append(formato)
      contador = 0
  
  ordenados = sorted(total_busquedas_prod, key=lambda total : 
   total[2])
  
  mostrar = 0

  if len(ordenados) >= 10:
    print("\n 10 productos menos buscados de categoria: " + categoria_producto + " \n")
    while mostrar < 10 :
      print("Producto: " + str(ordenados[mostrar][1]) + " cantidad de busquedas: " + str(ordenados[mostrar][2]))
      mostrar += 1
  else:
    print("\n" + str(len(ordenados)) +  " productos menos vendidos de categoria: " + categoria_producto + " \n")
    while mostrar < len(ordenados) :
      print("Producto: " + str(ordenados[mostrar][1]) + " cantidad de busquedas: " + str(ordenados[mostrar][2]))
      mostrar += 1

    print("\n No se pueden mostrar los 10 menos buscados de esa categoria porque existen menos de 5 elementos en esa categoria")
  
   
    



    