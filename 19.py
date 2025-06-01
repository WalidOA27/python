def calculadora():
    numero1 = float(input("Ingresa el primer número: "))
    operador = input("Menú de operaciones:\n1.- Sumar\n2.- Restar\n3. Multiplicar\n4.- Dividir\nElije una opcion:")
    numero2 = float(input("Ingresa el segundo número: "))
    def operadorSeleccionado(operador):
        if operador == '1':
            return '+'
        elif operador == '2':
            return '-'
        elif operador == '3':
            return '*'
        elif operador == '4':
            return '/'
        else:
            return ("Operador no válido")
            
    def calcular(numero1, numero2, operador_seleccionado):
        if operador_seleccionado == '+':
            return numero1 + numero2
        elif operador_seleccionado == '-':
            return numero1 - numero2
        elif operador_seleccionado == '*':
            return numero1 * numero2
        elif operador_seleccionado == '/':
            return numero1 / numero2
        else:
            return "Operador no válido"
        
    operador_seleccionado = operadorSeleccionado(operador)
    resultado = calcular(numero1, numero2, operador_seleccionado)
    if operador_seleccionado == "Operador no válido":
        print("Operador no válido")
        return
    print(f"El resultado es {resultado}")
calculadora()