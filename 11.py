def determinarMayorMenor():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: ")) 
    def comparar(numero1, numero2):
        if numero1 > numero2:
            return f"{numero1} es mayor que {numero2}"
        elif numero1 < numero2:
            return f"{numero1} es menor que {numero2}"
        else:
            return "Los números son iguales"
    resultado = comparar(numero1, numero2)    
    print(resultado)
determinarMayorMenor()