from random import randint
from kzp_probint import prob_check
from kzp_result import result
sample = 100000    #試行回数
prob = 319.68       #確率
rush_prob = 0.55

y,z=prob_check(prob)
# y:整数変換後の確率　z:10倍回数

jp = 10 ** z
rush_prob *= 10 ** z
rush_prob = int(rush_prob)
jp_ls = []
while len(jp_ls) < jp:
    n = randint(1,y)
    if n not in jp_ls:
        jp_ls.append(n)
    else:
        pass

rush_ls = jp_ls[0:rush_prob]
c_rush = []
c_jp = []

for i in range(sample):
    pick_num = 0
    count = 0
    while pick_num not in jp_ls:
        count += 1
        pick_num= randint(1,y)
        if pick_num in rush_ls:
            c_rush.append(count)
        elif pick_num in jp_ls:
            c_jp.append(count)
        else:
            pass

result(c_jp,c_rush)