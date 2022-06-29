#encoding:utf-8
'''
Lucas-Kanade tracker
====================
Lucas-Kanade sparse optical flow demo. Uses goodFeaturesToTrack
for track initialization and back-tracking for match verification
between frames.
Usage
-----
lk_track.py [<video_source>]
Keys
----
ESC - exit
'''
 
import logging
from matplotlib.font_manager import list_fonts
import numpy as np
import cv2
# import shutil
# import datetime
from time import clock
import os



 
lk_params = dict( winSize  = (15, 15), 
                  maxLevel = 2, 
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))    
 
feature_params = dict( maxCorners = 500, 
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
 
class App:
    def __init__(self, video_src,switch):#构造方法，初始化一些参数和视频路径
        try:
            logging.info('START')
            self.track_len = 10
            self.detect_interval = 5    # 抓取幀數間隔
            self.tracks = []
            self.cam = cv2.VideoCapture(video_src)
            self.frame_idx = 0
            self.frame_total = int(self.cam.get(cv2.CAP_PROP_FRAME_COUNT))
            self.video_width = int(self.cam.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.video_height = int(self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.list_tr = []
            self.video_src = str(video_src)
            self.switch = int(switch)
            self.list_global=[]
            self.list_global_rec=[]
        except Exception as e:
            logging.info(e)
 
    def run(self):#光流运行方法
        try:
            logging.info('START')
            print('start...')

            while True:
                ret, frame = self.cam.read()#读取视频帧
                if ret == True:
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#转化为灰度虚图像
                    vis = frame.copy()
        
                    #print(self.tracks)
                    if len(self.tracks) > 0:#检测到角点后进行光流跟踪
                        #print(self.tracks)
                        img0, img1 = self.prev_gray, frame_gray
                        p0 = np.float32([tr[-1] for tr in self.tracks]).reshape(-1, 1, 2)
                        
                        p1, st, err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)#前一帧的角点和当前帧的图像作为输入来得到角点在当前帧的位置
                        p0r, st, err = cv2.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)#当前帧跟踪到的角点及图像和前一帧的图像作为输入来找到前一帧的角点位置

                        # print('p0 :',p0[0][0],'p1 :',p1[0][0],type(p1[0][0]),'p0r :',p0r[0][0])     # testing
                        # print(p1[0][0][1])     # testing
                        # print(len(p1))


                        d = abs(p0-p0r).reshape(-1, 2).max(-1)#得到角点回溯与前一帧实际角点的位置变化关系
                        good = d < 1 #判断d内的值是否小于1，大于1跟踪被认为是错误的跟踪点
                        new_tracks = []
                        self.list_tr.clear()
                        for tr, (x, y), good_flag in zip(self.tracks, p1.reshape(-1, 2), good):#将跟踪正确的点列入成功跟踪点
                            if not good_flag:
                                continue
                            tr.append((x, y))
                            # if len(tr) > self.track_len:    # testing
                            #     del tr[0]    # testing
                            new_tracks.append(tr)
                            cv2.circle(vis, (int(x), int(y)), 2, (0, 255, 0), -1)
                            
                            self.list_tr.append(tr)
                            # self.list_global.append()
                            # print(self.list_tr)    # testing 20220608
                        # logging.info('RUN END')
                        #print(self.list_tr)    # testing 20220608
                        self.tracks = new_tracks
                        cv2.polylines(vis, [np.int32(tr) for tr in self.tracks], False, (0, 255, 0))#以上一振角点为初始点，当前帧跟踪到的点为终点划线
                        
                        # # track count    # testing
                        # draw_str(vis, (20, 20), 'track count: %d' % len(self.tracks))

                        # cv2.imwrite(datetime.datetime.now().strftime("%A_%d_%B_%Y_%I_%M_%S%p")+'.png',vis)    # testing
                        #print(self.frame_idx)

                    if self.frame_idx % self.detect_interval == 0:#每5帧检测一次特征点
                        mask = np.zeros_like(frame_gray)#初始化和视频大小相同的图像
                        mask[:] = 255#将mask赋值255也就是算全部图像的角点
                        for x, y in [np.int32(tr[-1]) for tr in self.tracks]:#跟踪的角点画圆
                            cv2.circle(mask, (x, y), 5, 0, -1)
                        p = cv2.goodFeaturesToTrack(frame_gray, mask = mask, **feature_params)#像素级别角点检测
                        if p is not None:
                            for x, y in np.float32(p).reshape(-1, 2):
                                self.tracks.append([(x, y)])#将检测到的角点放在待跟踪序列中

                                # print(len(self.tracks))    # testing
                                # print(self.tracks)    # testing

                    #print('TRACKS:')
                    #print( self.tracks)

                    if len(self.tracks)>0:
                        for jkl in range (len(self.tracks)):
                            if self.list_global_rec.count(self.tracks[jkl][0]) == 0:
                                frame_num_global = (self.tracks[jkl][0][0],self.tracks[jkl][0][1],self.frame_idx)
                                
                                self.list_global.append(frame_num_global)
                                self.list_global_rec.append(self.tracks[jkl][0])

                    #print(self.list_global) #testing
                    # print('FRAME IDX:',self.frame_idx) # testing only
                    self.frame_idx += 1
                    self.prev_gray = frame_gray

                    # cv2.imshow('lk_track', vis)
                    
                    # create video
                    # self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')#设置保存图片格式
                    # self.out = cv2.VideoWriter(datetime.datetime.now().strftime("%A_%d_%B_%Y_%I_%M_%S%p")+'.mp4',self.fourcc, 10.0, (self.video_width,self.video_height))#分辨率要和原视频对应
                    # self.out.write(vis)

                # ch = 0xFF & cv2.waitKey(1)
                if self.frame_idx == self.frame_total:
                    break
            
            # print(self.list_tr)    # print th whole data base
            logging.info('the length of feature points on a frame: '+str(len(self.list_tr)))    # print the length of feature points
            # print(self.list_tr[100])    # testing
            
            # Creating folders
            if os.path.exists('./feature_point_0') != True:
                os.mkdir('./feature_point_0')
                logging.info('mkdir ./feature_point_0')
            else:
                logging.info('path already exited: ./feature_point_0')

            if os.path.exists('./feature_point_1') != True:
                os.mkdir('./feature_point_1')
                logging.info('mkdir ./feature_point_1')
            else:
                logging.info('path already exited: ./feature_point_1')


            range_feature_pts = range(0,len(self.list_tr))
            for feature_pt_num in range_feature_pts:
                range_term_num = range(0,len(self.list_tr[feature_pt_num]))

                if self.switch == 0:
                    txt_name = str(feature_pt_num)+'_0_th.txt'

                if self.switch == 1:
                    txt_name = str(feature_pt_num)+'_1_th.txt'

                with open(txt_name, "w", encoding="utf-8") as f2:
                    for term_num in range_term_num:
                        # self.list_tr[feature_pt_num][term_num][0]    # x-coordinate
                        # self.list_tr[feature_pt_num][term_num][1]    # y-coordinate
                        line = str(term_num)+'_th_frame [x,y]/[c,r]'+"\t"+str(self.list_tr[feature_pt_num][term_num][0])+"\t"+str(self.list_tr[feature_pt_num][term_num][1])+"\n"
                        f2.write(line)

            if self.switch == 0:
                global_txt_name = './global_frame_number_0.txt'
            if self.switch == 1:
                global_txt_name = './global_frame_number_1.txt'


            global_term_num=range(len(self.list_global))
            with open(global_txt_name, "w", encoding="utf-8") as f3:
                for g_term_num in global_term_num:

                    # ↓ x,y,global frame number
                    f3_line = str(self.list_global[g_term_num][0])+"\t"+str(self.list_global[g_term_num][1])+"\t"+str(self.list_global[g_term_num][2])+"\n"
                    
                    f3.write(f3_line)


            
        except Exception as e:
            logging.error(e)



# def main():
#     import sys
#     try: video_src = sys.argv[1]
#     except: video_src = "20210930CON008_1.avi"
 
#     print (__doc__)
#     App(video_src).run()
#     cv2.destroyAllWindows()
 
# if __name__ == '__main__':
#     main()
'''============================================='''
# App('./cam_0.avi',0).run()