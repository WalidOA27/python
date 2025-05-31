def calculadora():
    notas = input("Ingresa tus notas separadas con comas: ")

    def separar(notas):
        notasSeparadas = [float(x.strip()) for x in notas.split(",")]
        return notasSeparadas
    def calcular(notasSepardas):
        media = sum(notasSepardas[:5])/5
        return media
    notasSeparadas = separar(notas)
    media = calcular(notasSeparadas)
    resultado = f"Media de {media}"
    print(resultado)
calculadora()        
        
