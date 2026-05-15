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
            print("Redirigiendo..")
        else:
            print("Error, el numero debe ser de (1 a 3)")
    except ValueError:
        print("Error, se requiere un valor numerico")  
        continue
            
        
    if opcion == 1:

        if usuario1 == None and usuario2 == None and usuario3 == None:
            print("Es necesario registrar un usuario antes.")
        else:
            usuario = input("Ingrese su usuario: ")
            contraseña = int(input("Ingrese su contraseña"))




    elif opcion == 2:
        print("--Registro de usuario--")






    elif opcion == 3:
        print("Saliendo..")
        break
