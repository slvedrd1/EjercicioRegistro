usuario1 = None
usuario2 = None
usuario3 = None
contraseña1 = None
contraseña2 = None
contraseña3 = None

while True:
    
    print("")
    print("--MENU--")
    print("1) Iniciar sesion.")
    print("2) Registrar usuario.")
    print("3) Salir.")
    print("")

    ##VALIDAMOS QUE SE INGRESE UN NUMERO
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
        
        #validamos que tengamos usuarios registrados, si no hay usuarios
        #tenemos que ir a la opcion 2, pero si hay caemos en el else
        #comprobando con parentesis si una de las condiciones se cumplen para ir al siguiente menu

        if usuario1 == None and usuario2 == None and usuario3 == None:
            print("Es necesario registrar un usuario antes.")
        else:
            print("Iniciar sesion.")
            usuario = input("Ingrese su usuario: ")
            contraseña = int(input("Ingrese su contraseña: "))

            if (usuario == usuario1 and contraseña == contraseña1) or (usuario == usuario2 and contraseña == contraseña2) or (usuario == usuario3 and contraseña == contraseña3):
                print("Inicio de sesion correcto")

                while True:

                    print("")
                    print("1)Realizar llamadas.")
                    print("2)Enviar correo electronico.")
                    print("3)Cerrar sesion.")
                    print("")

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
                        
                        numero = input("Ingrese el numero que desea llamar: ")

                        #len recorre valida que sean 9 caracteres y startswitch valida que empiece en 9
                        
                        if len(numero) == 9 and numero.startswith("9"):
                            print("Realizando llamado..")
                        else:
                            print("Numero incorrecto.")


                    elif opcion2 == 2:
                        
                        correo = input("Ingrese el correo donde desea mandar el email: ")

                        tiene_arroba = False

                        #usamos la variable letra donde se guardara cada caracter mientras el for la recorre
                        #cuando se comprueba que existe el arroba cambia la bandera a true

                        for letra in correo:
                            
                            if letra == "@":
                                tiene_arroba = True
                                
                        if tiene_arroba == True:
                            mensaje = input("Ingrese el mensaje: ") 
                            print("Correo enviado.")       

                        elif tiene_arroba == False:
                            print("Correo invalido")        
                            

                    elif opcion2 == 3:
                        print("Cerrando sesion...")
                        break
                    else:
                        print("Opcion invalida")

            else:
                print("Inicio de sesion incorrecto.")


    elif opcion == 2:
       
       #vemos si hay usuarios registrados comprobando
       #cada una, si no hay usuario pedira registrar 
       #los datos

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
