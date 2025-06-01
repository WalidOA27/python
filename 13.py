def determinarIgualdad():
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    def comparar(numero1, numero2):
        if numero1 == numero2:
            return "Los números son iguales"
        else:
            return "Los números son diferentes" 
    resultado = comparar(numero1, numero2)
    print(resultado)
determinarIgualdad()
                  
                  

