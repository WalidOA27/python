def calculadora():
    a= float(input("Introduce primer digito: "))
    operador= (input("Introduce operador: "))
    b= float(input("Introduce segundo digito: "))
    
    def calcular(a, b, operador):
            if operador == "+":
                return a + b
            elif operador == "-":
                return a - b
            elif operador == "*":
                return a * b
            elif operador == "/":
                return a / b
            else:
                return("operador invalido")
        
    resultado = calcular(a, b, operador)

    print(resultado)

calculadora()
