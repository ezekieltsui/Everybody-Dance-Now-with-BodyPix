import os
import cv2
import numpy as np
from tqdm import tqdm

# images_dir = './data/target/ori_images/'
# target_dir = './data/target/resized_ori_images/'
# images_dir = './data/target/label_images/'
# target_dir = './data/target/resized_label_images/'
images_dir = './data/source/label_images/'
target_dir = './data/source/resized_label_images/'

num_pic = 750
new_index = 0
for index in tqdm(range(num_pic)):
        img = cv2.imread(images_dir + '/{:05}.png'.format(index))
        if img is not None:
            shape_dst = np.min(img.shape[:2])
            oh = (img.shape[0] - shape_dst) // 2
            ow = (img.shape[1] - shape_dst) // 2
            img = img[oh:oh + shape_dst, ow:ow + shape_dst]

            img_resized = cv2.resize(img, (512, 512))
            cv2.imwrite((target_dir + '{:05}.png').format(new_index), img_resized)
            new_index = new_index + 1