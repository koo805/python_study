#9/2　木　１コマ オリジナルの関数
""" student_list = ['浅木','松田']
count = 0

for student in student_list:
    print('{}さんの試験結果を入力してください'.format(student))
    network = int(input('ネットワークの得点？　＞＞'))
    database = int(input('データベースの得点？＞＞'))
    security = int(input('セキュリティの得点？'))
    if student == '浅木':
        asagi_scores = [network, database,security]
        asagi_avg = sum(asagi_scores) / len(asagi_scores)
    else:
        matsuda_scores = [network,database,security]
        matsuda_avg = sum(matsuda_scores) / len(matsuda_scores)
print('浅木さんの平均点は{}です'.format(asagi_avg))
print('松田さんの平均点は{}です'.format(matsuda_avg)) """
#hello 関数の定義　（スッテプ１）
""" def hello():
    print('こんにちは。工藤です。')
#関数の呼び出し　（スッテプ２）
hello() """
#関数は独立して一つの世界
""" def input_scores():
    name = ''  #関数内部で宣言された変数　ローカル変数
    print('浅木さん試験結果を入力してください'.format(name))

name = '浅木'
input_scores()

name = '松田'
input_scores() """
#引数と戻り値　２コマ
""" def profile(name, age, hobby):
    print("私の名前は{}です".format(name))
    print("年齢は{}才です。".format(age))
    print("趣味は{}です。".format(hobby))

profile("浅木",24, "カフェ巡り") """
#
""" def input_scores(name):
    print("{}さんの試験結果を入力してください".format(name))
    network = int(input("ネットワークの得点？　＞＞"))
    datebase = int(input("データベースの得点？　＞＞"))
    security = int(input("セキュリティーの得点？　＞＞"))
    scores = [network, datebase, security]
    return scores

def calc_average(scores):
    avg = sum(scores) / len(scores)
    print("平均点は{}です".format(avg))

def output_result(name,avg):
    print("{}さんの平均点は{}です".format(name,avg))

asagi_scores = input_scores("浅木")
matsuda_scores = input_scores("松田")

asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)

output_result("浅木",asagi_avg)
output_result("松田",matsuda_avg) """


""" def plus(x,y):
    answer = x + y
    return answer

answer = plus(100,50)
print("足し算の答えは{}です".format(answer)) """
#
""" def eat(blackfast, lunch="ラーメン", dinner="カレー", *desserts):
    print("朝は{}を食べました".format(blackfast))
    print("昼は{}を食べました".format(lunch))
    print("夜は{}を食べました".format(dinner))
    for d in desserts:
        print("おやつに{}を食べました".format(d))

print("8月1日")
eat ("おにぎり")
print("8月２日")
eat(dinner="カレーうどん",blackfast="納豆ご飯")
print("8月3日")
eat("バナナ","そば","焼肉")
print("8月4日")
eat("サンドウィッチ", "焼肉弁当") 
eat("トースト","パスタ","カレー") """

""" name = "松田" #グローバル変数

def change_name():
    global name
    name = "浅木"

def hello():
    print("こんにちは" + name + "さん")

change_name()
hello() """
#9/6 1




""" def is_leapyear(seireki):
    if seireki % 400 == 0:
       return True
    elif seireki % 4 == 0 and seireki % 100 != 0:
        return True
    else:
        return False



seireki = int(input("西暦を入力してください。閏年であるか判断します"))
flag = is_leapyear(seireki)
print("西暦{}年は、".format(seireki), end="")
if flag:
    print("閏年です")
else:
    print("閏年ではありません") """

#p237の練習5-2にチャレンジ
""" def take_bus():
    print("バスに乗る")
    return [100,200,100]

[x,n,a] = take_bus() """

