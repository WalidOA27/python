def aconsejar():
    temp = int(input("Ingrese la temperatura: "))
    humedad = int(input("Ingrese el porcentaje de humedad: "))  



    def elegirRopa(temp, humedad):
        match (temp, humedad):
            case (t, h) if 0 <= t <= 25 and 90 <= h <= 100:
                return "Pantalón largo y camisa"
            case (t, h) if 0 <= t <= 10 and 50 <= h < 70:
                return "Pantalón de pana y chaqueleco"
            case (t, h) if 0 <= t <= 2 and 45 <= h < 70:
                return "Pantalón, chaleco y abrigo"
            case (t, h) if 10 <= t <= 30 and 86 <= h <= 100:
                return "Pantalón corto y camiseta"
            case (t, h) if 20 <= t <= 38 and 85 <= h <= 100:
                return "Pantalón corto y camiseta"
            case _:
                return "Ropa normal"
        return
    recomendacion = elegirRopa(temp, humedad)
    print(recomendacion)
aconsejar()