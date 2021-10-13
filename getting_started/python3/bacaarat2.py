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
print(str(calc(player))[-1])
print(str(calc(banker))[-1])
if  (str(calc(player))[-1]) == "8" or (str(calc(player))[-1])  == "9" or (str(calc(banker))[-1]) == "8" or (str(calc(banker))[-1]) =="9":
    if (str(calc(banker))[-1]) == (str(calc(player))[-1]) :
        print("タイ")
    elif int(str(calc(banker))[-1]) > int(str(calc(player))[-1]):
        print("バンカーの勝ち")
    else:
        print("プレイヤーの勝ち")
elif str(calc(player))[-1] <= "5":
     print("もう一枚引く")
elif str(calc(player))[-1] <= "8" or str(calc(player))[-1] >= "6":
      print("もう引かない")
    


    #print("ナチュラルウィンではない")

      #print("プレイヤーのナチュラルウィン")


# if str(calc(player))[-1] == "8"  and  str(calc(banker))[-1] == "8":
#     print("aa")

# if  str(calc(player))[-1] == "9"  and  str(calc(banker))[-1] == "9":
#     print("a")
# if str(calc(player))[-1] == "9"  and  str(calc(banker))[-1] == "8":
#     print("プレイヤーの勝ち")
# if str(calc(player))[-1] == "8"  and  str(calc(banker))[-1] == "9":
#     print("バンカーの勝ち")
 





    #  else:
    # print("ナチュラルウィンではない")
    



# playerscore =(str(calc(player))[-1])
# bankerscore = str(calc(banker))[-1])
# if 8<= playerscore <10 or 8 <= bankerscore < 10:
#     print()



