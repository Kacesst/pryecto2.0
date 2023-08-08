import json
from tienda import Tienda
from producto import Zapatilla, Camiseta

# Constantes
costo_envio = 10  # Costo fijo de envío en dólares
porcentaje_venta = 5  # Porcentaje adicional por venta en porcentaje


try:
    with open("clientes.json", "r") as archivo_clientes:
        clientes_data = json.load(archivo_clientes)
except FileNotFoundError:
    clientes_data = {}

try:
    with open("empleados.json", "r") as archivo_empleados:
        empleados_data = json.load(archivo_empleados)
except FileNotFoundError:
    empleados_data = {}
    


# Guardar empleados_data en el archivo empleados.json
with open("empleados.json", "w") as archivo_empleados:
    json.dump(empleados_data, archivo_empleados)
    

# Guardar cliente_data en el archivo clientes.json
with open("clientes.json", "w") as archivo_clientes:
    json.dump(clientes_data, archivo_clientes)


def menu_inicio(tienda):
    while True:
        print("======= MENÚ DE INICIO =======")
        print("1. Ingresar a su cuenta")
        print("2. Registrarse como nuevo cliente")
        print("3. Salir")

        opcion = input("Ingrese el número de opción que desee: ")

        if opcion == "1":
            usuario = tienda.iniciar_sesion()
            if usuario:
                print("Inicio de sesión exitoso.")
                return usuario
            else:
                print("Correo o contraseña incorrectos. Intente nuevamente.\n")
        elif opcion == "2":
            tienda.registrar_cliente()
        elif opcion == "3":
            print("Gracias por visitar nuestra tienda. ¡Hasta pronto!")
            exit()
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.\n")


def menu_compra(tienda, cliente):
    while True:
        print("======= MENÚ DE COMPRA =======")
        print("1. Ver carrito")
        print("2. Ver galería de productos")
        print("3. Salir")

        opcion = input("Ingrese el número de opción que desee: ")

        if opcion == "1":
            mostrar_carrito_cliente(cliente)
        elif opcion == "2":
            mostrar_galeria_productos(tienda.productos)
        elif opcion == "3":
            print("Gracias por utilizar nuestro servicio de compra. ¡Hasta pronto!")
            exit()
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.\n")



def menu_carrito(tienda, cliente):
    while True:
        print("======= MENÚ DEL CARRITO =======")
        print("1. Agregar producto al carrito")
        print("2. Quitar producto del carrito")
        print("3. Finalizar compra")
        print("4. Volver al menú de compra")
        
        opcion = input("Ingrese el número de opción que desee: ")
        
        if opcion == "1":
            mostrar_galeria_productos(tienda.productos)
            seleccion = int(input("Ingrese el número de producto que desea agregar al carrito: "))
            if seleccion > 0 and seleccion <= len(tienda.productos):
                cliente.agregar_producto_carrito(tienda.productos[seleccion - 1])
                print("Producto agregado al carrito.")
            else:
                print("Opción inválida. Ingrese un número de producto válido.")
        elif opcion == "2":
            mostrar_carrito_cliente(cliente)
            seleccion = int(input("Ingrese el número de producto que desea quitar del carrito: "))
            if seleccion > 0 and seleccion <= len(cliente.carrito):
                cliente.quitar_producto_carrito(seleccion - 1)
                print("Producto quitado del carrito.")
            else:
                print("Opción inválida. Ingrese un número de producto válido.")
        elif opcion == "3":
            realizar_compra(cliente)
            return
        elif opcion == "4":
            return
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.\n")

def mostrar_carrito_cliente(cliente):
    print(f"Carrito de {cliente.nombre} {cliente.apellido}:")
    for item in cliente.carrito:
        producto = item.producto
        cantidad = item.cantidad
        print(f"{producto.nombre} - Cantidad: {cantidad}")
    total_carrito = cliente.obtener_total_carrito()
    print(f"Total a pagar: ${total_carrito}\n")

def mostrar_galeria_productos(productos):
    print("======= GALERÍA DE PRODUCTOS =======")
    for idx, producto in enumerate(productos, 1):
        if isinstance(producto, Zapatilla):
            print(f"{idx}. {producto.nombre} - {producto.marca} - ${producto.precio}")
        elif isinstance(producto, Camiseta):
            print(f"{idx}. {producto.nombre} - {producto.marca} - ${producto.precio}")
    print()





def realizar_compra(cliente):
    print("======= MENÚ DE COMPRA =======")
    print("Ingrese los siguientes datos para completar la compra:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    dni = input("DNI: ")
    direccion = input("Dirección: ")
    tarjeta_credito = input("Tarjeta de crédito: ")
    
    # Calcular costo total de la compra
    costo_total = cliente['obtener_total_carrito']()+ costo_envio + (costo_envio * porcentaje_venta / 100)
    
    print(f"El costo total de la compra es: ${costo_total}")
    print("Compra realizada con éxito. ¡Gracias por su compra!")





def main():
    tienda = Tienda()
    usuario = menu_inicio(tienda)
    menu_compra(tienda, usuario)
    
   


if __name__ == "__main__":
    main()