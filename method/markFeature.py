import cv2


class markFeatures:
    def __init__(self,img):
        self.green_color = (0,255,0)
        self.img = cv2.imread(img)
    def plot(self):
        print('plot begins')


class plot_scale(markFeatures):

    def __init__(self,img,output_name):
        super(plot_scale,self).__init__(img)
        self.scaleLine_width = 1
        self.text_x = 'X(+ve)'
        self.text_y = 'Y(+ve)'
        self.output = output_name

    def plot(self):
        # print(self.green_color,self.point_radius,self.img)
        cv2.line(self.img,(50,50),(50,100),self.green_color,self.scaleLine_width)
        cv2.line(self.img,(50,50),(100,50),self.green_color,self.scaleLine_width)
        cv2.line(self.img,(100,50),(90,40),self.green_color,self.scaleLine_width)
        cv2.line(self.img,(100,50),(90,60),self.green_color,self.scaleLine_width)
        cv2.line(self.img,(50,100),(40,90),self.green_color,self.scaleLine_width)
        cv2.line(self.img,(50,100),(60,90),self.green_color,self.scaleLine_width)
        cv2.putText(self.img, self.text_y, (20, 115), cv2.FONT_HERSHEY_PLAIN,1, self.green_color, 1, cv2.LINE_AA)
        cv2.putText(self.img, self.text_x, (105, 55), cv2.FONT_HERSHEY_PLAIN,1, self.green_color, 1, cv2.LINE_AA)

        #cv2.imshow('TT',self.img)
        print(type(self.img))
        cv2.imwrite(self.output, self.img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        


class plot_featurePoints(markFeatures):
    def __init__(self,img,x_center,y_center,text):
        super(plot_featurePoints,self).__init__(img)
        self.x_center = x_center
        self.y_center = y_center
        self.point_radius = 2
        self.text = '#'+str(text)+'('+str(x_center)+','+str(y_center)+')'
        self.path_img = img

    def plot(self):
        cv2.circle(self.img,(self.x_center, self.y_center),self.point_radius,self.green_color, -1)
        cv2.putText(self.img, self.text, (self.x_center+5, self.y_center+5), cv2.FONT_HERSHEY_PLAIN,1, self.green_color, 1, cv2.LINE_AA)
        
        #cv2.imshow('test',self.img)
        cv2.imwrite(self.path_img, self.img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        



        

# ==========================================
# a=plot_scale('img.bmp')
# a.plot()
# b=plot_featurePoints('output.bmp',int(400.45),int(400.555),30000)
# b.plot()