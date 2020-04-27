import os
from PIL import Image
from tqdm import tqdm



def remake_label(img_lst, img_dir):
    for img_index in tqdm(img_lst):
        img = Image.open(img_dir + img_index)

        for w in range(width):
            for h in range(height):
                pixel_val = img.getpixel((w,h))
                if pixel_val == 0:
                    img.putpixel((w, h), (9))
                elif pixel_val == 1:
                    img.putpixel((w, h), (1))
                elif pixel_val == 2:
                    img.putpixel((w, h), (1))
                elif pixel_val == 3:
                    img.putpixel((w, h), (6))
                elif pixel_val == 4:
                    img.putpixel((w, h), (18))
                elif pixel_val == 5:
                    img.putpixel((w, h), (1))
                elif pixel_val == 6:
                    img.putpixel((w, h), (0))
                elif pixel_val == 7:
                    img.putpixel((w, h), (5))
                elif pixel_val == 8:
                    img.putpixel((w, h), (1))
                elif pixel_val == 9:
                    img.putpixel((w, h), (1))
                elif pixel_val == 10:
                    img.putpixel((w, h), (1))
                elif pixel_val == 11:
                    img.putpixel((w, h), (4))
                elif pixel_val == 12:
                    img.putpixel((w, h), (16))
                elif pixel_val == 13:
                    img.putpixel((w, h), (1))
                elif pixel_val == 14:
                    img.putpixel((w, h), (1))
                elif pixel_val == 15:
                    img.putpixel((w, h), (11))
                elif pixel_val == 16:
                    img.putpixel((w, h), (14))
                elif pixel_val == 17:
                    img.putpixel((w, h), (1))
                elif pixel_val == 18:
                    img.putpixel((w, h), (1))
                elif pixel_val == 19:
                    img.putpixel((w, h), (1))
                elif pixel_val == 20:
                    img.putpixel((w, h), (1))
                elif pixel_val == 21:
                    img.putpixel((w, h), (3))
                elif pixel_val == 22:
                    img.putpixel((w, h), (2))
                elif pixel_val == 23:
                    img.putpixel((w, h), (20))
                elif pixel_val == 24:
                    img.putpixel((w, h), (12))
        img.save(NEW_IMG_DIR + img_index, "png")

width = 512
height = 512

# new_img = Image.new('RGB', (width, height))

IMG_DIR = './data/source/final_label_images/'
NEW_IMG_DIR = './data/source/final_label_images/'
img_lst = os.listdir(IMG_DIR)

remake_label(img_lst, IMG_DIR)