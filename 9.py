def comprobarCalificacion():
    calificacion = int(input("Ingrese la calificación (0-10): "))
    def calcular(calificacion):
        if 0<= calificacion <= 5:
            return "Suspenso"
        elif 5 < calificacion <= 7:
            return "Notable"
        elif 7 < calificacion <= 9:
            return "Aprobado"      
        elif calificacion == 10:
            return "Matricula de Honor"   
        else:
            return "Calificación inválida"
    resultado = calcular(calificacion)
    print(f"La calificación es: {resultado}")
comprobarCalificacion()