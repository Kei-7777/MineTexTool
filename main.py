import glob          
import os         
import shutil as ut     
import numpy as np
from PIL import Image

def md(path):
    if not os.path.isdir(path):
        os.makedirs(path) 
        print("makedir: " + path)

size = float(input())                                      
                                                                                
for name in glob.glob('assets/**/*.png', recursive=True):
    if size < 1.0:
        img = Image.open(name)
        height = int(img.height*size)
        width = int(img.width*size)
        if height < 1:
            height = 1
        if width < 1:
            width = 1
        resize = img.resize((width, height), Image.LANCZOS)
        # resize = img.resize((width, height), Image.NEAREST)
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
        image = np.asarray(Image.open(name).convert("RGB"), dtype=np.uint8)
        zoomed_image = image.repeat(size, axis=0).repeat(size, axis=1)
        resize = Image.fromarray(zoomed_image)
        out = "out\\" + str(size) + "\\" + name
        pathlist = out.split('\\')
        del pathlist[-1]
        mdpath = ""
        for st in pathlist:
            mdpath = mdpath + st + "\\"
        md(mdpath)
        resize.save(out)
        print("resize Numpy->" + str(size) + "x" + str(size) + " : " + name)
        
# mcmeta
for name in glob.glob('assets/**/*.mcmeta', recursive=True):
    out = "out\\" + str(size) + "\\" + name
    pathlist = out.split('\\')
    del pathlist[-1]
    mdpath = ""
    for st in pathlist:
        mdpath = mdpath + st + "\\"
    md(mdpath) 
    ut.copyfile(name, out)
    print("mcmeta copy->" + str(out))
