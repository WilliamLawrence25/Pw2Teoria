class ProductoStock:
    def __init__(self, nombre, valor, cantidad):
        self.nombre = nombre
        self.valor = valor
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Valor: {self.valor}, Cantidad en stock: {self.cantidad}"

class StockProductos:
    def __init__(self):
        self.productos = {}

    def adicionaProducto(self, producto):
        self.productos[producto.nombre] = producto
        print(f"Producto {producto.nombre} añadido al stock.")

    def getProducto(self, nombre):
        return self.productos.get(nombre, None)

class CarritoCompra:
    def __init__(self, stock):
        self.stock = stock
        self.items = []

    def adicionaItem(self, nombre, cantidad):
        producto = self.stock.getProducto(nombre)
        if producto and producto.cantidad >= cantidad:
            self.items.append((producto, cantidad))
            print(f"Item {nombre} añadido al carrito.")
        else:
            print(f"Stock insuficiente para {nombre} o producto no encontrado.")

    def finalizarCompra(self):
        for producto, cantidad in self.items:
            producto.cantidad -= cantidad
            print(f"Compra finalizada. Stock de {producto.nombre} actualizado a {producto.cantidad}.")

    def calculaTotal(self):
        total = sum(producto.valor * cantidad for producto, cantidad in self.items)
        return total

class Principal:
    def main():
        
        stock = StockProductos()
        stock.adicionaProducto(ProductoStock("monitor", 500, 100))
        stock.adicionaProducto(ProductoStock("teléfono", 150, 300))
        stock.adicionaProducto(ProductoStock("teclado", 70, 50))
        stock.adicionaProducto(ProductoStock("mouse", 50, 50))

        carrito = CarritoCompra(stock)
        carrito.adicionaItem("monitor", 59)
        carrito.adicionaItem("teléfono", 99)
        carrito.adicionaItem("teclado", 38)

        carrito.finalizarCompra()
        
        total = carrito.calculaTotal()
        print(f"La suma de los productos: {total}")

if __name__ == "__main__":
    Principal.main()
