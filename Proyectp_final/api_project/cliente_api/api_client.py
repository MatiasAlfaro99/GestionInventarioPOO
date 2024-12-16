import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        """Iniciar sesión y obtener un token JWT."""
        url = f"{self.base_url}/api/token/"
        data = {"username": username, "password": password}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            self.token = response.json().get("access")
            return "Inicio de sesión exitoso."
        return f"Error: {response.status_code} - {response.json().get('detail')}"

    def get_headers(self):
        """Encabezados con token JWT."""
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def list_products(self):
        """Listar productos."""
        url = f"{self.base_url}/api/productos/"
        response = requests.get(url, headers=self.get_headers())
        return response.json()

    def create_product(self, nombre, precio, stock, descripcion=""):
        """Crear un producto."""
        url = f"{self.base_url}/api/productos/"
        data = {"nombre": nombre, "precio": precio, "stock": stock, "descripcion": descripcion}
        response = requests.post(url, json=data, headers=self.get_headers())
        return response.json()

    def update_product(self, product_id, data):
        """Actualizar un producto."""
        url = f"{self.base_url}/api/productos/{product_id}/"
        response = requests.put(url, json=data, headers=self.get_headers())
        return response.json()

    def delete_product(self, product_id):
        """Eliminar un producto."""
        url = f"{self.base_url}/api/productos/{product_id}/"
        response = requests.delete(url, headers=self.get_headers())
        return response.status_code
