from glob import glob
import cv2
import os
import re
import shutil
import logging


class region_split:
    def __init__(self) -> None:
        pass


    def second_region(self,img_path = './temp_img_0'):
        list_img = os.listdir(img_path)
        img_0 = './temp_img_0/'+str(list_img[0])
        img = cv2.imread(img_0)
        size = img.shape
        self.half_size_r = float(size[0])/2
        self.half_size_c = float(size[1])/2
        # print(size) # --> (row.col,channel) 
        # print(type(size)) #--> tuple (int,int)
        # self.size_global = size


    def data_split(self):
        
        # for feature_point_0
        if os.path.exists('./after_first_filter/feature_point_0/region_1'):
            logging.info('./after_first_filter/feature_point_0/region_1 has already exited')
        else:
            os.system('mkdir ./after_first_filter/feature_point_0/region_1')

        if os.path.exists('./after_first_filter/feature_point_0/region_2'):
            logging.info('./after_first_filter/feature_point_0/region_2 has already exited')
        else:
            os.system('mkdir ./after_first_filter/feature_point_0/region_2')

        if os.path.exists('./after_first_filter/feature_point_0/region_3'):
            logging.info('./after_first_filter/feature_point_0/region_3 has already exited')
        else:
            os.system('mkdir ./after_first_filter/feature_point_0/region_3')

        if os.path.exists('./after_first_filter/feature_point_0/region_4'):
            logging.info('./after_first_filter/feature_point_0/region_4 has already exited')
        else:
            os.system('mkdir ./after_first_filter/feature_point_0/region_4')

        # for feature_point_0
        if os.path.exists('./after_first_filter/feature_point_1/region_1'):
            logging.info('./after_first_filter/feature_point_1/region_1 has already exited')
        else:
            os.system('mkdir ./after_first_filter/feature_point_1/region_1')

        if os.path.exists('./after_first_filter/feature_point_1/region_2'):
            logging.info('./after_first_filter/feature_point_1/region_2 has already exited')
        else:
            os.system('mkdir ./after_first_filter/feature_point_1/region_2')

        if os.path.exists('./after_first_filter/feature_point_1/region_3'):
            logging.info('./after_first_filter/feature_point_1/region_3 has already exited')
        else:
            os.system('mkdir ./after_first_filter/feature_point_1/region_3')

        if os.path.exists('./after_first_filter/feature_point_1/region_4'):
            logging.info('./after_first_filter/feature_point_1/region_4 has already exited')
        else:
            os.system('mkdir ./after_first_filter/feature_point_1/region_4')


        # split work of feature pt 0
        for txt_name in glob('./after_first_filter/feature_point_0/*.txt'):
            # read the 1st line of each txt file and obtain the x and y coordinations
            # filter them by a if loop and flow it to the corresponing folder

            f1 = open(txt_name, "r")
            line = f1.readline()
            # print(line)    # testing
            # number = [int(temp)for temp in line.split() if temp.isdigit()]
            number = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
            # print(number)    # testing
            x_corr = float(number[0])
            y_corr = float(number[1])
            # first region
            if x_corr >= self.half_size_c and y_corr < self.half_size_r:
                shutil.move(txt_name,'./after_first_filter/feature_point_0/region_1')     
            
            # second region
            if x_corr < self.half_size_c and y_corr < self.half_size_r:
                shutil.move(txt_name,'./after_first_filter/feature_point_0/region_2')  

            # third region
            if x_corr < self.half_size_c and y_corr >= self.half_size_r:
                shutil.move(txt_name,'./after_first_filter/feature_point_0/region_3')  

            # fourth region
            if x_corr >= self.half_size_c and y_corr >= self.half_size_r:
                shutil.move(txt_name,'./after_first_filter/feature_point_0/region_4')          
        
        # split work of feature pt 1
        for txt_name in glob('./after_first_filter/feature_point_1/*.txt'):
            # read the 1st line of each txt file and obtain the x and y coordinations
            # filter them by a if loop and flow it to the corresponing folder

            f1 = open(txt_name, "r")
            line = f1.readline()
            # print(line)    # testing
            # number = [int(temp)for temp in line.split() if temp.isdigit()]
            number = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
            # print(number)    # testing
            x_corr = float(number[0])
            y_corr = float(number[1])
            # first region
            if x_corr >= self.half_size_c and y_corr < self.half_size_r:
                shutil.move(txt_name,'./after_first_filter/feature_point_1/region_1')     
            
            # second region
            if x_corr < self.half_size_c and y_corr < self.half_size_r:
                shutil.move(txt_name,'./after_first_filter/feature_point_1/region_2')  

            # third region
            if x_corr < self.half_size_c and y_corr >= self.half_size_r:
                shutil.move(txt_name,'./after_first_filter/feature_point_1/region_3')  

            # fourth region
            if x_corr >= self.half_size_c and y_corr >= self.half_size_r:
                shutil.move(txt_name,'./after_first_filter/feature_point_1/region_4')    

        logging.info('data_split is done')     

#=============
job = region_split()
job.second_region()
job.data_split()