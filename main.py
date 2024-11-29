from producto import Cocina, Lavadora, Refrigeradora, Horno_Microonda

def main():
    # Crear objetos de cada clase y asignar valores mediante el constructor
    cocina = Cocina(100, "Cocina a Gas", 1200.0, 2)
    lavadora = Lavadora(200, "Lavadora Automática", 1500.0, 1)
    refrigeradora = Refrigeradora(300, "Refrigeradora No Frost", 1800.0, 1)
    horno_microondas = Horno_Microonda(400, "Horno Microondas Digital", 800.0, 3)

    # Imprimir los datos de cada producto
    cocina.imprimir()
    lavadora.imprimir()
    refrigeradora.imprimir()
    horno_microondas.imprimir()


if __name__ == "__main__":
    main()
