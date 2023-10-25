### Clase que simula un rataurante ###
class Restaurant:
    def __init__(self, restaurant_name, type_kitchen):
        self.restaurant_name = restaurant_name
        self.type_kitchen = type_kitchen
        self.profits = 0

    # Metodo para mostrar los datos del restaurante
    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name} || Tipe of kitchen: {self.type_kitchen}")

    # Metodo para indicar si el restaurante esta abierto
    def open_restaurant(self):
        print("This restaurant is open")

    # Metodo para obtener las ganancias generadas por el restaurante
    def profits_generated(self):
        print(f"The profits generated are {self.profits}")

    # Metodo para actualizar las ganancias
    def update_earnings(self, profit):
        self.profits += profit # Cambia el valor del atributo por el valor añadido