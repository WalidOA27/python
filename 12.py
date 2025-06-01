def determinarMayorMenor():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: ")) 
    numero3 = int(input("Ingrese el tercer número: "))
    def mayorNumero(numero1, numero2, numero3):
        
        if numero1 > numero2 and numero1 > numero3:
            return f"{numero1} es el mayor"
        elif numero2 > numero1 and numero2 > numero3:
            return f"{numero2} es el mayor"
        elif numero3 > numero1 and numero3 > numero2:
            return f"{numero3} es el mayor"    
        else:
            return "Los números son iguales"
    def menorNumero(numero1, numero2, numero3):
        if numero1 < numero2 and numero1 < numero3:
            return f"{numero1} es el menor"
        elif numero2 < numero1 and numero2 < numero3:
            return f"{numero2} es el menor"
        elif numero3 < numero1 and numero3 < numero2:
            return f"{numero3} es el menor"    
        else:
            return "Los números son iguales"
    Resultado1 = mayorNumero(numero1, numero2, numero3)    
    resultado2 = menorNumero(numero1, numero2, numero3)
    print(Resultado1)
    print(resultado2)
determinarMayorMenor()