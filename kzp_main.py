from random import randint
from kzp_probint import prob_check
sample = 1000000
prob = 319.68
rush_prob = 55
num = 0
count = 0

x,y,z=prob_check(prob)

jp = 10 ** z
jp_ls = []
while len(jp_ls) < jp:
    n = randint(1,y)
    if n not in jp_ls:
        jp_ls.append(n)
    else:
        pass

rush_ls = jp_ls[0:rush_prob]

while num not in jp_ls:
    count += 1
    num = randint(1,y)



print(count)
#print(rush_ls)
#print(len(rush_ls))
