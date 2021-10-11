


import random

def draw(deck):
    card=deck.pop()
    return card

def calc(hand): 
    s =0
    for card in hand: 
        if 9<card[1]:
            s+=0
        else:
            s+=card[1]
    return s

deck =[]
marks =["♡","♤","♢","♧"]
for mark in marks:
    for kazu in range(1,14):
        deck.append([mark,kazu])
    
random.shuffle(deck)

player =[]
banker =[]
print(type(calc(player)))
player.append(draw(deck))
player.append(draw(deck))
banker.append(draw(deck))
banker.append(draw(deck))
print(player)
print(banker)
playerscoer = int(str(calc(player))[-1])
bankerscoer = int(str(calc(banker))[-1])
if 8<=playerscoer<10 or 8<=bankerscoer<10:
    if playerscoer > bankerscoer:
         print(player)
         print(banker)
         print("playerwin")
    elif bankerscoer > playerscoer:
        print(player)
        print(banker)
        print("bankerwin")
    elif playerscoer == bankerscoer:
          print(player)
          print(banker)
          print("draw")


