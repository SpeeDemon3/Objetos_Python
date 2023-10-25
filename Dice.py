from random import randint
### Clase para representar un dado
class Dice:

    def __init__(self, face_dice = 6):
        self.face_dice = face_dice


    def roll_dice(self):
        print(randint(1, self.face_dice))


# Creo una instancia de un dado de 6 caras
print("Six sided dice")
dice = Dice()
dice.roll_dice()

# Dado de 10 caras
dice_10 = Dice(10)
print("Ten sided dice:")
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()

dice_20 = Dice(20)
print("Twenty sided dice")
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
