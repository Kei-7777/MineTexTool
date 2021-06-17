import glob          
import os              
import cv2
from PIL import Image

def md(path):
    if not os.path.isdir(path):
        os.makedirs(path) 
        print("makedir: " + path)

size = float(input())                                            
                                                                                
for name in glob.glob('assets/**/*.png', recursive=True):                             
    img = Image.open(name)
    if size < 1.0:
        height = int(img.height*size)
        width = int(img.width*size)
        if height < 1:
            height = 1
        if width < 1:
            width = 1
        resize = img.resize((width, height), Image.LANCZOS)
        out = "out\\" + str(size) + "\\" + name
        pathlist = out.split('\\')
        del pathlist[-1]
        mdpath = ""
        for st in pathlist:
            mdpath = mdpath + st + "\\"
        md(mdpath)
        resize.save(out)
        print("resize Pillow->" + str(size) + "x" + str(size) + " : " + name)
    else:
        img = cv2.imread(name)
        height = int(img.shape[0]*size)
        width = int(img.shape[1]*size)
        if height < 1:
            height = 1
        if width < 1:
            width = 1
        # 段階的にResize
        resize = cv2.resize(img , (width, height))
        out = "out\\" + str(size) + "\\" + name
        pathlist = out.split('\\')
        del pathlist[-1]
        mdpath = ""
        for st in pathlist:
            mdpath = mdpath + st + "\\"
        md(mdpath)
        cv2.imwrite(out, resize)
        print("resize OpenCV->" + str(size) + "x" + str(size) + " : " + name)
