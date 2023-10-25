### Clases ###
from Hero import Hero
from Restaurant import Restaurant
from User import User
from Motorcycle import ElectricMotorcycle
# Crear una instancia de la clase Hero
hero_spiderman = Hero('Peter', 'human')

print(f"Hi, I'm your friend and neighbor {hero_spiderman.name}!!!") # Accedemos al atributo name del objeto

race_spiderman = hero_spiderman.race # Asigno la raza de spiderman a una variable
print(race_spiderman) # Imprimo su valor

# Metodos de la clase Hero usados por la instancia
hero_spiderman.attack()
hero_spiderman.defend()

# Creo un seguindo objeto de la clase Hero
hero_venom = Hero("Brock", "synvioid")
print(f"I'm {hero_venom.name} and I'm going to eat you!!!")
print(f"{hero_venom.name} is a {hero_venom.race}")

hero_venom.attack() # Invoco al metodo attack de la clase Hero

# Creo una instancia(objeto) de la clase Restaurant
restaurant = Restaurant("The kitchen of hell", "street kitchen")
print(restaurant.restaurant_name)
print(restaurant.type_kitchen)

restaurant.describe_restaurant()

restaurant_2 = Restaurant("Wakanda", "advanced cooking")
restaurant_2.describe_restaurant()

# Creo 2 instancias de la clase User
user_1 = User("Antonio", "Ruiz")
user_2 = User("Chula", "Ruiz")

user_1.greet_user()
user_2.greet_user()

user_1.describe_user()
user_2.describe_user()

print(user_1.login_attempts) # Compruebo los inicios de sesion que realiza el usuario
user_1.increase_login_attempts()
user_1.increase_login_attempts()

print(user_1.login_attempts) # Compruebo los inicios de sesion que realiza el usuario

user_1.reset_login_attempts() # Reseteo el numero de inicios a 0
print(user_1.login_attempts) # Compruebo los inicios de sesion que realiza el usuario



### Modificar el valor de un atributo directamente ###
# Creo un objeto
restaurant_3 = Restaurant("Urban 3", "contemporary")
# Compruebo las ganancias del restaurante utilizando el metodo
restaurant_3.profits_generated()
# Asigno el valor al atributo
restaurant_3.profits = 3000
# Utilizando el metodo obtengo las ganancias del atributo y compruebo si se a modificado
restaurant_3.profits_generated()

### Modificar el valor de un atributo a traves de un metodo ###
restaurant_3.update_earnings(5000) # Sumo 5000 mas a las ganancias del restaurante
restaurant_3.profits_generated()

### HERENCIA ###
# Objeto que hereda de la clase Motorcycle, teniendo los mismo atributos que la clase padre
my_cupra = ElectricMotorcycle('seat', '300', 2017)
print(my_cupra.get_describe_motorcycle()) # Metodo heredado de la clase padre
my_cupra.battery_size.describe_batery() # Metodo propio de la clase hija que a su vez utiliza un metodo de la clase Battery
my_cupra.battery_size.get_range() # Metodo de la clase Battery
