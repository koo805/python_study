# member = ["工藤", "松田", "浅木"]
# print(member[2])
# #リスト
# score = [88,90,95,75]
# total = sum(score)
# avg = total/len(score)
# print(f"合計{total}点　平均{avg}点")
# #平均値
# member.append("菅原")
# member.append("田中")
# member.append("山田")
# #追加処理
# member.pop("松田")
# #削除処理
# member[3] = "松本"
# #更新処理
# print(member)
# a = [10,20,30,40,50]
# print(a[1:3])
# print(a[2:1])
# print(a[-1])
# print(a[-1])
# #スライス処理
# score = {"network":60, "deatbase":80, "security":50}
# score["programing"] = 65
# score["deatbase"] = 99
# del score["security"]
# print(score)

# member_hobise = {
#     "松田":{'SNS', '麻雀', '自動車'},
#     "浅木":{"麻雀", "食べ歩き","数学","数学","数学"}
# }
# print(member_hobise["松田"]&member_hobise["浅木"])

# a = {1,2,3,4}
# b = {2,3,4,5}
# print(a | b)
# print(a & b)
# print(a - b)
# print(a ^ b)

# ja = int(input())
# ma = int(input())
# en = int(input())
# se = int(input())
# so = int(input())
# score = [ja,ma,en,se,so]
# total = sum(score)
# avg = total/len(score)
# print(f"合計{total}点　平均{avg}点")



# a = {"a", "b", "c", "d", "e"}
# b = {"a", "b", "c", "d", "e"}
# input = ("心の準備ができてから、enter keyを押してください")
# d = a&b
# e = a|b
# f = len(d) / len(e) * 100
# print(f)

""" name = "工藤"
food = input('{}さんの好きな食べ物を教えてくださいー＞'.format(name))
if 'カレー' in food:
    print("カレーいいですよね")
else:
    print('私も{}が好きですよ'.format(food))

score = {"network":60}

key = "work"
if key in score:
    print("a")
else:
    print("b")
 """

#if not(day in [28,30,31])


isError = False
n = 99
if isError == False and n < 100:
    print("正解")


number = int(input('数値を入力してください'))
if number % 2 == 0:
    print('偶数です')
else:
    print('奇数です')

greeting = input('')

