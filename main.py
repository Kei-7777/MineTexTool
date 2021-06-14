import glob                        
from PIL import Image                                             
                                                                                
for name in glob.iglob('**/*.png', recursive=True):                             
    img = Image.open(name)
    resize = img.resize((4, 4), Image.LANCZOS)
    resize.save(out)
    print(name)
