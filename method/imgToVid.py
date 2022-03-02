import cv2
import glob
import logging
 
 
def cam0():
    try:
        logging.info('START')
        list_img=[]
        for img in glob.glob('./temp_img_0/*_0.bmp'):
            img = str(img).replace('\\','/')
            img= img.replace('./temp_img_0/','')
            img=img.replace('C_0.bmp','')
            list_img.append(img)
        
        list_img.sort()

        img_array = []
        for j in range(len(list_img)):
            filename = './temp_img_0/'+str(list_img[j])+'C_0.bmp'
            img_to_go = cv2.imread(filename)
            height, width, layers = img_to_go.shape
            size = (width,height)
            img_array.append(img_to_go)
        


        out = cv2.VideoWriter('cam_0.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
        
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
    except Exception as e:
        logging.error(e)


def cam1():
    try:
        logging.info('START')
        list_img=[]
        for img in glob.glob('./temp_img_1/*_1.bmp'):
            img = str(img).replace('\\','/')
            img= img.replace('./temp_img_1/','')
            img=img.replace('C_1.bmp','')
            list_img.append(img)
        
        list_img.sort()

        img_array = []
        for j in range(len(list_img)):
            filename = './temp_img_1/'+str(list_img[j])+'C_1.bmp'
            img_to_go = cv2.imread(filename)
            height, width, layers = img_to_go.shape
            size = (width,height)
            img_array.append(img_to_go)
        


        out = cv2.VideoWriter('cam_1.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
        
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
    except Exception as e:
        logging.error(e)

#=======
# cam0()
# cam1()