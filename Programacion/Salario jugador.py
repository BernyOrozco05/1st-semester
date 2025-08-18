players = []
total_salary = 0

for i in range(1, 12):  
    print(f"\nJugador {i}:")
    
    
    name = input("Ingrese el nombre del jugador: ")

   
    while True:
        try:
            age = int(input("Ingrese la edad del jugador (debe ser 18): "))
            if age == 18:
                break
            else:
                print(" Solo se aceptan jugadores de 18 años. Intente nuevamente.")
        except ValueError:
            print(" Entrada inválida. Ingrese un número entero para la edad.")

    
    while True:
        try:
            salary = float(input("Ingrese el salario del jugador: "))
            break
        except ValueError:
            print(" Entrada inválida. Ingrese un número válido para el salario.")

    
    players.append({"nombre": name, "edad": age, "salario": salary})
    total_salary += salary

print("\n Registro completo de jugadores")
print(f" La suma total de los salarios es: {total_salary}")
