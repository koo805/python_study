import random
HP = 100
monster = 100
while HP>0:
    aite = random.randint(1,3)      # 1,2,3
    line = input("じゃんけん")          # グー
    if line == "グー":
        jibun = 1           # グー
    elif line == "チョキ":
        jibun = 2           # チョキ
    else:
        jibun = 3           # パー
    if jibun == aite:       # jibun == 1 and aite == 1 , jibun == 2 and aite == 2 , jibun == 3 and aite == 3
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
    if text == "負け":
        HP -= 20
    elif text == "ひきわけ":
        HP -= 0
    if text == "勝ち":
        monster -= 20
    elif text == "ひきわけ":
        monster -= 0
    print("自分の体力100HP/" + str(HP) + line)
    print("モンスターの体力100HP/" + str(monster) + aitestr)
    print(text)
print("0になった、ゲームオーバー")
