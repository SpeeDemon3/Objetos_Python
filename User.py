### Clase para representar usuarios ###
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    # Metodo para describir al usuario
    def describe_user(self):
        print(f"First Name: {self.first_name} || Last Name: {self.last_name}")

    # Metodo para saludar al usuario
    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}")

    # Metodo para incrementar los inicios de sesion
    def increase_login_attempts(self):
        self.login_attempts += 1 # Sumo 1 cada vez que se invoca al metodo desde un objeto

    # Metodo para restablecer el valor de los intentos de inicio a 0
    def reset_login_attempts(self):
        self.login_attempts = 0