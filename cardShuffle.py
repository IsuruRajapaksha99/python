
import random,itertools


player_1=[]
player_2=[]
player_3=[]
player_4=[]


deck = list(itertools.product([7,8,9,10,"J","Q","K","A"],["spade","club","heart","diamond"]))
random.shuffle(deck)

for i in range(8):
    player_1.append(deck[i])

for i in range(9,16):
    player_2.append(deck[i])

for i in range(17,24):
    player_3.append(deck[i])

for i in range(25,32):
    player_4.append(deck[i])



print(player_1)
print(player_2)
print(player_3)
print(player_4)
