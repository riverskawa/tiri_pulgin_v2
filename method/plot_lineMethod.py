
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import logging
import glob
import re
import math

def plot(glob_src,path_target_folder,switch):
    try:

        for source in glob.glob(glob_src):
            plt.switch_backend('agg')

        
            # New two lists called xpt and ypt
            xpt = []
            ypt = []

            source = str(source).replace('\\','/')
            with open(source) as f1:
                for line in f1.readlines():
                    coor = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                    diff=math.sqrt(float(coor[0])*float(coor[0])+float(coor[1])*float(coor[1]))
                    ypt.append(diff)

            for i in range (0,len(ypt)):
                xpt.append(i)
            
            print(len(xpt)) # testing 
            print(len(ypt)) # testing 


            fig = plt.gcf() 
            plt.xlabel('Frame Number')
            plt.ylabel('Distance of Two Points (Pixel)')
            plt.grid()

            # x and y axis setting
            ax=plt.gca()  #gca:get current axis得到当前轴
            #设置图片的右边框和上边框为不显示
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            #挪动x，y轴的位置，也就是图片下边框和左边框的位置
            ax.spines['bottom'].set_position(('data',0))  #data表示通过值来设置x轴的位置，将x轴绑定在y=0的位置
            ax.spines['left'].set_position(('data',0))  #axes表示以百分比的形式设置轴的位置，即将y轴绑定在x轴50%的位置，也就是x轴的中点



            plt.scatter(xpt,ypt,marker="o",s=5, c='green')    

            # highlight the customized point
            # for th_i in range (len(xpt)):
            #     if th_i == index_mfp:
            #         frame_th = str(th_i)+'_th_frame'
            #         ax.text(xpt[th_i]+4, ypt[th_i]*1.01, frame_th,
            #             fontsize = 10 ,color = "r", style = "italic", weight = "light",
            #             verticalalignment='center', horizontalalignment='right',rotation=0)

            if max(xpt)>=max(ypt):
                range_max = max(xpt)
            else:
                range_max = max(ypt)
            
            if min(xpt)>=min(ypt):
                range_min = min(ypt)
            else:
                range_min= min(xpt)
            if range_min > 0:
                range_min = 0

            plt.xlim(range_min-10,range_max+10)   # when using xlim, but gap does not looks equal
            plt.ylim(range_min-10,range_max+10)   # when using ylim, but gap does not looks equal
            # plt.xticks(range(range_min-10,range_max+10,5)) # i dont remember wtf is this
            # plt.yticks(range(range_min-10,range_max+10,5)) # i dont remember wtf is this
            # plt.scatter(xpt[idx_middfp],ypt[idx_middfp],marker="o",s=10,c='blue')    # middle feature point, also the new origin
            # plt.scatter(xpt[0],ypt[0],marker="o",s=10,c='red')    # the first feature point, the old (0,0)
            # plt.scatter(xpt[index_mfp],ypt[index_mfp],marker="o",s=10,c='yellow')    # max feature point

            xpt.clear()
            ypt.clear()

            if switch == 0:
                output_graph_name = source.replace('./pt_diff_0/','')
                output_graph_name = output_graph_name.replace('.txt','')
            if switch == 1:
                output_graph_name = source.replace('./pt_diff_1/','')
                output_graph_name = output_graph_name.replace('.txt','')

            save_name = path_target_folder+'/'+output_graph_name+'.png'
            # plt.show()

            fig.savefig(save_name)
            plt.close()

            with Image.open(save_name) as image:
                w,h=image.size
                if w>=h:
                    image = image.resize((w, w))
                else:
                    image = image.resize((h, h))
                image.save(save_name)

    except Exception as e:
        logging.error(e)

#===============================================
# xx=[34,4,45,67,-33,-22]
# yy=[2,5,7,9,5,-23]
# plot(xx,yy,'testing','./',3)
# with Image.open('testing.png') as image:
#     w,h=image.size
#     if w>=h:
#         image = image.resize((int(w*1.5), int(w*1.5)))
#     else:
#         image = image.resize((int(h*1.5), int(h*1.5)))
#     image.save("testing.png")



#=======================================================
# plot('./pt_diff_0/*_th.txt','./20220622testdel',0)