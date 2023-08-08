import json
class Producto:
    def __init__(self, nombre, tipo, marca, modelo, color, precio, stock):
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, talla, cantidad):
        if talla in self.stock:
            self.stock[talla] += cantidad
        else:
            print(f"Talla {talla} no disponible para este producto.")

def cargar_productos_desde_json(archivo):
    try:
        with open(archivo, "r") as file:
            data = json.load(file)
            productos = []

            for item in data:
                nombre = item["nombre"]
                tipo = item["tipo"]
                marca = item["marca"]
                modelo = item["modelo"]
                color = item["color"]
                precio = item["precio"]
                stock = item["stock"]
                tallas_stock = item["tallas_stock"]
                descripcion = item["descripcion"]

                # Verificar si la clave "diseño" está presente en la entrada
                if "diseño" in item:
                    diseño = item["diseño"]
                    producto = Camiseta(nombre, tipo, marca, modelo, color, precio, stock, diseño, tallas_stock, descripcion)
                else:
                    producto = Zapatilla(nombre, tipo, marca, modelo, color, precio, stock, descripcion, tallas_stock)

                productos.append(producto)

            return productos
    except FileNotFoundError:
        return []

    


class Zapatilla(Producto):
    def __init__(self, nombre, tipo, marca, modelo, color, precio, stock, descripcion, tallas_stock):
        super().__init__(nombre, tipo, marca, modelo, color, precio, stock)
        self.descripcion = descripcion
        self.tallas_stock = tallas_stock

class Camiseta(Producto):
    def __init__(self, nombre, tipo, marca, modelo, color, precio, stock, diseño, tallas_stock, descripcion):
        super().__init__(nombre, tipo, marca, modelo, color, precio, stock)
        self.diseño = diseño
        self.tallas_stock = tallas_stock
        self.descripcion = descripcion

# Otras clases para diferentes tipos de productos (Tapado, Abrigo, etc.)

    def __str__(self):
        return f"{self.nombre} - {self.marca} {self.modelo} - Color: {self.color} - Precio: ${self.precio} - Stock: {self.stock}"


