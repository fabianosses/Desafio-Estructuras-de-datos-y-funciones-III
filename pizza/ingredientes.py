# menú ingredientes, mostrado por medio de un bucle for
def menu_ingrediente():
    ingre_elegido = []
    ingredientes = {
    1: "Tomate",
    2: "Champiñones",
    3: "Aceitunas",
    4: "Cebolla",
    5: "Pollo",
    6: "Jamón",
    7: "Carne",
    8: "Tocino",
    9: "Queso"
    }
    print("Elige máximo 3 ingredientes")
    for key, value in ingredientes.items():
        print(f"{key}: {value}")

# bucle elección de ingredientes
    while True:
      valor = int(input("Ingrediente: "))
      ingrediente = ingredientes.get(valor)
      print(f"""Elegiste: {ingrediente}
            """)
      ingre_elegido.append(ingrediente)
      if len(ingre_elegido) == 3:
        break
      elif len(ingre_elegido) < 3:
        agrega = input("¿Desea agregar otro ingrediente? (s/n): ")
        if agrega == "n":
          break
        else:
          agrega == "s"
          print("Elige ")
          continue
    return ingre_elegido