# Ejercicio 2 — “Acceso al Campus y Menú Seguro”
# Objetivo: Login con intentos + menú de acciones con validación estricta.

usuario_correcto = "alumno"
clave_correcta = "python123"
acceso = False

intentos = 1

while intentos <= 3:
    usuario = input(f"Intento {intentos}/3 - Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido")
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if acceso:
    opcion = ""

    while opcion != "4":
        print("1) Estado   2) Cambiar clave   3) Mensaje   4) Salir")
        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            print("1) Estado   2) Cambiar clave   3) Mensaje   4) Salir")
            opcion = input("Opción: ")
            
        while opcion not in ("1", "2", "3", "4"):
            print("Error: opción fuera de rango.")
            print("1) Estado   2) Cambiar clave   3) Mensaje   4) Salir")
            opcion = input("Opción: ")
        
        if opcion == "1":
            print("Inscripto")
        elif opcion == "2":
            nueva_clave = input("Nueva clave: ")

            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")

            confirmar_clave = input("Confirme su contraseña: ")
            while confirmar_clave != nueva_clave:
                print("Las contraseñas no coinciden. Intente nuevamente: ")
                confirmar_clave = input("Confirme su contraseña: ")

            print("Contraseña cambiada con éxito.")       
        elif opcion == "3":
            print("\"Cada línea de código que escribís te acerca más a quien querés ser.\"")
        else:
            print("Saliendo del sistema... ¡Hasta pronto!")

else:
    print("Cuenta bloqueada.")