""" def int_input(message):
    return int(input("{}を入力してください".format(message)))

def clac_payment(amount,people=2):
    dnum = amount / people
    pay = dnum // 100 * 100
    if dnum > pay:
        pay = int(pay+100)
    payorg = amount =pay *(people-1)
    
    return [int(pay),int(payorg)]

def show_payment(pay,payorg,people=2):
    print("***支払額***")
    print("一人あたり{}円{}人)、幹事は{}円です".format(pay,people-1,payorg))

amount = int_input("支払総額")
people = int_input("参加人数")
pay_list = clac_payment(amount,people)
show_payment(pay_list[0],pay_list[1],people) """

#開発環境
""" userinfo = input("名前と血液型をカンマで区切って1行で入力＞＞")
[name, blood] = userinfo.split((","))   #オブジェクトを持っているから呼び出せる。　(.splitなど)
blood = blood.upper().strip()  #upper= 全て大文字にする　#strip　前後を空白にする
print("{}さんは{}型なので大吉です".format(name,blood)) """


#たくさんのメソットがある
#9/9 木 
# int_value = 10
# int_value = int(10)


# list_value1 = []
# list_value1 = list()

# class Hero:
#     name = "松田"
#     hp = 100

#     def sleep(self,hours):
#         print("{}は{}時間寝た！".format(self.name,hours))
#         self.hp += hours

# print("スッキリファンタジーXII ~金色の理想郷~")
# h = Hero()
# h.sleep(3)
# print("{}のhpは現在{}です".format(h.name,h.hp)
# )

# scores1 = [80,40,50]
# scores2 = [80,40,50]

# print("scores1のidentity:{}".format(id(scores1)))
# print("scores2のidentity:{}".format(id(scores2)))

# if scores1 == scores2:
#     print("scr1とscr2は同じ内容")
# else:
#     print("scr1とscr2は違う内容")

# if id(scores1) == id(scores2):
#     print("scr1とscr2は同じ存在")
# else:
#     print("scr1とscr2は違う存在")



""" 
def  add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + "さん"
    return names


before_names = ["松田","浅木","工藤"]
copied_names = list()
for n  in before_names:
    copied_names.append(n)

after_names = add_suffix(copied_names)
print("さん付け後" + after_names[0])
print("さん付け前" + before_names[0]) """
#参照値
# def add_suffix(name): #defとは、英語のdefine（定義する）
#     name = name + "さん"
#     return name 
# before_name = "松田"
# after_name = add_suffix(before_name)
# print("さん付け後:" + after_name)
# print("さん付け前:" + before_name)
#だべーじだべーじ破棄

# def welcome(u):
#     print("ようこそ{}さん".format(u["name"]))
#     u["age"] = u["age"] + 1
#     print("あなたは来年{}才だから大吉です！".format(u["age"]))

# username = input("名前を入力してください＞＞")
# usename = int(input("年齢を入力してください＞＞"))
# user = {"name":username,"age":username}
# copied_user = user.copy()
# welcome(copied_user)
# print("{}才の{}さん、またプレイしてくださいね" .format(user["age"],user["name"]))

# text = input("何を記録しますか？＞＞")
# # file = open("diary.txt", "a")
# # file.write(text + "\n")
# # file.close()
# with open("diary.txt,","a") as file:
#     file.write(text + "\n")

# import math
# print("円周率は{}です".format(math.pi))
# print("小数点以下を切り捨てれば{}です".format(math.floor)
"""9/13"""
#import math as m
# from math import pi
# from math import floor,ceil
# print("円周率の{}です".format(pi))
# print("小数点以下を切り捨てれば{}です".format(floor(pi)))
# print("小数点以下を切り上げれば{}です".format(ceil(pi)))

# def log(msg):
#     print("{}を記録します".format(msg))

# log(10)

# import http.client
# from http.client import client
# from http.client import HTTPConnection

# conn = HTTPConnection("www.python.org")



# nums = list()
# for n in range(3):
#     data = int(input("{}個数の整数を入力してください＞＞＞".format(n + 1)))
#     nums.append(data)
# print(max(nums))


# pi = 3.141519
# print(round(pi))
# for n in range(4):
#     print(round(pi, n+ 2))

# file_r = open("sample.txt","r")
# file_w = open("copy.txt","w")

# for line in file:
#     print(line)
# file.close()


