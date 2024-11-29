class Producto:
    def __init__(self, codigo, descripcion, precio, cantidad):
        # Atributos privados
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__precio = precio
        self.__cantidad = cantidad

    # Métodos getter y setter para cada atributo
    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    # Método privado: calcular importe de compra (precio * cantidad)
    def __importe_compra(self):
        return self.__precio * self.__cantidad

    # Método privado: calcular IGV (18% del importe de compra)
    def __igv(self):
        return self.__importe_compra() * 0.18

    # Método público: calcular importe total a pagar
    def importe_a_pagar(self):
        return self.__importe_compra() + self.__igv()

    # Método público: imprimir los datos del producto
    def imprimir(self):
        print("===================================")
        print("Datos del Producto:")
        print(f"Código         : {self.__codigo}")
        print(f"Descripción    : {self.__descripcion}")
        print(f"Precio Unitario: {self.__precio}")
        print(f"Cantidad       : {self.__cantidad}")
        print(f"Importe        : {self.__importe_compra()}")
        print(f"IGV (18%)      : {self.__igv()}")
        print(f"Total a Pagar  : {self.importe_a_pagar()}")
        print("===================================")


# Subclases vacías que heredan de Producto
class Cocina(Producto):
    pass


class Lavadora(Producto):
    pass


class Refrigeradora(Producto):
    pass


class Horno_Microonda(Producto):
    pass
