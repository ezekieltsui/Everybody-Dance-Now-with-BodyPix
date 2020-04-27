import os
import shutil

# print(type(os.getcwd()))
# ------data folder-----------
data_dir = './data/'
source_dir = data_dir + 'source/'
target_dir = data_dir + 'target/'

source_label_images_dir = source_dir + 'label_images/'
source_resized_label_images_dir = source_dir + 'resized_label_images/'
source_final_label_images_dir = source_dir + 'final_label_images/'
source_final_label_images_norm_dir = source_dir + 'final_label_images_norm/'

target_ori_images_dir = target_dir + 'ori_images/'
target_label_images_dir = target_dir + 'label_images/'
target_resized_label_images_dir = target_dir + 'resized_label_images/'
target_resized_ori_images_dir = target_dir + 'resized_ori_images/'
target_final_label_images_dir = target_dir + 'final_label_images/'

if not os.path.exists(data_dir):
    os.mkdir(data_dir)
    if not os.path.exists(source_dir):
        os.mkdir(source_dir)
        if not os.path.exists(source_label_images_dir):
            os.mkdir(source_label_images_dir)
        if not os.path.exists(source_resized_label_images_dir):
            os.mkdir(source_resized_label_images_dir)
        if not os.path.exists(source_final_label_images_dir):
            os.mkdir(source_final_label_images_dir)
        if not os.path.exists(source_final_label_images_norm_dir):
            os.mkdir(source_final_label_images_norm_dir)
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
        if not os.path.exists(target_ori_images_dir):
            os.mkdir(target_ori_images_dir)
        if not os.path.exists(target_label_images_dir):
            os.mkdir(target_label_images_dir)
        if not os.path.exists(target_resized_ori_images_dir):
            os.mkdir(target_resized_ori_images_dir)  
        if not os.path.exists(target_resized_label_images_dir):
            os.mkdir(target_resized_label_images_dir)  
        if not os.path.exists(target_final_label_images_dir):
            os.mkdir(target_final_label_images_dir)    
        
else:
    shutil.rmtree(data_dir)


# ------checkpoint folder-----------
checkpoint_dir = './checkpoint'
result_dir = ''


