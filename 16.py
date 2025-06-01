def aconsejar():
    temp = int(input("Ingrese la temperatura: "))
    humedad = int(input("Ingrese el porcentaje de humedad: "))  



    def elegirRopa(temp, humedad):
        if 0 <= temp <= 25 and 90 <= humedad <= 100:
            return "Pantalón largo y camisa"
        elif 0 <= temp <= 10 and 50 <= humedad < 70:
            return "Pantalón de pana y chaqueleco"
        elif 0 <= temp <= 2 and 45 <= humedad < 70:
            return "Pantalón, chaleco y abrigo"
        elif 10 <= temp <= 30 and 86 <= humedad <= 100:
            return "Pantalón corto y camiseta"
        elif 20 <= temp <= 38 and 85 <= humedad <= 100:
            return "Pantalón corto y camiseta"
        else:
            return "Ropa normal"
    recomendacion = elegirRopa(temp, humedad)
    print(recomendacion)
aconsejar()