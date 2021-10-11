import random
HP = 100
monster = 100
kurikaesi = 0
print("じゃんけんゲームスタート！")
while HP>0:
    aite = random.randint(1,3)      # 1,2,3
    line = input("自分の手を入力してください")          # グー
    if line == "グー":
        jibun = 1           # グー
    elif line == "チョキ":
        jibun = 2           # チョキ
    else:
        jibun = 3           # パー   　　↓jibun == 3 and aite == 3
    if jibun == aite:       # jibun == 1 and aite == 1 , jibun == 2 and aite == 2 
        aitestr = line      # line == "グー"
        text = "ひきわけ"
    elif jibun == 1:
        if aite == 2:
            aitestr = "チョキ"
            text = "勝ち"
        if aite == 3:
            aitestr = "パー"
            text = "負け"
    elif jibun == 2:
        if aite == 3:
            aitestr = "パー"
            text = "勝ち"
        if aite == 1:
            aitestr = "グー"
            text = "負け"
    else:
        if aite == 1:
            aitestr = "グー"
            text = "勝ち"
        if aite == 2:
            aitestr = "チョキ"
            text = "負け"
    print("自分の手" + line)
    print("モンスターの手" + aitestr)
    print(text)
    kurikaesi += 1
    make = 10
    damage = 10
    if text == "負け":
        print("負けHPが減るよ")
        HP -= make
    print("自分のHP"+str(HP))
    if text == "勝ち":
        monster -= damage
    print("モンスターのHP"+str(monster))
    if HP <=0:
        print("負け")
        print("繰り返し回数"+str(kurikaesi))
    if monster <=0:
        print("勝ち")
        print("繰り返し回数"+str(kurikaesi))
#print("0になった、ゲームオーバー、乙です")

