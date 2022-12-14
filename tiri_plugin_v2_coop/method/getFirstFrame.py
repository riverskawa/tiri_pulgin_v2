import glob

def cam0():
    list_img=[]
    for img in glob.glob('./temp_img_0/*_0.bmp'):
        img = str(img).replace('\\','/')
        img= img.replace('./temp_img_0/','')
        img=img.replace('C_0.bmp','')
        list_img.append(img)

    list_img.sort()
    img_name_1st = './temp_img_0/'+str(list_img[0])+'C_0.bmp'
    return img_name_1st


def cam1():
    list_img2=[]
    for img in glob.glob('./temp_img_1/*_1.bmp'):
        img = str(img).replace('\\','/')
        img= img.replace('./temp_img_1/','')
        img=img.replace('C_1.bmp','')
        list_img2.append(img)

    list_img2.sort()
    img_name_1st2 = './temp_img_1/'+str(list_img2[0])+'C_1.bmp'
    return img_name_1st2