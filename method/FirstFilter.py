# threshold == 10 in x and y direction respectively

import shutil
import re
import os
import logging
import glob

class firstFilter:
    def __init__(self) -> None:
        if os.path.exists('./after_first_filter'):
            logging.info('./after_first_filter has already exited')
        else:
            os.mkdir('./after_first_filter')
            logging.info('create --> ./after_first_filter')
        
        if os.path.exists('./after_first_filter/feature_point_0'):
            logging.info('./after_first_filter/feature_point_0 has already exited')
        else:
            os.mkdir('./after_first_filter/feature_point_0')
            logging.info('create --> ./after_first_filter/feature_point_0')

        if os.path.exists('./after_first_filter/feature_point_1'):
            logging.info('./after_first_filter/feature_point_1 has already exited')
        else:
            os.mkdir('./after_first_filter/feature_point_1')
            logging.info('create --> ./after_first_filter/feature_point_1')
        
    
    def run(self,switch):

        if switch == 0:
            path = glob.glob('./feature_point_0/*_0_th.txt')
            target_path = './after_first_filter/feature_point_0'
        if switch == 1:
            path = glob.glob('./feature_point_1/*_1_th.txt')
            target_path = './after_first_filter/feature_point_1'

        for txt_name in path:

            list_x = []
            list_y = []
            
            txt_name = str(txt_name).replace('\\','/')

            with open(txt_name, "r") as f1:
                for line in f1.readlines():
                    # print(line)    # testing
                    # number = [int(temp)for temp in line.split() if temp.isdigit()]
                    number = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                    # print(number)    # testing
                    list_x.append(float(number[0]))    # format:float
                    # ↓ Counting from the bottom (img_col - feature_col)
                    list_y.append(float(number[1]))

            max_x = max(list_x)
            min_x = min(list_x)
            max_y = max(list_y)
            min_y = min(list_y)

            if float(max_x-min_x) > float(10) or float(max_y-min_y) > float(10):
                shutil.move(txt_name,target_path)

# TESTING========================================
# firstFilter().run(1)