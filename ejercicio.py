while True:
    try:
        print("(1)")
        print("(2)")
        print("(3)")
        print("(4)")
        opcion=int(input ("Ingrese opcion: "))
        if opcion==1:
            print("HOLA")
        else:
            if opcion==2:
                print("CHAO")
            else:
                if opcion==3:
                    print("Jorge chupalo")
                else:
                    if opcion==4:
                        break

    except ValueError:
        print("ingrese solo numeros")