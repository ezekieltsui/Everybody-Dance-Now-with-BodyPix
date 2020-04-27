from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import os
from tqdm import tqdm

kmeans = KMeans(n_clusters=25, init='k-means++', max_iter=300, n_init=10, random_state=0)

def generate_mask(img_lst, img_dir, save=True):
    """
    Generate mask with new mapping
    Input is a list of image file names and directory where images are stored
    Set the save variable to True to overwrite masks with new masks
    Returns a list of successful converted masks and a list of failed conversions
    """
    colors = []
    for im in tqdm(img_lst):
        im = np.array(Image.open(img_dir + im))
        for val in np.unique(im.reshape(-1, im.shape[2]), axis=0):
            colors.append(val)
    # get unique colors from list of images
    pixel_vals = np.unique(np.array(colors), axis=0)
    
    # predict mapping to 25 colors
    pred_y = kmeans.fit_predict(pixel_vals)
    print(set(pred_y))
    #generate color map
    color_map = dict(zip(tuple((tuple(tup) for tup in pixel_vals)), pred_y))
    
    # transform overlays
    generated_imgs = []
    failed_imgs = []
    for im in tqdm(img_lst):
        img_index = im
        try:
            im = np.array(Image.open(img_dir + im))
            imm = im.reshape(-1, im.shape[2])
            for idx, pixel in enumerate(imm):
                new_color = [color_map[tuple(pixel)]] * 3
                imm[idx] = new_color
            imm = imm.reshape(512, 512, 3)
            save_img = Image.fromarray(imm)
            generated_imgs.append(save_img)
            if save:
                save_img = save_img.convert('L')
                save_img.save(NEW_IMG_DIR + img_index, "png")
        except:
            failed_imgs.append(im)
    return generated_imgs, failed_imgs


IMG_DIR = './data/source/resized_label_images/'
NEW_IMG_DIR = './data/source/final_label_images/'
img_lst = os.listdir(IMG_DIR)

success_imgs, failed_imgs = generate_mask(img_lst, IMG_DIR)

