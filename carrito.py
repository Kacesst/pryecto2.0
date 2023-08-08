class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        item = {
            "producto": producto,
            "cantidad": cantidad
        }
        self.items.append(item)

    def obtener_total_carrito(self):
        total = 0
        for item in self.items:
            producto = item["producto"]
            cantidad = item["cantidad"]
            total += producto.precio * cantidad
        return total

    def mostrar_carrito(self):
        print("======= CARRITO DE COMPRAS =======")
        if not self.items:
            print("El carrito está vacío.\n")
        else:
            for idx, item in enumerate(self.items, 1):
                producto = item["producto"]
                cantidad = item["cantidad"]
                subtotal = producto.precio * cantidad
                print(f"{idx}. {producto.nombre} - Cantidad: {cantidad} - Subtotal: ${subtotal}")
            total_carrito = self.obtener_total_carrito()
            print(f"Total a pagar: ${total_carrito}\n")