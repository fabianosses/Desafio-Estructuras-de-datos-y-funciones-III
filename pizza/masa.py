def menu_masa():
    masas = {
    1: "Masa Tradicional",
    2: "Masa Delgada",
    3: "Masa con Bordes de Queso"
    }
    for key, value in masas.items():
        print(f"{key}: {value}")
    valor = int(input("Elige tipo de masa: "))
    masa = masas.get(valor)
    print(f"""elegiste: {masa}
          """)
    return masa