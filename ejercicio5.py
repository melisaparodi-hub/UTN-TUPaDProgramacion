# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

###### VARIABLES INICIALES ######
vida_gladiador = 100
vida_enemigo = 100
pociones_de_vida = 3
danio_ataque_pesado = 15
danio_del_enemigo = 12
danio_rafaga = 5
turno_gladiador = True

print("------ BIENVENIDO A LA ARENA ------")

###### CONFIGURACION DEL PERSONAJE ######
nombre_gladiador = input("Nombre del Gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Nombre del Gladiador: ")

###### INICIO COMBATE ######
print("\n====== INICIO DEL COMBATE ======")

while vida_gladiador > 0 and vida_enemigo > 0:
###### TURNO GLADIADOR ######
    if turno_gladiador:
        print(f"\n{nombre_gladiador.capitalize()} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_de_vida}")

###### MENU COMBATE ######
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        while not opcion.isdigit() or opcion not in ("1", "2", "3"):
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

###### OPCION 1: ATAQUE PESADO ######
        if opcion == "1":
            if vida_enemigo < 20:
                danio = danio_ataque_pesado * 1.5
            else:
                danio = danio_ataque_pesado

            vida_enemigo -= danio
            print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

###### OPCIÓN 2: RÁFAGA VELOZ ######
        elif opcion == "2":
            suma_danio_rafaga = 0
            print(">> ¡Inicias una ráfaga de golpes!")

            for i in range(1, 4):
                vida_enemigo -= danio_rafaga
                suma_danio_rafaga += danio_rafaga
                print(f"> {i}° Golpe conectado por {danio_rafaga} de daño.")

            print(f"¡Atacaste al enemigo por {suma_danio_rafaga} puntos de daño!")

###### OPCIÓN 3: CURAR ######
        elif opcion == "3":
            if pociones_de_vida > 0:
                vida_gladiador += 30
                pociones_de_vida -= 1
                print("Te curaste 30 puntos de vida.")
            else:
                print("¡No quedan pociones!")

        turno_gladiador = False
###### TURNO DEL ENEMIGO ######
    else:
        print("\n>> Turno del enemigo...")
        vida_gladiador -= danio_del_enemigo
        print(f"¡El enemigo te atacó por {danio_del_enemigo} puntos de daño!")

        print("====== NUEVO TURNO ======")

        turno_gladiador = True


###### FIN DEL JUEGO ######
print("\n====== FIN DEL COMBATE ======")

if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador.capitalize()} ha ganado la batalla.")
else:
    print("¡DERROTA! Has caído en combate.")