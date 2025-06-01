def mediaPositivos():
    numeros = input("Ingrese números separados por comas: ")
    numerosSeparados = [int(n) for n in numeros.split(",")]
    
    def numerosPositivos(numerosSeparados):
        return [n for n in numerosSeparados if n > 0]
        
    def calcularMedia(lista):
        if len(lista) == 0:
            return 0
        return sum(lista) / len(lista)

    positivos = numerosPositivos(numerosSeparados)
    resultado = calcularMedia(positivos)
    print("Media de los números positivos:", resultado)
    print(numerosSeparados)
mediaPositivos()


