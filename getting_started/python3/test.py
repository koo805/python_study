#ja = int(input())
#ma = int(input())
#en = int(input())
#se = int(input())
#so = int(input())
#score = [ja,ma,en,se,so]
#total = sum(score)
#avg = total/len(score)
#print(f"合計{total}点　平均{avg}点")

# is_awake = True
# count = 0
# while is_awake:
#     count +=1
#     print("羊が{}匹".format(count))
#     key = input("もう眠りそうですか？ (y/n) >>")
#     if key=="y":
#         is_awake =False
# print("おやすみなさい")

# count = 0
# student_num = int(input("学生の数を入力＞＞"))
# score_list = list()
# while count < student_num:
#     count += 1
#     score = int(input("{}人目の試験の得点を入力＞＞".format(count)))
#     score_list.append(score)
# print(score_list)
# total = sum(score_list)
# print("平均点は{}点です".format(total / student_num))

# scores = [80,20,75,60]
# count = 0
# while count < len(scores):
#     if score[count] >= 60:
#         print("合格")
#     else:
#         print("不合格")
#     count += 1

# scores = [80,20,75,60]
# for data in scores:
#     if data >= 60:
#         print("合格")
#     else:
#         print("不合格")

# for num in range(3):
#     print("pythonは楽しい" + str(num))

# ages = [28,50,8,20,78,25,22,10,27,33]
# num = 5
# samples = list()
# for age in ages:
#     if 20 <= age < 30:
#         if len(samples) < 5:
#             samples.append(age)
#             if len(samples) == num:
#                 break
# print(samples)
# is_awake = True
# count = 0
# print("カレーを召し上がれ")
# while is_awake  == True:
#     print("{}皿のカレーを食べました".format(count))
#     key = input("おかわはいかがですか？ (y/n) >>")
#     if key=="y":
#         count += 1
#     else:    
#         is_awake = False
# print("ご馳走様でした")




# for i in range(10):
#     print("{},".format(10 - i),end="")
# print("left off")

# for i in range(9):
#     for j in range(9):
#         print("{}*{}={}".format(i + 1,j + 1 (i + 1)*(j + 1)))


# temp = list()
# deta = [7.8,9.1,10.2,11.0,12.5,12.4,14.3,13.8,12.9,12.4]
# temp = []
# for i in deta:
#      temp.append[i]

# for count in range(len(temp)):
#     print("{}時")




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
def make_deck():
     deck =[]
     marks =["♡","♤","♢","♧"]
     for mark in marks:
         for kazu in range(1,14):
          deck.append([mark,kazu])
    
     random.shuffle(deck)
     return deck

deck = make_deck()
player =[]
banker =[]


money = 100000

while True :
    print("現在の所持金は"+str(money)+"円です。")
    if money<=0:
        print("所持金は０円になりました。")
        break
    predict = int(input("[誰に賭けますか？プレイヤー；０、バンカー；１、引き分け；２]"))
    bet = int(input("いくら賭けますか？"))
    if money<bet:
        bet = money
        print("全財産を賭け金とします。")
    money-=bet
    if len(deck)<=10:
        deck = make_deck()
    #プレーヤー・バンカーの順番で2枚ずつ交互に配布
    for i in range(2):
        player.append(draw(deck))
        banker.append(draw(deck))
    print(player)
    print(banker)

print(type(calc(player)))
player.append(draw(deck))
player.append(draw(deck))
banker.append(draw(deck))
banker.append(draw(deck))
print(player)
print(banker)
print(str(calc(player))[-1])
print(str(calc(banker))[-1])
if str(calc(player))[-1] == "8" or  str(calc(player))[-1] == "9" or str(calc(banker))[-1] == "8" or str(calc(banker))[-1] =="9":
    if str(calc(banker))[-1] ==  str(calc(player))[-1]:
        print("タイ")
    elif int(str(calc(banker))[-1])> int(str(calc(player))[-1]):
        print("バンカーの勝ち")
    else:
        print("プレイヤーの勝ち")
elif str(calc(player))[-1] <= "６":
     print("もう一枚引く")
elif str(calc(player))[-1] <= "8" or str(calc(player))[-1] >= "6":
     print("もう引かない")
    