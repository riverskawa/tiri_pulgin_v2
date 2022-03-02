
from distutils.command.config import config
import os
import tkinter as tk
from tkinter import Frame, filedialog
from tkinter.constants import END, GROOVE, SUNKEN
import tkinter.font as tkFont
from tkinter import ttk
import threading
import time
from turtle import width
import cv2
from matplotlib.pyplot import text
from numpy import pad
from pyparsing import col





import interface.interface
import method.initialization


root = tk.Tk()
root.title('[No Job] TIRI_000')
#root.attributes('-fullscreen',True)
# root.state('zoomed')
root.geometry("1500x800+210+0")
root.minsize(1500,800)
# root.maxsize(1500,800)


class mainpage(object):
    def __init__(self,master = None,*args):
        self.root = master

        # clear initialize the root folder
        method.initialization.run()

        self.filemenu = tk.Menu(self.root)
        self.root.config(menu=self.filemenu)
        self.menu1 = tk.Menu(self.filemenu)


        self.cav1 = tk.Canvas(self.root,state=tk.DISABLED)
        self.cav1.place(relx=0,rely=0,relwidth=1,relheight=0.9)
        self.notebook = ttk.Notebook(self.cav1)
        self.notebook.place(relx=0.005,rely=0.05,relwidth=0.78,relheight=0.98)
        self.nb_frame1 = tk.Frame(self.notebook,)
        # self.nb_frame2 = tk.Frame(self.notebook,bg='red')
        self.nb_frame1.pack(fill='both',expand=1)
        # self.nb_frame2.pack(fill='both',expand=1)
        self.notebook.add(self.nb_frame1,text='Area Select')
        # self.notebook.add(self.nb_frame2,text='page2')

        #font style
        self.fontStyle = tkFont.Font(family="Terminal", size=10)
        self.fontStyle_run = tkFont.Font(family="Terminal", size=15)

        self.cav1_2 = tk.Canvas(self.cav1,bg='white',bd=3,relief=GROOVE,background="white")
        self.cav1_2.place(relx=0.785,rely=0.05,relwidth=0.21,relheight=0.98)


        self.menu1.add_command(label='create a new project',command=self.new_proj)
        self.menu1.add_command(label='open a project')
        self.menu1.add_command(label='exit',command=root.quit)


        self.filemenu.add_cascade(label='File',menu=self.menu1)
        self.filemenu.add_cascade(label='Reference')


        self.img_cav_test = tk.PhotoImage(file='./demo2.png')
        self.cav1_1 = tk.Canvas(self.nb_frame1,width=700,height=700)
        self.cav1_right = tk.Canvas(self.nb_frame1,width=700,height=700)
        self.cav1_bottom = tk.Canvas(self.nb_frame1,width=1450,height=60,bg="white")


        self.cav1_1.create_image(0, 0, anchor='nw', image=self.img_cav_test)
        self.cav1_1.grid(row=0,column=0,rowspan=1,columnspan=1,padx=20)
        # self.cav1_1.pack(fill='both',expand=1)

        self.cav1_right.create_image(0, 0, anchor='nw', image=self.img_cav_test)
        self.cav1_right.grid(row=0,column=1,rowspan=1,columnspan=1,padx=20)

        self.cav1_bottom.grid(row=1,column=0,columnspan=2,padx=20,pady=15)


        self.cav1_1.bind('<Button-1>', self.onLeftButtonDown)
        self.cav1_1.bind('<B1-Motion>', self.onLeftButtonMove) # 按下左鍵
        self.cav1_1.bind('<ButtonRelease-1>', self.onLeftButtonUp) 

        self.cav1_right.bind('<Button-1>', self.onLeftButtonDown_right)
        self.cav1_right.bind('<B1-Motion>', self.onLeftButtonMove_right) # 按下左鍵
        self.cav1_right.bind('<ButtonRelease-1>', self.onLeftButtonUp_right) 

        self.label_left_selec_TL = tk.Label(self.cav1_bottom,text=u'Left (Top Left Corner (c,r):',font=self.fontStyle)
        self.label_left_selec_BR = tk.Label(self.cav1_bottom,text=u'Left (Bottom Right Corner (c,r):',font=self.fontStyle)
        self.entry_left_selec_TL = tk.Entry(self.cav1_bottom)
        self.entry_left_selec_BR = tk.Entry(self.cav1_bottom)
        self.label_right_selec_TL = tk.Label(self.cav1_bottom,text=u'Right (Top Left Corner (c,r):',font=self.fontStyle)
        self.label_right_selec_BR = tk.Label(self.cav1_bottom,text=u'Right (Bottom Right Corner (c,r):',font=self.fontStyle)
        self.entry_right_selec_TL = tk.Entry(self.cav1_bottom)
        self.entry_right_selec_BR = tk.Entry(self.cav1_bottom)
        self.btn_selec_confirm = tk.Button(self.cav1_bottom,text=u'Confirm',font=self.fontStyle_run)
        self.label_left_selec_TL.grid(row=0,column=0,rowspan=1,columnspan=1,padx=5,pady=5,sticky="w")
        self.label_left_selec_BR.grid(row=1,column=0,rowspan=1,columnspan=1,padx=5,pady=5,sticky="w")
        self.entry_left_selec_TL.grid(row=0,column=1,rowspan=1,columnspan=1,padx=5,pady=5,sticky="w")
        self.entry_left_selec_BR.grid(row=1,column=1,rowspan=1,columnspan=1,padx=5,pady=5,sticky="w")
        self.label_right_selec_TL.grid(row=0,column=2,rowspan=1,columnspan=1,padx=5,pady=5,sticky="w")
        self.label_right_selec_BR.grid(row=1,column=2,rowspan=1,columnspan=1,padx=5,pady=5,sticky="w")
        self.entry_right_selec_TL.grid(row=0,column=3,rowspan=1,columnspan=1,padx=5,pady=5,sticky="w")
        self.entry_right_selec_BR.grid(row=1,column=3,rowspan=1,columnspan=1,padx=5,pady=5,sticky="w")
        self.btn_selec_confirm.grid(row=0,column=4,rowspan=2,columnspan=1,padx=5,pady=5,sticky="w")

        # self.label2 = tk.Label(self.cav1_1,text=u'canvas 1_1')
        # self.label2.place(x=10,y=10)

        # image import to use 
        self.img_menu = tk.PhotoImage(file='./ui/menu.png')

        # value of radio button 
        self.rdio_calib_value = tk.IntVar()
        self.rdio_skip_value = tk.IntVar()
        self.X = tk.IntVar(value=0)
        self.Y = tk.IntVar(value=0)
        self.X_right= tk.IntVar(value=0)
        self.Y_right= tk.IntVar(value=0)

        # mouse up and down
        self.sel = False
        self.sel_right = False
        
        self.lastDraw = None
        self.lastDraw_right = None

        # on off signal
        self.first_confirm_btn = 0
        self.second_confirm_btn = 0
        self.third_confirm_btn = 0

        self.label_menu = tk.Label(self.cav1_2,image=self.img_menu,)
        self.sep = tk.Label(self.cav1_2,image=self.sep_img)

        # progress bar style
        self.s = ttk.Style()
        self.s.theme_use('clam')
        self.s.configure("orange.Horizontal.TProgressbar", foreground='orange', background='orange')

        self.label_cam_cali = tk.Label(self.cav1_2,text=u'Camera  Calibration : ',font=self.fontStyle,fg='orange')
        self.rdio_run_calib = tk.Radiobutton(self.cav1_2, text=u'Import',variable=self.rdio_calib_value, value= 1,font=self.fontStyle,fg='orange',command=self.activeImporCaliImage)
        self.rdio_skip_calib = tk.Radiobutton(self.cav1_2,text=u'Skip',variable=self.rdio_calib_value,value= 0,font=self.fontStyle,fg='orange',command=self.activeImporCaliImage)
        self.btn_import_cali_img = tk.Button(self.cav1_2,text=u' Import ... ',font=self.fontStyle,fg='orange',state=tk.DISABLED,command=self.fileImportCali)
        # self.combo_cali_slip = ttk.Combobox(self.cav1_2,values=["Last one","import"],state=tk.DISABLED)
        self.label_path_cali_img = tk.Label(self.cav1_2,text=u'Path : ',font=self.fontStyle,fg='orange',state=tk.DISABLED)
        self.entry_calib_path = tk.Entry(self.cav1_2,bg='AntiqueWhite1',state=tk.DISABLED)
        self.btn_path_comfirm_cail = tk.Button(self.cav1_2,text=u' Confirm ',font=self.fontStyle,fg='orange',state=tk.DISABLED,command=self.comfirImporCalib)
        self.label_cali_opt = tk.Label(self.cav1_2,text=u'Calibration Option : ',font=self.fontStyle,fg='orange',state=tk.DISABLED)
        self.rdio_skip_priv = tk.Radiobutton(self.cav1_2, text=u' Previous ',variable=self.rdio_skip_value, value= 0,font=self.fontStyle,fg='orange',state=tk.DISABLED,command=self.activateSkipPathCaliImg)
        self.rdio_skip_import = tk.Radiobutton(self.cav1_2,text=u' Import ',variable=self.rdio_skip_value,value= 1,font=self.fontStyle,fg='orange',state=tk.DISABLED,command=self.activateSkipPathCaliImg)
        self.btn_skip_import = tk.Button(self.cav1_2,text=u' Import ... ',font=self.fontStyle,fg='orange',state=tk.DISABLED,command=self.fileImportCaliParam)
        self.label_path_skip_cali_import = tk.Label(self.cav1_2,text=u'Path : ',font=self.fontStyle,fg='orange',state=tk.DISABLED)
        self.entry_skip_cali_import_path = tk.Entry(self.cav1_2,bg='AntiqueWhite1',state=tk.DISABLED)
        self.btn_path_comfirm_skip_cail = tk.Button(self.cav1_2,text=u' Confirm ',font=self.fontStyle,fg='orange',state=tk.DISABLED,command=self.comfirSkipImporCalib)
        self.label_img_correction = tk.Label(self.cav1_2,text=u'Image  Correction : ',font=self.fontStyle,fg='orange')
        self.btn_path_img_corr_import = tk.Button(self.cav1_2,text=u' Import ... ',font=self.fontStyle,fg='orange',command=self.fileImportImgCorr)
        self.label_path_img_corr = tk.Label(self.cav1_2,text=u'Path : ',font=self.fontStyle,fg='orange')
        self.entry_path_img_corr = tk.Entry(self.cav1_2,bg='AntiqueWhite1')
        self.btn_path_path_img_corr = tk.Button(self.cav1_2,text=u' Confirm ',font=self.fontStyle,fg='orange',command=self.comfirImporImgCorr)
        self.btn_run = tk.Button(self.cav1_2,text=u' Run ',font=self.fontStyle_run,fg='orange',command=self.thread_control_run)
        self.progressbar = ttk.Progressbar(self.cav1_2,length=280,style="orange.Horizontal.TProgressbar",mode='indeterminate',maximum=20,value=0,orient=tk.HORIZONTAL)
        # self.progressbar.step(1)


        # reification
        self.label_menu.place(x=20,y=10)
        self.label_cam_cali.place(x=20,y=60)
        self.rdio_run_calib.place(x=20,y=90)
        self.rdio_skip_calib.place(x=150,y=90)
        self.btn_import_cali_img.place(x=20,y=120)
        self.label_path_cali_img.place(x=20,y=150)
        self.entry_calib_path.place(x=80,y=150)
        self.btn_path_comfirm_cail.place(x=220,y=150)
        self.rdio_skip_priv.place(x=20,y=180)
        self.rdio_skip_import.place(x=150,y=180)
        self.btn_skip_import.place(x=20,y=210)
        self.label_path_skip_cali_import.place(x=20,y=240)
        self.entry_skip_cali_import_path.place(x=80,y=240)
        self.btn_path_comfirm_skip_cail.place(x=220,y=240)

        self.label_img_correction.place(x=20,y=290)
        self.btn_path_img_corr_import.place(x=20,y=320)
        self.label_path_img_corr.place(x=20,y=350)
        self.entry_path_img_corr.place(x=80,y=350)
        self.btn_path_path_img_corr.place(x=220,y=350)

        self.btn_run.place(x=238,y=380)

        self.progressbar.place(x=20,y=450)
        
        #------------------------------------------------------------------------------------

    def _from_rgb(self,rgb):
        return "#%02x%02x%02x" % rgb

