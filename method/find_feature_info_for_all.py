import glob
import logging
import math
from operator import index
import re
import os

import method.plot

'''in the following, there are the work FOR EACH ONE FEATURE POINT
And the number of frame equals to the max.-line'''

def run(file_glob,switch,img_col):
    try:
        
        file_glob = str(file_glob).replace('\\','/')

        if switch == 0:
            logging.info('Case 0')
            file_glob2 = file_glob+'/*.txt'

        if switch == 1:
            logging.info('Case 1')
            file_glob2 = file_glob+'/*.txt'

        # create folder for saving displace per frame
        if os.path.exists('./displacementPerFrame'):
            logging.info('./displacementPerFrame has already exited')
        else:
            os.mkdir('./displacementPerFrame')
            logging.info('./displacementPerFrame is created')

        for txt_name in glob.glob(file_glob2):

            list_x = []
            list_y = []


            list_displacement = []
            list_radius = []
            list_txt_name = []

            f_determ = open(txt_name)
            f_lines_num = f_determ.readlines()
            logging.info('the length of '+str(txt_name)+': '+str(len(f_lines_num)))

            # This method imports the txt files of ALL FEATURE POINTS
            # but only consider FEATURE POINT  which contains the identical frame number with max.-line

            
            # logging.info('the txt file with full frame: '+str(txt_name)) # disable in for_all

            with open(txt_name, "r") as f1:
                for line in f1.readlines():
                    # print(line)    # testing
                    # number = [int(temp)for temp in line.split() if temp.isdigit()]
                    number = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                    # print(number)    # testing
                    list_x.append(float(number[0]))    # format:float
                    # ↓ Counting from the bottom (img_col - feature_col)
                    list_y.append(float(img_col)-float(number[1]))    # *(-1) format:float (圖像y軸跟正常y軸倒置，所以*-1, 去反轉)

            # Getting the FIRST frame of THIS feature point     
            x_1st = list_x[0]
            y_1st = list_y[0]

            list_radius.append(getRadius(list_x,list_y))
            list_txt_name.append(txt_name)

            # all in value of coordinates
            # Getting the MAX DISPLACEMENT IN X-DIRECTION
            x_max = max(list_x)
            # Getting the INEDX OF MAX DISPLACEMENT IN X-DIRECTION
            x_max_index = list_x.index(x_max)
            # Getting the MIN DISPLACEMENT IN X-DIRECTION
            x_min = min(list_x)
            # Getting the INEDX OF MIN DISPLACEMENT IN X-DIRECTION
            x_min_index = list_x.index(x_min)

            # all in value of coordinates
            # Getting the MAX DISPLACEMENT IN Y-DIRECTION
            y_max = max(list_y)
            # Getting the INEDX OF MAX DISPLACEMENT IN Y-DIRECTION
            y_max_index = list_y.index(y_max)
            # Getting the MIN DISPLACEMENT IN Y-DIRECTION
            y_min = min(list_y)
            # Getting the INEDX OF MIN DISPLACEMENT IN Y-DIRECTION
            y_min_index = list_y.index(y_min)

            # Data logging
            logging.info('Total lenght of [X,Y]: '+str(len(list_x))+'\t'+str(len(list_y)))
            logging.info('1st frame [X,Y]: '+str(x_1st)+'\t'+str(y_1st))
            logging.info('X_max. [ DISPLACEMENT | INDEX ]: '+str(x_max)+'\t'+str(x_max_index))
            logging.info('X_min. [ DISPLACEMENT | INDEX ]: '+str(x_min)+'\t'+str(x_min_index))
            logging.info('Y_max. [ DISPLACEMENT | INDEX ]: '+str(y_max)+'\t'+str(y_max_index))
            logging.info('Y_min. [ DISPLACEMENT | INDEX ]: '+str(y_min)+'\t'+str(y_min_index))
            logging.info('===================================================================')

            
            list_diff_x = []
            list_diff_y = []


            for term in range (0,len(list_x)):


                # When compare with the 1ST FRAME
                diff_x = list_x[term]-list_x[0]
                diff_y = list_y[term]-list_y[0]
                list_diff_x.append(diff_x)
                list_diff_y.append(diff_y)


                c_square = math.pow(diff_x,2)+math.pow(diff_y,2)
                c = math.pow(c_square,0.5)
                list_displacement.append(c)
            
            # add here
            text_for_all = txt_name.replace('\\','/')
            for_displacement_frame_graph(file_glob,text_for_all,list_displacement)

            index_middfp = findMiddleFP(list_displacement)

            # del list_displacement[0]    # no use , the min must be index = 1
            logging.info('disp_1st(check): '+str(list_displacement[0]))
            logging.info('disp_max: '+str(max(list_displacement)))
            logging.info('disp_max_index: '+str(list_displacement.index(max(list_displacement))))
            logging.info('disp_min: '+str(min(list_displacement)))
            logging.info('disp_min_index: '+str(list_displacement.index(min(list_displacement))))
            
            
            frame_max_displacement = list_displacement.index(max(list_displacement))

            # Creating the folder for graph
            if os.path.exists('./graph') != True:
                os.mkdir('./graph')
                logging.info('mkdir ./graph')
            else:
                logging.info('path has already exit ./graph')

            # Graph name of each feature pt with max.-line
            graph_name = txt_name.replace('\\','/')
            graph_name = graph_name.replace('.txt','')
            graph_name = graph_name.replace(str(file_glob),'')
            logging.info('Graph name: '+graph_name)
            
            # Plotting graph
            method.plot.plot(list_diff_x,list_diff_y,graph_name,frame_max_displacement,index_middfp)
        
        minpt=list_radius.index(min(list_radius)) # index of feature point
        minpt_txt_name = list_txt_name[minpt]
        logging.info('final center fp: '+str(minpt_txt_name))
                
    
    except Exception as e:
        logging.error(e)




# Sub-method
def getRadius(lx,ly):
    xmin = min(lx)
    ymin = min(ly)
    xmax= max(lx)
    ymax = max(ly)
    xdiff = xmax-xmin # value only
    ydiff = ymax-ymin # value only
    sqxdiff = xdiff*xdiff
    sqydiff = ydiff*ydiff
    range_value = math.sqrt(sqxdiff)+math.sqrt(sqydiff)
    return range_value # float




# Sub-method
def findMiddleFP(list_a):
    
    list_sum = sum(list_a)
    logging.info('displacement sum: '+str(list_sum))
    ans = list_sum/(len(list_a))
    logging.info('avg displacement: '+str(ans))

    diff2 = 99999
    index_num = 0

    for k in range (len(list_a)):
        
        if list_a[k] > ans:
            diff = list_a[k]-ans
        if list_a[k] < ans:
            diff = ans - list_a[k]
        if list_a[k] == ans:
            index_num = k
            break
        if diff < diff2:
            diff2 = diff
            index_num = k
    
    logging.info('middle index_num : '+str(index_num))

    return index_num

def for_displacement_frame_graph(folder_path,txt_path,list_displacement):
    

    
    new_txt_name = str(txt_path).replace(folder_path,'')
    print(new_txt_name)
    new_txt_name = 'dPF_'+new_txt_name
    print(new_txt_name)
    new_txt_path = './displacementPerFrame/'+new_txt_name
    print(new_txt_path)
    
    # create and insert 
    with open(new_txt_path, 'a') as f:
        for i in range (len(list_displacement)):
            f.write(str(list_displacement[i])+'\n')
