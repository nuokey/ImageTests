from PIL import Image, ImageDraw

size = (300, 300)

im = Image.new("RGB", size)
draw = ImageDraw.Draw(im)

for y in range(-size[1], size[1], 10):
    for x in range(size[0]):
        draw.point((x + y, x), (255, 255, 255))

im.show()