#---------some btn action(left)--------------------------------------------------------------------------
    def getImgSize(self):
        img=cv2.imread('./demo.png')
        r,c,no_use = img.shape
        return r,c
    
    def onLeftButtonDown(self,event):
        self.X.set(event.x)
        self.Y.set(event.y)
        #開始截圖
        self.sel = True

    def onLeftButtonMove(self,event):
        #鼠標左鍵移動，顯示選取的區域
        if not self.sel:
            return
        try: #刪除剛畫完的圖形，要不然鼠標移動的時候是黑乎乎的一片矩形
            self.cav1_1.delete(self.lastDraw)
        except Exception as e:
            pass
        self.lastDraw = self.cav1_1.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='green')

    def onLeftButtonUp(self,event):
        #獲取鼠標左鍵擡起的位置，保存區域截圖
        self.sel = False

        # # delete the rectangle at the end of selection
        # try:
        #     self.cav1_1.delete(self.lastDraw)
        # except Exception as e:
        #     pass

        time.sleep(0.1)
        #考慮鼠標左鍵從右下方按下而從左上方擡起的截圖
        left, right = sorted([self.X.get(), event.x])
        top, bottom = sorted([self.Y.get(), event.y])
        self.str_left_TL = '[ '+str(left)+', '+str(top)+' ]'
        self.str_left_BR = '[ '+str(right)+', '+str(bottom)+' ]'
        self.entry_left_selec_TL.delete(0,END)
        self.entry_left_selec_TL.insert(0,self.str_left_TL)
        self.entry_left_selec_BR.delete(0,END)
        self.entry_left_selec_BR.insert(0,self.str_left_BR)

