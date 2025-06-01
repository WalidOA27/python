def clasificar():
    numero = int(input("Ingrese un número: "))
    def parOImpar(numero):
        if numero % 2 == 0:
            return "par"
        else:
            return "impar"
    resultado = parOImpar(numero)
    print(f"El número {numero} es {resultado}.")
clasificar()