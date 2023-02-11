import os

def doPack(dst_path): #full path

    #check/create the dst path folder
    if os.path.exists(dst_path)==True:
        print(str(dst_path)+' exited')
    else:
        os.system('mkdir '+str(dst_path))

    ls_prog = ['ui', 'interface', '.DS_Store', 'testingBox', 
    '.gitattributes', 'requirement.txt', 'log', 
    'log-camera-calibration-setting', '.vscode', 
    '__main__.py', 'method']
    
    # following elemets need to be kept
    # ['ui', 'interface', '.DS_Store', 'testingBox', 
    # '.gitattributes', 'requirement.txt', 'log', 
    # 'log-camera-calibration-setting', '.vscode', 
    # '__main__.py', 'method']

    ls_element = os.listdir('./')
    for element in ls_element:

        if ls_prog.count(str(element)) == 0 :
            cmd_line = 'mv '+str(element)+' '+str(dst_path)+'/'+str(element)
            os.system(cmd_line)
            print(element,' is moved')
        
            


#===========================================
# doPack('./')