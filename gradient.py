from PIL import Image, ImageDraw

size = (255, 255)

im = Image.new("RGB", size)
draw = ImageDraw.Draw(im)

for y in range(size[1]):
    for x in range(size[0]):
        if y <= size[1] // 2:
            color1 = y
        else:
            color1 = size[1] - y

        if x <= size[0] // 2:
            color2 = x
        else:
            color2 = size[0] - x
        
        draw.point((x, y), (color2, color1, color2 + color1))

im.show()