#--------------------------------------------------------------------------------------------------------------------

# def getLeftImg(self): # 20220302 stop edit here


#---------some btn action(right)--------------------------------------------------------------------------

    def onLeftButtonDown_right(self,event):
        self.X_right.set(event.x)
        self.Y_right.set(event.y)
        #開始截圖
        self.sel_right = True

    def onLeftButtonMove_right(self,event):
        #鼠標左鍵移動，顯示選取的區域
        if not self.sel_right:
            return
        try: #刪除剛畫完的圖形，要不然鼠標移動的時候是黑乎乎的一片矩形
            self.cav1_right.delete(self.lastDraw_right)
        except Exception as e:
            pass
        self.lastDraw_right = self.cav1_right.create_rectangle(self.X_right.get(), self.Y_right.get(), event.x, event.y, outline='green')

    def onLeftButtonUp_right(self,event):
        #獲取鼠標左鍵擡起的位置，保存區域截圖
        self.sel_right = False

        # # delete the rectangle at the end of selection
        # try:
        #     self.cav1_1.delete(self.lastDraw)
        # except Exception as e:
        #     pass

        time.sleep(0.1)
        #考慮鼠標左鍵從右下方按下而從左上方擡起的截圖
        left, right = sorted([self.X_right.get(), event.x])
        top, bottom = sorted([self.Y_right.get(), event.y])
        self.str_right_TL = '[ '+str(left)+', '+str(top)+' ]'
        self.str_right_BR = '[ '+str(right)+', '+str(bottom)+' ]'
        self.entry_right_selec_TL.delete(0,END)
        self.entry_right_selec_TL.insert(0,self.str_right_TL)
        self.entry_right_selec_BR.delete(0,END)
        self.entry_right_selec_BR.insert(0,self.str_right_BR)

