def menu_salsa():
    salsas = {
    1: "Salsa de Tomate",
    2: "Salsa Alfredo",
    3: "Salsa Barbecue",
    4: "Salsa Pesto"
    }
    for key, value in salsas.items():
        print(f"{key}: {value}")
    valor = int(input("Elige tipo de salsa: "))
    salsa = salsas.get(valor)
    print(f"""elegiste: {salsa}
          """)
    return salsa