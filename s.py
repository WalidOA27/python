def calculadora():
    radio = float(input("Dime el radio"))
    def eleccion():
        eleccion = input("Superfice (s), Volumen (v) o longitud (l)")
        return eleccion
    
    def calcular(radio, eleccion,):
        if eleccion == "s":
            return 2 * 3.14 * radio**2
        elif eleccion == "l":
            return 2 * 3.14 * radio
        elif eleccion == "v":
            return 4 * 3.14 * (radio**3)/3
        else:
            return("vete")
    resultado = calcular(radio, eleccion(),)
    print(resultado)
calculadora()
        
                
