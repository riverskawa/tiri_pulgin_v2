

def one():
    nums = [(40, 36), (89, 2), (36, 100), (7, 999)]

    case = (3, 100)
    if nums.count(case) == 0:
    #if nums.index(case) == 0:
        print(nums)
        nums.append(case)
        print('AFTER')
        print(nums)
    else:
        print('alreadt in list')

def yoa():
    aa=[('aadd','ad'),('ddaa','da')]
    for comb in aa:
        a,b = comb
        print(a,b)

from itertools import combinations
list_pts = ['aa','bb','cc']
list_pts_comb = combinations(list_pts,2)
print(type(list_pts_comb))
for i in list_pts_comb:
    print(i)