import glob
import shutil
import os

list_path = []
list_path_before= []
index_num = 0
for i in glob.glob('./temp_img_0/*_0.bmp'):
    path = str(i)
    list_path_before.append(path)
    path = path.replace('./temp_img_0/','')
    path= path.replace('C_0.bmp','')
    key_set = [path,index_num]
    list_path.append(key_set)
    index_num+=1

print(list_path) # for testing
print('=============================================================')
list_path.sort(key=lambda x:x[0])
print(list_path) # for testing


#----------------------------------------------------
# os.mkdir('./img_0_sorted')
# os.mkdir('./img_1_sorted')

# for i in range (len(list_path)):
#     old_index = int(list_path[i][0])
#     path_to_work=str(list_path_before[old_index])