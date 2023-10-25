### Clase heroe, con sus atributos y metodos ###

class Hero:
    # Utilizando __init__() indicamos a python que ejecute este metodo cada vez que se cree una instancia(objeto)
    # El parametro self indica que cualquier atributo o metodo de la clase podra ser accedido desde la propia clase
    # Atributos de la clase
    def __init__(self, name, race):
        self.name = name # Inicializa el atributo
        self.race = race # Inicializa el atributo

    # Metodo para que el heroe ataque
    def attack(self):
        print(f"{self.name} is attacking!!!")

    # Metodo para que el heroe se defienda
    def defend(self):
        print(f"{self.name} is defending himself!!!")