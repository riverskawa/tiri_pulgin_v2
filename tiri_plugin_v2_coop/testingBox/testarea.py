

# def one():
#     nums = [(40, 36), (89, 2), (36, 100), (7, 999)]

#     case = (3, 100)
#     if nums.count(case) == 0:
#     #if nums.index(case) == 0:
#         print(nums)
#         nums.append(case)
#         print('AFTER')
#         print(nums)
#     else:
#         print('alreadt in list')

# def yoa():
#     aa=[('aadd','ad'),('ddaa','da')]
#     for comb in aa:
#         a,b = comb
#         print(a,b)

# from itertools import combinations
# list_pts = ['aa','bb','cc']
# list_pts_comb = combinations(list_pts,2)
# print(type(list_pts_comb))
# for i in list_pts_comb:
#     print(i)

#============================================

# import glob
# import math
# print(math.comb(len(glob.glob('./after_first_filter/feature_point_0/*')),2))

#============================================

# import glob

# list_root = []

# base = './sdsdsds/dsds'

# for i in glob.glob('./testingBox/*.py'):
#     list_root.append([base,i])

# print(list_root)


# ds = []
# for i in range (1,10):
#     ds.append(i)

# path = 'output.txt'
# f = open(path, 'w')
# for i in (ds):
#     f.write(str(i)+'\n')
# f.write(str(123))
# f.write(str(123.45))
# f.close()


# ss = '97_0_th_82_0_th_5'

# print(type(ss.split('_')[6]))
# import re

# with open('./excel_cam_0/97_0_th_96_0_th_5.txt') as f1:
#     for line in f1.readlines():
#         # print(line)    # testing
#         # number = [int(temp)for temp in line.split() if temp.isdigit()]
#         disp = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
#         print(float(line))
#         print(type(float(line)))

# import glob

# ls_base = [] 
# for base_pt in glob.glob('./excel_cam_0/region_1/*.txt'):
#     base_pt = base_pt.replace('./excel_cam_0/region_1/','')
#     base_pt = base_pt.split('_')[0]
#     if base_pt not in ls_base:
#         ls_base.append(base_pt)


# ss = '345_0'

# print(ss.find('34_'))

aa = 22
bb = 22
if str(aa) == str(bb):
    print('work')