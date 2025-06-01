def comprobarCalificacion():
    calificacion = int(input("Ingrese la calificación (0-10): "))
    def calcular(calificacion):
        match calificacion:
            case _ if 0 <= calificacion <= 5:
                return "Suspenso"
            case _ if 5 <= calificacion <= 7:
                return "Aprobado"
            case _ if 8 <= calificacion <= 9:
                return "Notable"
            case 10:
                return "Matricula de Honor"
            case _: 
                return "Calificación inválida"
    resultado = calcular(calificacion)
    print(f"La calificación es: {resultado}")
comprobarCalificacion()
