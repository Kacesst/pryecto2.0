import json
from producto import cargar_productos_desde_json

class Tienda:
    def __init__(self):
        self.clientes = self.cargar_datos_json("clientes.json")
        self.empleados = self.cargar_datos_json("empleados.json")
        self.es_empleado = False
        self.productos = cargar_productos_desde_json("productos.json")

    def cargar_datos_json(self, archivo):
        try:
            with open(archivo, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def guardar_datos_json(self, datos, archivo):
        with open(archivo, "w") as file:
            json.dump(datos, file, indent=4)

    def registrar_cliente(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        email = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")

        cliente = {
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "password": password
        }

        self.clientes.append(cliente)
        self.guardar_datos_json(self.clientes, "clientes.json")
        print("Registro exitoso. Ahora puede iniciar sesión.")
    def iniciar_sesion(self):
        email = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")

        for cliente in self.clientes:
            if cliente["email"] == email:
                if cliente["password"] == password:
                    self.es_empleado = False
                    return cliente
                else:
                    print("Contraseña incorrecta. Intente nuevamente.")
                    return None

        for empleado in self.empleados:
            if empleado["email"] == email:
                if empleado["password"] == password:
                    self.es_empleado = True
                    return empleado
                else:
                    print("Contraseña incorrecta. Intente nuevamente.")
                    return None

        print("Correo electrónico no registrado. Intente nuevamente.")
        return None

    def mostrar_informacion_cliente(self, cliente):
        if self.es_empleado:
            print("Información del cliente:")
            print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
            print(f"Correo: {cliente['email']}")
            print(f"Dirección: {cliente['direccion']}")
            print(f"DNI: {cliente['dni']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Tarjeta de crédito: {cliente['tarjeta_credito']}\n")
        else:
            print("Acceso denegado. Solo los empleados pueden ver información de clientes.\n")
    

        self.clientes.append(cliente)
        self.guardar_datos_json(self.clientes, "clientes.json")
        print("Registro exitoso. Ahora puede iniciar sesión.")
        
    def mostrar_galeria_productos(self):
        print("======= GALERÍA DE PRODUCTOS =======")
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto.nombre} - ${producto.precio}")
        print("=====================================")


    def actualizar_stock_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.actualizar_stock(cantidad)
                self.guardar_datos_json([prod.__dict__ for prod in self.productos], "productos.json")
                print(f"Se ha actualizado el stock de {producto.nombre}. Nuevo stock: {producto.stock}")
                break
        else:
            print(f"No se encontró un producto con el nombre '{nombre_producto}'.")
    def buscar_cliente_por_email(self, email):
        for cliente in self.clientes:
            if cliente['email'] == email:
                return cliente
        return None