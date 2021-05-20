
## FASE 1 #################################################

def restaurante():
    # Creamos las variables de los billetes y arrays
    b1, b2, b3, b4, b5, b6, b7 = 5, 10, 20, 50, 100, 200, 500
    TOT = 0

    menu = []
    precios = []

## FASE 2 #################################################
# (1)

    # Pedimos los datos por pantalla para llenar los arrays
    print("\n Vamos a crear la carta para las tapas!! \n")
    CANT = int(input("Introduce la cantidad de platos que vas a introducir \n"))
    print("\n")

    CONT = 1

    for i in range(CANT):
        PL = input("Dime el nombre de la tapa Nº %s \n" % CONT)
        PR = input("Dime el precio de %s \n" % PL)
        print("\n")

        CONT += 1
        CANT -= 1

        # LLenamos los arrays
        menu.append(PL)
        precios.append(PR)

    # Creamos el diccionario
    CARTA = dict(zip(menu, precios))

# (2)

    # Mostramos el menu
    print("-----LAS TAPAS DEL DIA-----")
    print("---------------------------")

    for key in CARTA:
        print(key, ":", CARTA[key], "€")

    print("---------------------------")

# (3)

    # Realizamos el pedido
    LISTA = []
    OPT = 1

    while OPT == 1:

        print("\n Introduce la tapa que deseas:")
        VAR = input("->")
        print("\n")
        print("¿Quieres seguir pidiendo? (1:SI / 0:NO)")
        OPT = int(input("->"))
        LISTA.append(VAR)

## FASE 3 #################################################

# (1)
    # Comprobacion del pedido
    VAR = True

    for key in LISTA:
        if key not in CARTA:
            print("\n Producto %s no encontrado" % key)
            VAR = False

    # Proceso de pago
    if VAR:
        print("\n*******************************************")
        print("Procesando su pedido :)")
        print("*******************************************")
        print("Tapas pedidas:", LISTA)
        print("*******************************************")

        for key in LISTA:
            TOT = TOT + int(CARTA.get(key))

        print("Total a pagar: %d€" % TOT)
    # (2)

    # Pedido no encontrado
    else:
        print("\n Lo sentimos, el pedido no puede ser procesado, intentelo de nuevo mas tarde")


restaurante()
