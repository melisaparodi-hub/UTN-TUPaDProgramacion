# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

lunes = "1"
martes = "2"
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1= ""
martes2= ""
martes3= ""

operador = input("Ingrese su nombre: ")
while not operador.isalpha() or operador == "":
    operador = input("Valor inválido. Ingrese su nombre: ")

opcion = ""

while opcion != "5":
    print("1. Reservar turno \n2. Cancelar turno (por nombre)\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema")
    opcion = input("Opción: ")
    while not opcion.isdigit() or not (opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5"):
        print("Opción inválida.")
        opcion = input("Opción: ")

    if opcion == "1":
        print("1. Reservar turno:")
        dia = input("Elija el día del turno, 1=Lunes, 2=Martes: ")
        while dia != lunes and dia != martes:
            print("Opción incorrecta.")
            dia = input("Elija el día del turno, 1=Lunes, 2=Martes: ")

        nombre_paciente = input("Nombre del paciente: ")
        while not nombre_paciente.isalpha():
            nombre_paciente = input("Valor inválido. Nombre del paciente: ")

        if dia == lunes:
            if lunes1 == nombre_paciente or lunes2 == nombre_paciente or lunes3 == nombre_paciente or lunes4 == nombre_paciente:
                print("El paciente ya tiene un turno asignado el día Lunes.")
            else:
                if lunes1 == "":
                    lunes1 = nombre_paciente
                elif lunes2 == "":
                    lunes2 = nombre_paciente
                elif lunes3 == "":
                    lunes3 = nombre_paciente
                elif lunes4 == "":
                    lunes4 = nombre_paciente
                else:
                    print("No hay turnos disponibles el día Lunes.")
        elif dia == martes:
            if martes1 == nombre_paciente or martes2 == nombre_paciente or martes3 == nombre_paciente:
                print("El paciente ya tiene un turno asignado el día Martes.")
            else:
                if martes1 == "":
                    martes1 = nombre_paciente
                elif martes2 == "":
                    martes2 = nombre_paciente
                elif martes3 == "":
                    martes3 = nombre_paciente
                else:
                    print("No hay turnos disponibles el día Martes.")

    elif opcion == "2":
        print("2. Cancelar turno:")
        dia = input("Elija el día del turno, 1=Lunes, 2=Martes: ")
        while dia != lunes and dia != martes:
            print("Opción incorrecta.")
            dia = input("Elija el día del turno, 1=Lunes, 2=Martes: ")

        nombre_paciente = input("Nombre del paciente: ")
        while not nombre_paciente.isalpha():
            nombre_paciente = input("Valor inválido. Nombre del paciente: ")

        turno_cancelado = False

        if dia == lunes:
            if lunes1 == nombre_paciente:
                lunes1 = ""
                turno_cancelado = True
            elif lunes2 == nombre_paciente:
                lunes2 = ""
                turno_cancelado = True
            elif lunes3 == nombre_paciente:
                lunes3 = ""
                turno_cancelado = True
            elif lunes4 == nombre_paciente:
                lunes4 = ""
                turno_cancelado = True
        elif dia == martes:
            if martes1 == nombre_paciente:
                martes1 = ""
                turno_cancelado = True
            elif martes2 == nombre_paciente:
                martes2 = ""
                turno_cancelado = True
            elif martes3 == nombre_paciente:
                martes3 = ""
                turno_cancelado = True

        if turno_cancelado:
            print("Turno cancelado con éxito.")
        else:
            print("No se encontró un turno con ese nombre.")

    elif opcion == "3":  
        print("3. Agenda del día:")
        dia = input("Elija el día del turno para visualizar, 1=Lunes, 2=Martes: ")
        while dia != lunes and dia != martes:
            print("Opción incorrecta.")
            dia = input("Elija el día del turno para visualizar, 1=Lunes, 2=Martes: ")

        if dia == lunes:
            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)
            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)
            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)
            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)
        elif dia == martes:
            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)
            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)
            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)

    elif opcion == "4":
        print("4. Ver resumen general:")

        turnos_libres_lunes = 0
        turnos_ocupados_lunes = 0
        turnos_libres_martes = 0
        turnos_ocupados_martes = 0

        if lunes1 == "":
            turnos_libres_lunes += 1
        else:
            turnos_ocupados_lunes += 1
        if lunes2 == "":
            turnos_libres_lunes += 1
        else:
            turnos_ocupados_lunes += 1
        if lunes3 == "":
            turnos_libres_lunes += 1
        else:
            turnos_ocupados_lunes += 1
        if lunes4 == "":
            turnos_libres_lunes += 1
        else:
            turnos_ocupados_lunes += 1

        if martes1 == "":
            turnos_libres_martes += 1
        else:
            turnos_ocupados_martes += 1
        if martes2 == "":  
            turnos_libres_martes += 1
        else:
            turnos_ocupados_martes += 1
        if martes3 == "":
            turnos_libres_martes += 1
        else:
            turnos_ocupados_martes += 1
        print("--- Lunes ---")
        print(f"Turnos ocupados el día Lunes: {turnos_ocupados_lunes}")
        print(f"Turnos disponibles el día Lunes: {turnos_libres_lunes}")
        print("--- Martes ---")
        print(f"Turnos ocupados el día Martes: {turnos_ocupados_martes}")
        print(f"Turnos disponibles el día Martes: {turnos_libres_martes}")

        if turnos_ocupados_lunes > turnos_ocupados_martes:
            print("El día Lunes tiene más turnos.")
        elif turnos_ocupados_martes > turnos_ocupados_lunes:
            print("El día Martes tiene más turnos.")
        else:
            print("Ambos días tienen la misma cantidad de turnos.")
    
    elif opcion == "5":
        print("Saliendo del sistema. ¡Hasta pronto!") 