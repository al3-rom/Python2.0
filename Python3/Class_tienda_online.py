"""
TIENDA ONLINE
Crea una clase "Producto" con atributos como nombre, precio y cantidad en
stock. Luego, crea una clase "Tienda" que contenga una lista de productos
disponibles y métodos para agregar productos, mostrar el inventario y
realizar una compra.

"""

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f'Producto {producto.nombre} agregado al inventario.')

    def mostrar_inventario(self):
        print("Inventario de la tienda:")
        for producto in self.productos:
            print(f'Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}')

    def realizar_compra(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    total_precio = producto.precio * cantidad
                    print(f'Compra exitosa. Total a pagar: {total_precio}')
                else:
                    print('No hay suficiente cantidad en stock para realizar esta compra.')
                return
        print('El producto solicitado no está disponible en la tienda.')


# Ejemplo de uso
if __name__ == "__main__":
    producto1 = Producto("Camiseta", 20, 50)
    producto2 = Producto("Pantalón", 30, 30)

    tienda = Tienda()
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)

    tienda.mostrar_inventario()

    tienda.realizar_compra("Camiseta", 3)
    tienda.realizar_compra("Pantalón", 40)

    tienda.mostrar_inventario()
        