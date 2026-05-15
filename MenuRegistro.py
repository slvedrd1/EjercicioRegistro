usuario1 = None
usuario2 = None
usuario3 = None
contraseña1 = None
contraseña2 = None
contraseña3 = None

while True:
    
    print("--MENU--")
    print("1) Iniciar sesion.")
    print("2) Registrar usuario.")
    print("3) Salir.")

  
    try:
        opcion = int(input("Ingrese una opcion (1-3): "))

        if opcion >= 1 and opcion <= 3:
            print("Accediendo al menu..")
        else:
            print("Error, el numero debe ser de (1 a 3)")
    except ValueError:
        print("Error, se requiere un valor numerico")  
        continue
            
        
    if opcion == 1:

        if usuario1 == None and usuario2 == None and usuario3 == None:
            print("Es necesario registrar un usuario antes.")
        else:
            print("Iniciar sesion.")
            usuario = input("Ingrese su usuario: ")
            contraseña = int(input("Ingrese su contraseña: "))

            if (usuario == usuario1 and contraseña == contraseña1) or (usuario == usuario2 and contraseña == contraseña2) or (usuario == usuario3 and contraseña == contraseña3):
                print("Inicio de sesion correcto")

                while True:
                    print("1)Realizar llamadas.")
                    print("2)Enviar correo electronico.")
                    print("3)Cerrar sesion.")

                    try:
                        opcion2 = int(input("Ingrese una opcion (1-3): "))

                        if opcion2 >= 1 and opcion2 <= 3:
                            print("Accediendo al menu..")
                        else:
                            print("Error, el numero debe ser de (1 a 3)")
                    except ValueError:
                            print("Error, se requiere un valor numerico")  
                            continue
                    
                    if opcion2 == 1:
                        print("Ingrese numero")

                    elif opcion2 == 2:
                        print("Ingrese correo")

                    elif opcion2 == 3:
                        print("Cerrando sesion...")
                        break
                    else:
                        print("Opcion invalida")
                    

                     


            else:
                print("Inicio de sesion incorrecto.")




    elif opcion == 2:
        print("--Registro de usuario--")
        if usuario1 == None:
            usuario1 = input("Ingrese el nombre de usuario a registrar: ")
            contraseña1 = int(input("Ingrese la contraseña: "))
            print("Usuario registrado correctamente.")
       
        elif usuario2 == None:
            usuario2 = input("Ingrese el nombre de usuario a registrar: ")
            contraseña2 = int(input("Ingrese la contraseña: "))
            print("Usuario registrado correctamente.")
       
        elif usuario3 == None:
            usuario3 = input("Ingrese el nombre de usuario a registrar: ")
            contraseña3 = int(input("Ingrese la contraseña: "))
            print("Usuario registrado correctamente.")

        else:
            print("No se pueden registrar mas usuarios.")






    elif opcion == 3:
        print("Saliendo..")
        break
