from PIL import Image, ImageFilter, ImageEnhance

#открой файл с оригиналом картинки
with Image.open('путь к картинке') as original:
    print('Размер фото:', original.size)
    print('Формат фото:', original.format)
    print('Цвет фото:', original.mode)
    original.show()
#сделай оригинал изображения чёрно-белым
org_bl = original.convert('L')
org_bl.save('gray.jpg')
org_bl.show()
#сделай оригинал изображения размытым
org_blur = original.filter(ImageFilter.BLUR)
org_blur.save('blured.jpg')
org_blur.show()
#поверни оригинал изображения на 180 градусов
org_up = original.transpose(Image.ROTATE_180)
org_up.save('up.jpg')
org_up.show()
