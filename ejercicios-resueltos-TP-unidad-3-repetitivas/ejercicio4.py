# Ejercicio 4 — “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma= False
codigo_parcial = ""
cant_opcion1 = 0

print("################### Escape Room: La Bóveda ###################\n")
print("------------------------------------------------------------\n")
print("Sos un agente que intenta abrir una bóveda con 3 cerraduras. \nTenés energía y tiempo limitados. \nSi abrís las 3 cerraduras antes de quedarte sin energía \no sin tiempo, ganás.")
print("------------------------------------------------------------\n")

nombre_agente = input("Escribe tu nombre de agente (solo se permiten letras): ")
while not nombre_agente.isalpha() or nombre_agente == "":
    print("¡Nombre inválido! Intenta nuevamente.")
    nombre_agente = input("Escribe tu nombre de agente (solo se permiten letras): ")

print()
print(f"¡Bienvenido Agente {nombre_agente.capitalize()}! Hora de comenzar el juego.\n")
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    
###### BLOQUEO POR ALARMA ######   
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:  
        print("Sistema bloqueado.")
        break

    print("----------------- ESTADO DEL JUEGO -----------------\n")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print("Alarma:", "Activada" if alarma else "Desactivada")
    print(f"Código parcial: {codigo_parcial}")
    print()

    print("----------------- MENU DE OPCIONES ------------------\n")
    print("(1) Forzar cerradura \n(2) Hackear panel \n(3) Descansar \n")

    opcion_menu = input("Elija su opción ingresando 1, 2, 3: ")
    while not opcion_menu.isdigit() or opcion_menu == "" or opcion_menu not in ("1", "2", "3"):
        print("Error: opción inválida")
        opcion_menu = input("Elija su opción ingresando 1, 2, 3: ")

###### MENU 1 #########
    if opcion_menu == "1":
        energia -= 20
        tiempo -= 2
        cant_opcion1 += 1
    
        if cant_opcion1 == 3:
            alarma = True
            print("¡ALARMA ACTIVADA! La cerradura se trabó.")
        elif energia < 40:
            numero = input("Ingresa un número del 1 al 3: ")
            while not numero.isdigit() or numero == "" or numero not in ("1", "2", "3"):
                print("Error: opción inválida")
                numero = input("Ingresa un número del 1 al 3: ")
            if numero == "3":
                alarma = True
            else:
                cerraduras_abiertas += 1
        else:
            cerraduras_abiertas += 1

######## MENU 2 ##########        
    if opcion_menu == "2":
        energia -= 10
        tiempo -= 3
        cant_opcion1 = 0

        for i in range(1, 5):
            codigo_parcial += "A"
            print(f"{i}. Cargando... \"{codigo_parcial}\"")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Cerradura abierta con éxito.")
        else:
            print("Código incompleto.")
            print(f"Te faltan {8 - len(codigo_parcial)} cifras de 8 para descifrar el código.")

######## MENU 3 ##########  
    if opcion_menu == "3":
        tiempo -= 1
        cant_opcion1 = 0

        if (energia + 15) <= 100:
            energia += 15
        else:
            energia = 100

        if alarma:
            energia -= 10      

#### CONDICIONES DE FIN ####

if cerraduras_abiertas == 3:
    print("¡VICTORIA! Has abierto las tres cerraduras a tiempo.")
elif energia <= 0 or tiempo <= 0:
    print("¡DERROTA! Te quedaste sin energía o tiempo.") 
elif alarma and tiempo <= 3:
    print("¡DERROTA! Has sido bloqueado por la alarma")          







