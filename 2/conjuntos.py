def run():
  
  a=set()
  b=set()
  nA = int(input('Ingrese el rango del conjunto A '))
    
  for i in range(nA):
    lista_agg = int(input('agrega el numero para el conjunto A: '))
    a.add(lista_agg)
    
  nB = int(input('Ingrese el rango del conjunto B '))
  for i in range(nB):
    lista_agg = int(input('agrega el numero para el conjunto B: '))
    b.add(lista_agg)
    
  
  def mostrar_menu(opciones):
      print('Seleccione una opción:')
      for clave in sorted(opciones):
          print(f' {clave}) {opciones[clave][0]}')
  
  
  def leer_opcion(opciones):
      while (a := input('Opción: ')) not in opciones:
          print('Opción incorrecta, vuelva a intentarlo.')
      return a
  
  
  def ejecutar_opcion(opcion, opciones):
      opciones[opcion][1]()
  
  
  def generar_menu(opciones, opcion_salida):
      opcion = None
      while opcion != opcion_salida:
          mostrar_menu(opciones)
          opcion = leer_opcion(opciones)
          ejecutar_opcion(opcion, opciones)
          print()
  
  
  def menu_principal():
      opciones = {
          '1': ('Union', accion1),
          '2': ('Interseccion', accion2),
          '3': ('Diferencia', accion3),
          '4': ('Diferencia Simetrica', accion4),
          '5': ('Salir', salir)
      }
  
      generar_menu(opciones, '5')
  
  
  def accion1():
      print(a.union(b))
  
  
  def accion2():
      deff = [value for value in a if value in b]
      print(deff)
  
  
  def accion3():
      print(a-b)
      print(b-a)
  
  def accion4():
      print(a^b)
  
  
  def salir():
      print('Saliendo')

  
  menu_principal()

if __name__ == '__main__':
    run()


