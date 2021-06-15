import glob          
import os              
from PIL import Image

def md(path):
    if not os.path.isdir(path):
        os.makedirs(path) 
        print("makedir: " + path)

size = int(input())                                            
                                                                                
for name in glob.glob('assets/**/*.png', recursive=True):                             
    img = Image.open(name)
    resize = img.resize((size, size), Image.LANCZOS)
    out = "out\\" + str(size) + "\\" + name
    pathlist = out.split('\\')
    del pathlist[-1]
    mdpath = ""
    for st in pathlist:
        mdpath = mdpath + st + "\\"
    md(mdpath)
    resize.save(out)
    print("resize " + str(size) + "x" + str(size) + " : " + name)
