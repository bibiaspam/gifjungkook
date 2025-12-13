import os
from PIL import Image
files = os.listdir

img1 = Image.open("jk1.jpg")
img2 = Image.open("jk2.jpg")


imagens = [img1, img2]

imagens[0].save(
    "animacao.gif",
    save_all=True,
    append_images=imagens[1:], 
    duration=500,  
    loop=0        
      )