from PIL import Image, ImageDraw

size = (300, 300)

im = Image.new("RGB", size)
draw = ImageDraw.Draw(im)

for y in range(0, size[1], 10):
    for x in range(size[0]):
        draw.point((x, y), (255, 255, 255))

for y in range(size[1]):
    for x in range(0, size[0], 10):
        draw.point((x, y), (255, 255, 255))

im.show()