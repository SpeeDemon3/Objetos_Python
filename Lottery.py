from random import choice

### Clase que representa un boleto de loteria
class Lottery:

    def __init__(self):
        self.list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']


    def winning_ticket(self):
        ticket = [] # Lista donde guardar el ticket ganador
        count = 0 # Contador para controlar el numero de elementos que entran en el ticket dentro de un if
        for index in range(0, len(self.list)):
            if count < 4:
                ticket.append(choice(self.list))
            count += 1 # Sumamos uno en cada iteracion

        print(f"The winning combination is {ticket}")

ticket_win = Lottery()
ticket_win.winning_ticket()

my_ticket = [3, 'a', 9, 'b']

winner = False

count_round = 0

# Comprobamos el numero de partidas necesarias para poder ganar el premio
while  not winner:

    if my_ticket == ticket_win:
        winner = True

    count_round += 1

print(f"Number of rounds {count_round}")