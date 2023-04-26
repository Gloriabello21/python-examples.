#para ejecutar esto en la terminal debe poner python3 costumes.py costume1.git costume2.gif
#luego se pone code costumes.gif
import sys

from PIL import Image
images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)