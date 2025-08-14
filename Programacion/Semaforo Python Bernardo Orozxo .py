def semaforo(): #Crea una fucion llamada semaforo
    hora = input("Ingresa la hora del día ('dia' o 'noche'): ") #Te enseña un prompt para inresar la hora
    trafico = input("Ingresa el nivel de tráfico ('bajo', 'medio' o 'alto'): ")#Te enseña un prompt para inresar el nivel de trafico 
    print(f"\nHora: {hora} | Tráfico: {trafico}")
	
    if hora == "noche":
        print("Luz: Amarilla Intermitente")#Desactiva el semaforo y brilla amarillo intermitente
    elif hora == "dia":
        # Determina la duracion del verde
        if trafico == "bajo":
            duracion_verdes = 10
        elif trafico == "medio":
            duracion_verdes = 20
        elif trafico == "alto":
            duracion_verdes = 40  #Determina la duracion del semaforo de acuerdo al nivel de trafico 
        else:
            print("Nivel de tráfico no válido.")#Si la opción no es valida, te regresa al principio 
            return

        # Muestra la secuencia de luces y la duracion
        print(f"Luz: VERDE ({duracion_verdes} segundos)")
        print("Luz: AMARILLA (3 segundos)")
        print("Luz: ROJA (30 segundos)")
    else:
        print("Hora del día no válida. Usa 'dia' o 'noche'.")#Si la hora no es valida, te lo dirá 


semaforo()#cierra la funcion 
