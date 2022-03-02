import os
import tkinter as tk
from tkinter import Frame, filedialog
from tkinter.constants import END, GROOVE, SUNKEN
import tkinter.font as tkFont
from tkinter import ttk
import threading




import interface.interface
import method.initialization


root = tk.Tk()
root.title('[No Job] TIRI_000')
#root.attributes('-fullscreen',True)
# root.state('zoomed')
root.geometry("1500x800+210+0")
root.minsize(1500,800)
root.maxsize(1500,800)


class mainpage(object):
    def __init__(self,master = None,*args):
        self.root = master

        # clear initialize the root folder
        method.initialization.run()

        self.filemenu = tk.Menu(self.root)
        self.root.config(menu=self.filemenu)
        self.menu1 = tk.Menu(self.filemenu)


        self.cav1 = tk.Canvas(self.root,state=tk.DISABLED)
        # self.cav1.place(relx=0,rely=0,relwidth=1,relheight=0.99)
        self.cav1_1 = tk.Canvas(self.cav1,bg='white',bd=3,relief=GROOVE)
        self.cav1_1.place(relx=0.005,rely=0.05,relwidth=0.78,relheight=0.98)
        self.cav1_2 = tk.Canvas(self.cav1,bg='white',bd=3,relief=GROOVE,background="white")
        self.cav1_2.place(relx=0.785,rely=0.05,relwidth=0.21,relheight=0.98)
        self.bg_cav1_2 = tk.PhotoImage(file='./ui/bg.png')
        self.label_bg_cav1_2 = tk.Label(self.cav1_2,image=self.bg_cav1_2)
        self.label_bg_cav1_2.place(x=0,y=0)

        self.menu1.add_command(label='create a new project',command=self.new_proj)
        self.menu1.add_command(label='open a project')
        self.menu1.add_command(label='exit',command=root.quit)


        self.filemenu.add_cascade(label='File',menu=self.menu1)
        self.filemenu.add_cascade(label='Reference')

        self.label1=tk.Label(self.cav1,text=u'canvas 1')
        self.label1.place(x=0,y=0)

        self.label2 = tk.Label(self.cav1_1,text=u'canvas 1_1')
        self.label2.place(x=10,y=10)

        #font style
        self.fontStyle = tkFont.Font(family="Terminal", size=10)
        self.fontStyle_run = tkFont.Font(family="Terminal", size=15)

        self.img_menu = tk.PhotoImage(file='./ui/menu.png')
        self.sep_img = tk.PhotoImage(file='./ui/sep.png')

        self.rdio_calib_value = tk.IntVar()
        self.rdio_skip_value = tk.IntVar()

        self.label_menu = tk.Label(self.cav1_2,image=self.img_menu,bg=self._from_rgb((36,36,36)))
        self.sep = tk.Label(self.cav1_2,image=self.sep_img)

        self.s = ttk.Style()
        self.s.theme_use('clam')
        self.s.configure("orange.Horizontal.TProgressbar", foreground='orange', background='orange')

        self.label_cam_cali = tk.Label(self.cav1_2,text=u'Camera  Calibration : ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='white')
        self.rdio_run_calib = tk.Radiobutton(self.cav1_2, text=u'Import',variable=self.rdio_calib_value, value= 1,bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='white',command=self.activeImporCaliImage)
        self.rdio_skip_calib = tk.Radiobutton(self.cav1_2,text=u'Skip',variable=self.rdio_calib_value,value= 0,bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='white',command=self.activeImporCaliImage)
        self.btn_import_cali_img = tk.Button(self.cav1_2,text=u' Import ... ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='orange',state=tk.DISABLED,command=self.fileImportCali)
        # self.combo_cali_slip = ttk.Combobox(self.cav1_2,values=["Last one","import"],state=tk.DISABLED)
        self.label_path_cali_img = tk.Label(self.cav1_2,text=u'Path : ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='white',state=tk.DISABLED)
        self.entry_calib_path = tk.Entry(self.cav1_2,bg='AntiqueWhite1',state=tk.DISABLED)
        self.btn_path_comfirm_cail = tk.Button(self.cav1_2,text=u' Confirm ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='orange',state=tk.DISABLED)
        self.label_cali_opt = tk.Label(self.cav1_2,text=u'Calibration Option : ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='white',state=tk.DISABLED)
        self.rdio_skip_priv = tk.Radiobutton(self.cav1_2, text=u' Previous ',variable=self.rdio_skip_value, value= 0,bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='white')
        self.rdio_skip_import = tk.Radiobutton(self.cav1_2,text=u' Import ',variable=self.rdio_skip_value,value= 1,bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='white')
        self.btn_skip_import = tk.Button(self.cav1_2,text=u' Import ... ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='orange',state=tk.DISABLED)
        self.label_path_skip_cali_import = tk.Label(self.cav1_2,text=u'Path : ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='white',state=tk.DISABLED)
        self.entry_skip_cali_import_path = tk.Entry(self.cav1_2,bg='AntiqueWhite1',state=tk.DISABLED)
        self.btn_path_comfirm_skip_cail = tk.Button(self.cav1_2,text=u' Confirm ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='orange',state=tk.DISABLED)
        self.label_img_correction = tk.Label(self.cav1_2,text=u'Image  Correction : ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='white')
        self.btn_path_img_corr_import = tk.Button(self.cav1_2,text=u' Import ... ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='orange')
        self.label_path_img_corr = tk.Label(self.cav1_2,text=u'Path : ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='white')
        self.entry_path_img_corr = tk.Entry(self.cav1_2,bg='AntiqueWhite1')
        self.btn_path_path_img_corr = tk.Button(self.cav1_2,text=u' Confirm ',bg=self._from_rgb((36,36,36)),font=self.fontStyle,fg='orange')
        self.btn_run = tk.Button(self.cav1_2,text=u' Run ',bg=self._from_rgb((36,36,36)),font=self.fontStyle_run,fg='orange')
        self.progressbar = ttk.Progressbar(self.cav1_2,length=280,style="orange.Horizontal.TProgressbar",mode='indeterminate',value=0,orient=tk.HORIZONTAL)
        self.progressbar.step(1)


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

        # Generating a btn
        self.dbscan_btn=tk.Button(self.cav1_2,text=u'DBSCAN',command=self.threadClickDbscan)

    def _from_rgb(self,rgb):
        return "#%02x%02x%02x" % rgb
#------------------------------------------------------------------------------------------------------

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
        

    def fileImportCali(self):
        if self.entry_calib_path.winfo_ismapped() == 0:
            self.entry_calib_path.grid(padx=15,ipady=5,row=5,rowspan=1,columnspan=2,sticky="we")
        self.file_path_cali = filedialog.askdirectory(parent=root,initialdir='~/')
        self.entry_calib_path.delete(0,END)
        self.entry_calib_path.insert(0,self.file_path_cali)
        # # Button is generated
        # self.proc_btn = tk.Button(self.cav1_2,text=u'IMPORT OBJECT IMAGE',command=self.fileImportProc)
        # self.proc_btn.place(x=self.import_btn.winfo_x(),y=self.import_btn.winfo_y()+50,width=180,height=30)
        # root.title('[Calibration Image Imported] TIRI_000')
    
    def fileImportProc(self):
        self.file_path_proc = filedialog.askdirectory(parent=root,initialdir='~/')
        self.entry_proc_path = tk.Entry(self.cav1_2,bg='AntiqueWhite1')
        self.entry_proc_path.place(x=self.import_btn.winfo_x(),y=self.proc_btn.winfo_y()+30,relwidth=0.9)
        # self.calib_path_entry.place(x=self.calibr_btn.winfo_x(),y=self.calibr_btn.winfo_y()+30,width=self.cav1_2.winfo_width()-25)
        self.entry_proc_path.insert(0,self.file_path_proc)
        # Button is generated
        self.calibr_btn = tk.Button(self.cav1_2,text=u'RUN CALIBRATION',command=self.threadClickCali)
        self.calibr_btn.place(x=self.import_btn.winfo_x(),y=self.proc_btn.winfo_y()+50,width=180,height=30)


    
    def new_proj(self):
        self.cav1.place(relx=0,rely=0,relwidth=1,relheight=0.9)

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
    
    def threadClickCali(self):
        # Disable the import and run cailb btn
        self.import_btn.configure(state=tk.DISABLED)
        self.proc_btn.configure(state=tk.DISABLED)
        self.calibr_btn.configure(state=tk.DISABLED)
        root.title('[Calibration Loading] TIRI_000')

        threading.Thread(target=self.runCali).start()
        
    def runCali(self):
        # Calling the interface of class interfaceCalibration
        self.class01=interface.interface.interfaceCalibration()
        self.class01.calib(self.file_path_cali)
        
        # Button is generated
        self.imgProc_btn = tk.Button(self.cav1_2,text=u'IMAGE PROCESSING',command=self.threadClickProc)
        self.imgProc_btn.place(x=self.import_btn.winfo_x(),y=self.calibr_btn.winfo_y()+30,width=180,height=30)
        # Change title
        root.title('[Calibration Done] TIRI_000')

    def threadClickProc(self):
        # Disable the import and run cailb btn
        self.imgProc_btn.configure(state=tk.DISABLED)
        root.title('[Image Processing Loading] TIRI_000')

        threading.Thread(target=self.runProc).start()

    def runProc(self):
        # Undergoing image processing
        self.class01.imgProc(self.file_path_proc)
        # Converting image to video
        interface.interface.interfaceImgToVid().doTransfer()
        self.output_video_btn = tk.Button(self.cav1_2,text=u'MAKE VIDEO',command=self.threadClickMakeVideo)
        self.output_video_btn.place(x=self.import_btn.winfo_x(),y=self.calibr_btn.winfo_y()+60,width=180,height=30)
        root.title('[Image Processing Done] TIRI_000')

    def threadClickMakeVideo(self):
        # Disable the output_video_btn
        self.output_video_btn.configure(state=tk.DISABLED)
        # Changing the title
        root.title('[Video Generate Loading] TIRI_000')
        # run 'runMakeVideo'
        threading.Thread(target=self.runMakeVideo).start()

    def runMakeVideo(self):
        # Convert img to vid
        interface.interface.interfaceImgToVid().doTransfer()

        # Generating a btn
        self.opticalflow_btn=tk.Button(self.cav1_2,text=u'OPTICALFLOW',command=self.threadClickOpticalFlow)
        self.opticalflow_btn.place(x=self.import_btn.winfo_x(),y=self.calibr_btn.winfo_y()+90,width=180,height=30)
        # Changing the title
        root.title('[Video Generate Done] TIRI_000')

    def threadClickOpticalFlow(self):
        # Disable the opticalflow_btn
        self.opticalflow_btn.configure(state=tk.DISABLED)
        # Changing the title
        root.title('[Optical Flow Loading] TIRI_000')
        
        threading.Thread(target=self.runOpticalFlow).start()

    def runOpticalFlow(self):
        interface.interface.interfaceOpticalFlow().doOpticalFlow()
        
        # Generating a btn
        self.Cal_btn=tk.Button(self.cav1_2,text=u'CAL',command=self.threadClickCal)
        self.Cal_btn.place(x=self.import_btn.winfo_x(),y=self.calibr_btn.winfo_y()+120,width=180,height=30)
        # Changing the title
        root.title('[Optical Flow Done] TIRI_000')


    def threadClickCal(self):
        # Changing the title
        root.title('[Cal Loading] TIRI_000')
        self.Cal_btn.configure(state=tk.DISABLED)
        threading.Thread(target=self.runCal).start()
        self.dbscan_btn.place(x=self.import_btn.winfo_x(),y=self.calibr_btn.winfo_y()+150,width=180,height=30)


    def runCal(self):
        self.list_max_frame = interface.interface.interfaceCalulation().doCal()


    def threadClickDbscan(self):
        root.title('[DBScan Loading] TIRI_000')
        threading.Thread(target=self.runDbscan).start()
        self.dbscan_btn.configure(state=tk.DISABLED)
    
    def runDbscan(self):
        interface.interface.interfaceDBScan().doDBScan(self.list_max_frame[0],self.list_max_frame[1])
        # Generating a btn
        self.save_btn=tk.Button(self.cav1_2,text=u'SAVE',command=self.fileSaving)
        self.save_btn.place(x=self.import_btn.winfo_x(),y=self.calibr_btn.winfo_y()+180,width=180,height=30)

    def fileSaving(self):
        self.file_path_saving = filedialog.askdirectory(parent=root,initialdir='~/')
        self.threadClickSave()
        
    def threadClickSave(self):
        threading.Thread(target=self.runSave).start()

    def runSave(self):
        interface.interface.interfaceMoveFolder().doMoveFolder(self.file_path_saving)
        
    def threadClickSkipCalib(self):
        threading.Thread(target=self.skipCalib).start()
        self.import_btn.configure(state=tk.DISABLED)
        self.calibr_btn.configure(state=tk.DISABLED)
    def skipCalib(self):
        # Calling the interface of class interfaceCalibration
        self.class01=interface.interface.interfaceCalibration()
        self.class01.skipCalib()
        # Button is generated
        self.proc_btn = tk.Button(self.cav1_2,text=u'IMPORT OBJECT IMAGE',command=self.fileImportProc)
        self.proc_btn.place(x=self.import_btn.winfo_x(),y=self.import_btn.winfo_y()+50,width=180,height=30)
        root.title('[Calibration Image Imported] TIRI_000')

        # Button is generated
        self.imgProc_btn = tk.Button(self.cav1_2,text=u'IMAGE PROCESSING',command=self.threadClickProc)
        self.imgProc_btn.place(x=self.import_btn.winfo_x(),y=self.import_btn.winfo_y()+120,width=180,height=30)



        
        
mainpage(root)
root.mainloop()