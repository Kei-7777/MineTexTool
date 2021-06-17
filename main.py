import glob          
import os              
from PIL import Image

def md(path):
    if not os.path.isdir(path):
        os.makedirs(path) 
        print("makedir: " + path)

size = float(input())                                            
                                                                                
for name in glob.glob('assets/**/*.png', recursive=True):                             
    img = Image.open(name)
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
    print("resize " + str(size) + "x" + str(size) + " : " + name)
