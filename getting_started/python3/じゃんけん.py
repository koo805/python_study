import random
HP = 100
monster = 100
print("じゃんけんゲームスタート！")
while HP>=0 or monster >=0:


        aite = random.randint(1,3)      # 1,2,3
        line = input("自分の手を入力してください")          # グー
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
            print("負けHPが減るよ！　雑魚GG")
            HP -= 20
        elif text == "ひきわけ":
            HP -= 0
        

        if text == "勝ち":
            monster -= 20
        elif text == "ひきわけ":
            monster -= 0
        
        
          

            
        
        print("自分の手" + line)
        print("モンスターの手" + aitestr)
        print("自分の体力100HP/" + str(HP) + "HP")
        print("モンスターの体力100HP/" + str(monster) + "HP")
        print(text)
        if HP == 0:
            break
        if monster == 0:
            break
if HP ==0:
    print("プレイヤーの負け")
if monster ==0:
    print("プレイヤーの勝利")
    print("おめでとう！")



#if monster == 0:
#    print("プレイヤーの勝利")





