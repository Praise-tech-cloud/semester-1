
from image import Image

img = Image.read("feep.pgm")

img = Image.read("coins.pgm") 
print(img.get(1,1))
img._invert_img()
img.write_pgm("new.pgm")