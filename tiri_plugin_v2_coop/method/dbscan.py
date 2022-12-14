from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
import re
import glob
import logging


def run(switch,max_lines):
    plt.switch_backend('agg')
    if switch == 0:
        folder_path ='./feature_point_0/*.txt'
    if switch == 1:
        folder_path ='./feature_point_1/*.txt'

    for txt_path in glob.glob(folder_path):
        
        i2 = str(txt_path).replace('\\','/')

        f_determ = open(i2)
        f_lines_num = f_determ.readlines()
        logging.info('the length of '+str(i2)+': '+str(len(f_lines_num)))

        if len(f_lines_num) == max_lines:
            X =[]
            with open(i2, "r") as f1:
                for line in f1.readlines():
                    # print(line)    # testing
                    # number = [int(temp)for temp in line.split() if temp.isdigit()]
                    number = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                    # print(number)    # testing
                    X.append([float(number[0]),float(630)-float(number[1])])    # format:float  # *(-1) format:float (圖像y軸跟正常y軸倒置，所以*-1, 去反轉)

            logging.info('type of original data: '+str(type(X))) # for test

            # Convert array to np-array
            XX = np.array(X)
            logging.info('type of data after convert: '+str(XX.shape))

            # Setting of DB scan --> eps(radius) and min_samples
            clustering = DBSCAN(eps=0.8, min_samples=8).fit(XX)

            logging.info('type of clustering.labels: '+str(type(clustering.labels_)))

            logging.info('length of clustering.labels: '+str(len(clustering.labels_)))

            logging.info('clustering.labels: ')
            logging.info(clustering.labels_) # For testing

            # print(clustering) # For testing

            fig = plt.gcf()
            plt.scatter(XX[:,0],XX[:,1],c=clustering.labels_)

            if switch == 0:
                i3 = i2.replace('./feature_point_0/','')
                i3 = i3.replace('.txt','')
            if switch == 1:
                i3 = i2.replace('./feature_point_1/','')
                i3 = i3.replace('.txt','')

            save_name = './dbscan_output/'+'dbscan_'+i3+'png'
            # plt.show() # for test
            fig.savefig(save_name)
            plt.close()

'''------------------------------'''
# run(0,709)
# run(1,709)