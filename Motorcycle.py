### Clase con los metodos y atributos de un coche ###

class Motorcycle:
    # Atributos
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 0    

    # Metodo para obtener la descripcion de la moto
    def get_describe_motorcycle(self):
        long_describe = f"{self.make} {self.model} {self.year}"
        return long_describe

    # Metodo para obtener los kilometros que tiene la moto
    def read_odemeter(self):
        print(f"This motorcycle has {self.odemeter_reading} kilometres on it.")

    # Metodo para actualizar los kilometros
    def update_odemeter(self, kilometres):
        if kilometres >= 0: # Si los kilometros son positivos
            self.odemeter_reading += kilometres # Se suman a los kilometros actuales
        else: # Si no se avisa por consola de que la operacion NO se puede realizar
            print("You can't roll back an odemeter!")


# Clase bateria
class Battery:
    # Atributos
    def __init__(self, battery_size = 33): # batery_size tendra un valor por defecto
        self.battery_size = battery_size

    # Metodo que indica la autonomia de la bateria segun su tamaño
    def get_range(self):
        if self.battery_size > 100: # Si el tamaño es mayor a 100
            range = 300
        elif self.battery_size < 50: # Si el tamaño es menor a 50
            range = 150

        print(f"This motorcycle can go about {range} kilometres on a full charge.")

    # Metodo para obtener la informacion de la bateria
    def describe_batery(self):
        print(f"This motorcycle has a {self.battery_size}kwh batery.")


# Clase que hereda de la clase Motorcycle
class ElectricMotorcycle(Motorcycle):

    # Inicio los atributos que pertenecen a la clase padre
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # Utilizando el metodo super() obtenemos todos los atributos de la clase padre
        # Atributos propios de la clase ElectricMotorcycle
        self.battery_size = Battery() # Este atributo recibe un objeto de la clase Batery
