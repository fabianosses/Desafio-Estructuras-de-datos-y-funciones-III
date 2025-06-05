# importación de funciones de otros archivos desde carpeta pizza
from pizza.ingredientes import menu_ingrediente
from pizza.salsa import menu_salsa
from pizza.masa import menu_masa

# archivo principal
def main():
  masa = menu_masa()
  salsa = menu_salsa()
  ingredientes = menu_ingrediente()

  pizza = {
      "masa elegida": "masa",
      "salsa elegida": "salsa",
      "ingredientes elegidos": "ingrediente"
      }

  pizza["masa elegida"] = masa
  pizza["salsa elegida"] = salsa
  pizza["ingredientes elegidos"] = ingredientes
  return pizza

pizza = (main())

# determinación de tiempo de preparación
print("tiempo estimado: ")
c = len(pizza["ingredientes elegidos"])
print(f"{c*2+20} min")

#Bucle para confirmar, modificar o eliminar pedido
while True:
  print(f"""Pizza por confirmar:
          {pizza}""")
  print("¿Que desea hacer con el pedido?")
  alternativas = [1, 2, 3]
  confirma = int(input("""
              1: confirmar
              2: modificar
              3: cancelar pedido
              """))
  if confirma not in alternativas:
      print("Opción no válida")
      continue
# elimina pedido de pizza
  if confirma == 1:
      print(f"""Pizza confirmada:
            {pizza}""")
      break
  
# alternativa para modificar
  elif confirma == 2:
      modifica = int(input("""¿Que desea modificar?:
            1: masa
            2: salsa
            3: ingredientes
            """))
# modifica masa
      if modifica == 1:
          pizza["masa elegida"] = menu_masa()
# modifica salsa
      elif modifica == 2:
          pizza["salsa elegida"] = menu_salsa()
# modifica ingredientes
      elif modifica == 3:
          pizza["ingredientes elegidos"] = menu_ingrediente()
# cancela pedido
  elif confirma == 3:
      print("Pizza eliminada")
      break