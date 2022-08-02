from PIL import Image

img = Image.open('savedImage.jpg')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] >= 200 and item[1] >= 200 and item[2] >=200 :
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("img2.png", "PNG")