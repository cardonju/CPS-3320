

from PIL import Image, ImageFilter

#applying 2 conversion to an image


img = Image.open('')  #select an image path between ''
img.convert("L").save(
    "result/im_convert_m_L_01.jpg")
img.convert("1").save(
    "result/im_convert_m_1_01.jpg")

im = Image.open('')  #select any image path between ''

print(im.format, im.size, im.mode)  #printing file info

# scale convertion rotate 180 degrees and adding filter
new_im = im.convert('L').rotate(180).filter(ImageFilter.GaussianBlur()) #

new_im.save('data/dst/anyname.jpg', quality=95)