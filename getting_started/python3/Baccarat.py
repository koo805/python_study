#カード除法作成

#プレイヤーとバンカーと交互にカードを配布　（計二枚）

# class card():
#     suit = ("♤" "♡" "♧" "♢")
#     number = ("A" "2" "3" "4" "5" "6" "7" "8" "9" "10" "J" "Q" "K")
    

# import random
    
# def drew(deck):
#     card = deck.pop()
#     return card

# deck = []


import random
# Constants
# SUITS = ('♡', '◇', '♠', '♣')
# RANKS = ('Ａ', '２', '３', '４', '５', '６', '７', '８', '９', '10', 'Ｊ', 'Ｑ', 'Ｋ')
# CARD_VAL = {'２':2, '３':3, '４':4, '５':5, '６':6, '７':7, '８':8, '９':9, '10':10, 'Ｊ':10, 'Ｑ':10, 'Ｋ':10, 'Ａ':11}
# class Card(object):
    
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank
        
#     def __str__(self):
#         return  self.suit + ' ' + self.rank
    
# class Deck(object):
    
#     def __init__(self):
#         self.deck = [] 
#         for suit in SUITS:
#             for rank in RANKS:
#                 self.deck.append(Card(suit,rank))
#         random.shuffle()
#         random.shuffle(self)
# player =[]
# banker =[]
# player.append((self))
# player.append(draw(deck))
# banker.append(draw(deck))
# banker.append(draw(deck))
# print(player)



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
#プレーヤー・バンカーの順番で2枚ずつ交互に配布
for i in range(2):
    player.append(draw(deck))
    banker.append(draw(deck))
print(player)
print(banker)
pghyouka = (int(str(calc(player))[-1]))
bghyouka = (int(str(calc(banker))[-1]))
print(pghyouka)
print(bghyouka)
#プレーヤーの合計 (1の位のみ )がどれに当てはまるかを見て2枚または3枚のプレーヤーの値を決める。
if  8<=pghyouka<10:  #プレーヤーの合計　8・9　勝負判定 
    if pghyouka>bghyouka:
        print("勝利")
        print(player)
        print(banker)
    elif pghyouka<bghyouka:
        print("敗北")
        print(player)
        print(banker)
    elif pghyouka==bghyouka:
        print("引き分け")
        print(player)
        print(banker)
    else:
        if pghyouka>bghyouka:
            print("勝利")
            print(player)
            print(banker)
        elif pghyouka<bghyouka:
            print("敗北")
            print(player)
            print(banker)
        elif pghyouka==bghyouka:
            print("引き分け")
            print(player)
            print(banker)
elif 6<=pghyouka<8 and bghyouka<6:  #プレーヤーの合計6・7 もう引かない
    banker.append(draw(deck))  #プレーヤーが2枚目で終了の場合、バンカーが、0~5の場合はバンカーにもう一枚引く。
    print(banker)  
    if pghyouka>bghyouka:
        print("勝利")
        print(player)
        print(banker)
    elif pghyouka<bghyouka:
        print("敗北")
        print(player)
        print(banker)
    elif pghyouka==bghyouka:
        print("引き分け")
        print(player)
        print(banker)
    else:
        if pghyouka>bghyouka:
            print("勝利")
            print(player)
            print(banker)
        elif pghyouka<bghyouka:
            print("敗北")
            print(player)
            print(banker)
        elif pghyouka==bghyouka:
            print("引き分け")
            print(player)
            print(banker)
elif pghyouka<6: #プレーヤーの合計が0~5
    player.append(draw(deck))#もう一枚引く、プレーヤーが3枚目で終了の場合
    if bghyouka<3:  #バンカー０〜２
        banker.append(draw(deck))
        print(banker)
        if pghyouka>bghyouka:
            print("勝利")
            print(player)
            print(banker)
        elif pghyouka<bghyouka:
            print("敗北")
            print(player)
            print(banker)
        elif pghyouka==bghyouka:
            print("引き分け")
            print(player)
            print(banker)
    elif bghyouka ==3 and 0<=pghyouka<8:  #バンカ−３
        banker.append(draw(deck))
        print(banker)
        if pghyouka>bghyouka:
            print("勝利")
            print(player)
            print(banker)
        elif pghyouka<bghyouka:
            print("敗北")
            print(player)
            print(banker)
        elif pghyouka==bghyouka:
            print("引き分け")
            print(player)
            print(banker)
    elif bghyouka ==4 and 2<=pghyouka<8:  #バンカー４
        banker.append(draw(deck))
        print(banker)
        if pghyouka>bghyouka:
            print("勝利")
            print(player)
            print(banker)
        elif pghyouka<bghyouka:
            print("敗北")
            print(player)
            print(banker)
        elif pghyouka==bghyouka:
            print("引き分け")
            print(player)
            print(banker)
    elif bghyouka ==5 and 4<=pghyouka<8:  #バンカ−５
        banker.append(draw(deck))
        print(banker)
        if pghyouka>bghyouka:
            print("勝利")
            print(player)
            print(banker)
        elif pghyouka<bghyouka:
            print("敗北")
            print(player)
            print(banker)
        elif pghyouka==bghyouka:
            print("引き分け")
            print(player)
            print(banker)
    elif bghyouka ==6 and 6<=pghyouka<8:  #バンカー６
        banker.append(draw(deck))
        print(banker)
        if pghyouka>bghyouka:
            print("勝利")
            print(player)
            print(banker)
        elif pghyouka<bghyouka:
            print("敗北")
            print(player)
            print(banker)
        elif pghyouka==bghyouka:
            print("引き分け")
            print(player)
            print(banker)
    else:
        if pghyouka>bghyouka:
            print("勝利")
            print(player)
            print(banker)
        elif pghyouka<bghyouka:
            print("敗北")
            print(player)
            print(banker)
        elif pghyouka==bghyouka:
            print("引き分け")
            print(player)
            print(banker)
else:
    if pghyouka>bghyouka:
        print("勝利")
        print(player)
        print(banker)
    elif pghyouka<bghyouka:
        print("敗北")
        print(player)
        print(banker)
    elif pghyouka==bghyouka:
        print("引き分け")
        print(player)
        print(banker)









































    
            
                
 


 
 