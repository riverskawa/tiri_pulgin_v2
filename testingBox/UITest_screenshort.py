import os
import tkinter
import tkinter.filedialog
from PIL import ImageGrab
import time


class FreeCapture():
    """ 用來顯示全屏幕截圖並響應二次截圖的窗口類
    """
    def __init__(self, root, img):
        #變量X和Y用來記錄鼠標左鍵按下的位置
        self.X = tkinter.IntVar(value=0)
        self.Y = tkinter.IntVar(value=0)
        #屏幕尺寸
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        #創建頂級組件容器
        self.top = tkinter.Toplevel(root, width=screenWidth, height=screenHeight)
        #不顯示最大化、最小化按鈕
        self.top.overrideredirect(True)
        self.canvas = tkinter.Canvas(self.top,bg='white', width=screenWidth, height=screenHeight)
        #顯示全屏截圖，在全屏截圖上進行區域截圖 
        self.image = tkinter.PhotoImage(file=img)
        self.canvas.create_image(screenWidth//2, screenHeight//2, image=self.image)
        
        self.lastDraw = None
        #鼠標左鍵按下的位置
        def onLeftButtonDown(event):
            self.X.set(event.x)
            self.Y.set(event.y)
            #開始截圖
            self.sel = True

        self.canvas.bind('<Button-1>', onLeftButtonDown)
        
        def onLeftButtonMove(event):
            #鼠標左鍵移動，顯示選取的區域
            if not self.sel:
                return
            try: #刪除剛畫完的圖形，要不然鼠標移動的時候是黑乎乎的一片矩形
                self.canvas.delete(self.lastDraw)
            except Exception as e:
                pass
            self.lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='green')

        def onLeftButtonUp(event):
            #獲取鼠標左鍵擡起的位置，保存區域截圖
            self.sel = False
            try:
                self.canvas.delete(self.lastDraw)
            except Exception as e:
                pass

            time.sleep(0.1)
            #考慮鼠標左鍵從右下方按下而從左上方擡起的截圖
            left, right = sorted([self.X.get(), event.x])
            top, bottom = sorted([self.Y.get(), event.y])
            pic = ImageGrab.grab((left+1, top+1, right, bottom))
            #彈出保存截圖對話框
            fileName = tkinter.filedialog.asksaveasfilename(title='保存截圖', filetypes=[('image', '*.jpg *.png')])

            if fileName:
                pic.save(fileName)
            #關閉當前窗口
            self.top.destroy()

        self.canvas.bind('<B1-Motion>', onLeftButtonMove) # 按下左鍵
        self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp) # 擡起左鍵
        #讓canvas充滿窗口，並隨窗口自動適應大小
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)


def screenShot(root, button_screenShot):
    """ 自由截屏的函數 (button按鈕的事件)
    """
#    print("test")
    root.state('icon')  # 最小化主窗體
    time.sleep(0.2)
    im = ImageGrab.grab()
    # 暫存全屏截圖
    im.save('temp.png')
    im.close()
    # 進行自由截屏 
    w = FreeCapture(root, 'temp.png')
    button_screenShot.wait_window(w.top)
    # 截圖結束，恢復主窗口，並刪除temp.png文件
    root.state('normal')
    os.remove('temp.png')

####
root = tkinter.Tk()
root.title('自由截屏')
#指定窗口的大小
root.geometry('200x200')
#不允許改變窗口大小
root.resizable(False,False)

# ================== 佈置截屏按鈕 ====================================
button_screenShot = tkinter.Button(root, text='截屏', command=lambda:screenShot(root,button_screenShot))
button_screenShot.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)
# ================== 完 =============================================

try:
    root.mainloop()
except:
    root.destroy()