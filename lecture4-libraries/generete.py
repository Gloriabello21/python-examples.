#ejemplo1
import random 

coin = random.choice(["heads","tails"])
print(coin)

#ejempplo2
from random import choice

coin = choice(["heads", "tails"])
print(coin)

#ejemplo3
import random
number = random.randint(1, 10)
print(number)

#ejemplo4
import random
cards = ["jack", "queen", "king"]
random.shufles(cards)
for card in cards:
    print(card)