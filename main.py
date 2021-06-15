import glob                        
from PIL import Image 

size = int(input())                                            
                                                                                
for name in glob.iglob('**/*.png', recursive=True):                             
    img = Image.open(name)
    resize = img.resize((size, size), Image.LANCZOS)
    resize.save(out)
    print(name)