#--------------------------------------------------------------------------------------------------------------------

    def thread_control_run(self):
        # progress bar start
        self.progressbar.start()
        threading.Thread(target=self.run).start()

    def run(self):
        # title change
        root.title('[Calibration Loading] TIRI_000')
        # 
        self.class01=interface.interface.interfaceCalibration()
        # camera calibration import mode
        if self.rdio_calib_value.get() == 1 and self.first_confirm_btn == 1 :
            self.class01.calib(self.entry_calib_path.get())
        
        # camera calibration skip mode
        if self.rdio_calib_value.get() == 0 :
            # skip camera calibration previous mode
            if self.rdio_skip_value.get() == 0:
                self.class01.skipCalib()
            # skip camera calibration import mode
            if self.rdio_skip_value.get() == 1 and self.second_confirm_btn == 1:
                self.class01.skipCalibInput(self.entry_skip_cali_import_path.get())
        
        # image correction

        self.class01.imgProc(self.entry_path_img_corr.get())
        # Converting image to video
        interface.interface.interfaceImgToVid().doTransfer()
        # optical flow
        interface.interface.interfaceOpticalFlow().doOpticalFlow()
        # cal
        self.list_max_frame = interface.interface.interfaceCalulation().doCal()
        # DBScan
        interface.interface.interfaceDBScan().doDBScan(self.list_max_frame[0],self.list_max_frame[1])



    def activateSkipPathCaliImg(self):
        if self.rdio_skip_value.get()==1:   # skip import == 1 
            self.btn_skip_import.config(state=tk.NORMAL)
            self.label_path_skip_cali_import.config(state=tk.NORMAL)
            self.entry_skip_cali_import_path.config(state=tk.NORMAL)
            self.btn_path_comfirm_skip_cail.config(state=tk.NORMAL)
            self.rdio_skip_priv.config(fg='orange')
            self.rdio_skip_import.config(fg='green')

        if self.rdio_skip_value.get()==0:
            self.btn_skip_import.config(state=tk.DISABLED)
            self.label_path_skip_cali_import.config(state=tk.DISABLED)
            self.entry_skip_cali_import_path.config(state=tk.DISABLED)
            self.btn_path_comfirm_skip_cail.config(state=tk.DISABLED)
            self.rdio_skip_priv.config(fg='green')
            self.rdio_skip_import.config(fg='orange')


    def activeImporCaliImage(self):
        if self.rdio_calib_value.get() == 1: # it means import is "on"
            # disable widget
            self.rdio_skip_priv.config(state=tk.DISABLED)
            self.rdio_skip_import.config(state=tk.DISABLED)
            # self.label_path_skip_cali_import.config(state=tk.DISABLED)
            # self.entry_skip_cali_import_path.config(state=tk.DISABLED)
            # self.btn_path_comfirm_skip_cail.config(state=tk.DISABLED)
            # enable widget
            self.btn_import_cali_img.config(state=tk.NORMAL)
            self.label_path_cali_img.config(state=tk.NORMAL)
            self.entry_calib_path.config(state=tk.NORMAL)
            self.btn_path_comfirm_cail.config(state=tk.NORMAL)
            # widget of skip
            self.btn_skip_import.config(state=tk.DISABLED)
            self.label_path_skip_cali_import.config(state=tk.DISABLED)
            self.entry_skip_cali_import_path.config(state=tk.DISABLED)
            self.btn_path_comfirm_skip_cail.config(state=tk.DISABLED)
            self.rdio_run_calib.config(fg='green')
            self.rdio_skip_calib.config(fg='orange')
        
        if self.rdio_calib_value.get() == 0:
            # disable widget
            self.btn_import_cali_img.config(state=tk.DISABLED)
            self.label_path_cali_img.config(state=tk.DISABLED)
            self.entry_calib_path.config(state=tk.DISABLED)
            self.btn_path_comfirm_cail.config(state=tk.DISABLED)
            # enable widget
            self.rdio_skip_priv.config(state=tk.NORMAL)
            self.rdio_skip_import.config(state=tk.NORMAL)
            # self.label_path_skip_cali_import.config(state=tk.NORMAL)
            # self.entry_skip_cali_import_path.config(state=tk.NORMAL)
            # self.btn_path_comfirm_skip_cail.config(state=tk.NORMAL)
            # widget of skip
            self.btn_skip_import.config(state=tk.DISABLED)
            self.label_path_skip_cali_import.config(state=tk.DISABLED)
            self.entry_skip_cali_import_path.config(state=tk.DISABLED)
            self.btn_path_comfirm_skip_cail.config(state=tk.DISABLED)
            self.rdio_run_calib.config(fg='orange')
            self.rdio_skip_calib.config(fg='green')
        

    def fileImportCali(self):
        self.file_path_cali = filedialog.askdirectory(parent=root,initialdir='~/')
        self.entry_calib_path.delete(0,END)
        self.entry_calib_path.insert(0,self.file_path_cali)
        self.btn_import_cali_img.config(fg='orange')
        # # Button is generated
        # self.proc_btn = tk.Button(self.cav1_2,text=u'IMPORT OBJECT IMAGE',command=self.fileImportProc)
        # self.proc_btn.place(x=self.import_btn.winfo_x(),y=self.import_btn.winfo_y()+50,width=180,height=30)
        # root.title('[Calibration Image Imported] TIRI_000')
    
    def fileImportCaliParam(self):
        self.file_path_cali_param = filedialog.askdirectory(parent=root,initialdir='~/')
        self.entry_skip_cali_import_path.delete(0,END)
        self.entry_skip_cali_import_path.insert(0,self.file_path_cali_param)
        self.btn_skip_import.config(fg='orange')

    def fileImportImgCorr(self):
        self.file_path_img_corr = filedialog.askdirectory(parent=root,initialdir='~/')
        self.entry_path_img_corr.delete(0,END)
        self.entry_path_img_corr.insert(0,self.file_path_img_corr)
        self.btn_path_img_corr_import.config(fg='orange')

    def comfirImporCalib(self):
        if self.first_confirm_btn == 0 :
            self.btn_path_comfirm_cail.config(fg='green')
            self.btn_import_cali_img.config(state=tk.DISABLED)
            self.entry_calib_path.config(state=tk.DISABLED)
            self.first_confirm_btn = 1
            return

        if self.first_confirm_btn == 1 :
            self.btn_path_comfirm_cail.config(fg='orange')
            self.btn_import_cali_img.config(state=tk.NORMAL)
            self.entry_calib_path.config(state=tk.NORMAL)
            self.first_confirm_btn = 0
            return

    def comfirSkipImporCalib(self):
        if self.second_confirm_btn == 0 :
            self.btn_path_comfirm_skip_cail.config(fg='green')
            self.btn_skip_import.config(state=tk.DISABLED)
            self.entry_skip_cali_import_path.config(state=tk.DISABLED)
            self.second_confirm_btn = 1
            return

        if self.second_confirm_btn == 1 :
            self.btn_path_comfirm_skip_cail.config(fg='orange')
            self.btn_skip_import.config(state=tk.NORMAL)
            self.entry_skip_cali_import_path.config(state=tk.NORMAL)
            self.second_confirm_btn = 0
            return
    
    def comfirImporImgCorr(self):
        if self.third_confirm_btn == 0 :
            self.btn_path_path_img_corr.config(fg='green')
            self.btn_path_img_corr_import.config(state=tk.DISABLED)
            self.entry_path_img_corr.config(state=tk.DISABLED)
            self.third_confirm_btn = 1
            return

        if self.third_confirm_btn == 1 :
            self.btn_path_path_img_corr.config(fg='orange')
            self.btn_path_img_corr_import.config(state=tk.NORMAL)
            self.entry_path_img_corr.config(state=tk.NORMAL)
            self.third_confirm_btn = 0
            return

    def new_proj(self):
        print()
        # self.cav1.place(relx=0,rely=0,relwidth=1,relheight=0.9)

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
    # def make_list_area_0(self):
    #     self.scrollbar_listbox_0 = tk.Scrollbar(self.cav1_2)
    #     self.scrollbar_listbox_0.place(x=self.import_btn.winfo_x()+self.cav1_2.winfo_width()-40,y=self.import_btn.winfo_y()+60,width=15,height=200)
    #     self.listbox_dir_img_list_0 = tk.Listbox(self.cav1_2,yscrollcommand=self.scrollbar_listbox_0.set)
    #     self.listbox_dir_img_list_0.place(x=self.import_btn.winfo_x(),y=self.import_btn.winfo_y()+60,width=self.cav1_2.winfo_width()-40,height=200)
    #     self.listbox_dir_img_list_0.config(bd=2,relief=GROOVE)


    #     img_list_0 = [img for img in os.listdir(self.filePath)]
    #     # print(img_list_0[0])    # testing
    #     for img in img_list_0:
    #         print(type(img))
    #         print(img)
    #         if img[-6:-1] == '_0.bm':
    #             self.listbox_dir_img_list_0.insert(END,img)
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------



        
        
mainpage(root)
root.mainloop()