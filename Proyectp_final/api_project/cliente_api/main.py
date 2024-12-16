from api_client import APIClient

def main():
    client = APIClient(base_url="http://127.0.0.1:8000")

    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1. Iniciar sesión")
        print("2. Listar productos")
        print("3. Crear producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            username = input("Usuario: ")
            password = input("Contraseña: ")
            print(client.login(username, password))
        elif choice == "2":
            products = client.list_products()
            for p in products:
                print(p)
        elif choice == "3":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            descripcion = input("Descripción: ")
            print(client.create_product(nombre, precio, stock, descripcion))
        elif choice == "4":
            product_id = int(input("ID del producto: "))
            nombre = input("Nuevo nombre: ")
            print(client.update_product(product_id, {"nombre": nombre}))
        elif choice == "5":
            product_id = int(input("ID del producto: "))
            print(client.delete_product(product_id))
        elif choice == "6":
            break

if __name__ == "__main__":
    main()