def compararIguales():
    texto1 = input("Ingrese el primer texto: ")
    texto2 = input("Ingrese el segundo texto: ")
    texto3 = input("Ingrese el tercer texto: ")
    def comparar(texto1, texto2, texto3):
        if texto1 == texto2 and texto1 == texto3:
            return "Los textos son iguales"
        elif texto1 != texto2 and texto1 != texto3 and texto2 != texto3:
            return "Los textos son diferentes"
        elif texto1 == texto2 or texto1 == texto3 or texto2 == texto3:
            return "Algunos textos son iguales"
        else:
            return "Error al comparar los textos"
    resultado = comparar(texto1, texto2, texto3)
    print(resultado)    
compararIguales()