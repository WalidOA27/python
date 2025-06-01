def calculadora():
    altura = float(input("Introduce altura: "))
    base = float(input("Introduce base: "))
    
    def calcular(altura, base):
        return (altura * base) / 2

    
    resultado = calcular(altura, base)
    
    print(f"El area es {resultado}")
calculadora()