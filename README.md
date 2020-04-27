# Everybody Dance Now with BodyPix:

The motion transfer task is essentially an image / video synthesis task based on motion information. This task can be divided into two sub-problems, one is to seek a representation that can properly express motion information, and the second is to try to find the mapping function between the motion information representation and the image domain.

Everybody Dance Now, the original paper use 2D skeleton model as motion information representation, now we try to use Part Map as motion information representation instead of 2D skeleton model. But later, I think this is not a good idea, because Part Map bring more identity information (such as height, fat and thin) of source people to target people. Intuitively speaking, the final result will not look like the target people.



# Configuration:

Usually we need a pose estimation model and a generative model to reach our purpose.

In this project, we use: BodyPix + Pix2PixHD



# Installation:

The source code of BodyPix and Pix2PixHD is included, we can find it in `src/`.

We need to install dependencies and prepare the build directory by running `yarn` in `src/body-pix/demos`. please make sure you have install `yarn` before running the command.

If you still want to use 2D skeleton model as motion information representation, please refer to [EverybodyDanceNow_reproduce_pytorch](https://github.com/CUHKSZ-TQL/EverybodyDanceNow_reproduce_pytorch). This repository take 18 key point model to be the motion information representation , if you want to make the same labels like original paper(include face key points, hand key points and body key points), please refer to [OpenPose Video Installation Guide](https://www.youtube.com/watch?v=QC9GTb6Wsb4&feature=youtu.be).



# Preparation:

Put the source video in `src/body-pix/demos` folder, rename it to `source_video.mp4`.

Put the target video in `src/body-pix/demos` folder, rename it to `target_video.mp4`.



# Quick Start:

0. Run `python 0. prepare_folder.py` to build `data` folder structure, which we used to store our data. If you run this command again, the `data` folder will be removed and all the data will be deleted.

1. Prepare source dataset and target dataset. 

   1) target dataset: 

   ​	To obtain video frames:

   ​		Step 1: Find `segmentBodyInRealTime()` in `src/body-pix/demos/index.js`. Comment `const canvas = document.getElementById('output');` and uncomment `const canvas = document.getElementById('main');`. Comment `line 654 to line 713`.

   ​		Step 2: Open `index.html` in `src/body-pix/demos/`, change `src` attribute's value to `target_video.mp4`.

   ​		Step 3: Set your browser's download location as `data/target/ori_images/`.

   ​		Step 4: In `src/body-pix/demos` folder, run `yarn watch`. [ Be careful, make sure you have enough space on your hard drive. Not only the disk where this project placed, but also the boot disk, normally is `C:`, browser cache will be generated here! ]

   

   ​	To obtain corresponding labels:

   ​		Step 1: Find `segmentBodyInRealTime()` in `src/body-pix/demos/index.js`. Uncomment `const canvas = document.getElementById('output');` and comment `const canvas = document.getElementById('main');`. Uncomment `line 654 to line 713`.

   ​		Step 2: Set your browser's download location as `data/target/label_images/`.

   ​		Step 3: In `src/body-pix/demos` folder, run `yarn watch`. [ Be careful again! ]

   

   2) source dataset: put labels of every frames in source video in `data/source/label_images/`.

   ​	To obtain labels:

   ​		Step 1: Find `segmentBodyInRealTime()` in `src/body-pix/demos/index.js`. Uncomment `const canvas = document.getElementById('output');` and comment `const canvas = document.getElementById('main');`. Uncomment `line 654 to line 713`.

   ​		Step 2: Set your browser's download location as `data/source/label_images/`.

   ​		Step 3: In `src/body-pix/demos` folder, run `yarn watch`. [ Be careful again and again! ]

   

   After all steps done above:

   ​	① run `python 1.1 resize_image.py` for `/data/source/label_images/`, `data/target/label_images/` and `data/target/ori_images/`. [ Remember to change the path in the script ] 

   Check result in `data/source/resized_label_images/`, `data/target/resized_label_images/` and `data/target/resized_ori_images/`.

   ​	② run `python 1.2 make_label.py` for `data/source/resized_label_images/` and `data/target/resized_label_images/`. [ Remember to change the path in the script ]

   Check result in `data/source/final_label_images/` and `data/target/final_label_images/`.

   ​	③ run `python 1.3 remake_label.py ` for `data/source/final_label_images/`. Check result in the same place, `data/source/final_label_images/`.

   ​		Why we need this step? That's because the label of the source video and the label of the target video are not in a one-to-one correspondence! For example, the value of LEFT UPPER HAND region in target video is 7. But the value 7 in source video maybe represent RIGHT UPPER LEG region! We need to fix this issue by listing the correspondence between values and regions, both source video and target video. And correct the value of labels in `data/source/final_label_images/`. [ Need to make changes in the script.]

2. Run `python 2. train.py` to train the generative model.

3. Run `python 3. normalize.py` to normalize the labels in `data/source/final_label_image/`, check the result in `data/source/final_label_image_norm/`.

4. Run `python 4. transfer.py` to get the generated frames, you can check it in `results/`.

5. Run `python 5. make_gif.py` to get the final gif result `output.gif` in current folder.



# Reference:

[EverybodyDanceNow_reproduce_pytorch](https://github.com/CUHKSZ-TQL/EverybodyDanceNow_reproduce_pytorch)

[Motion Transfer using Person Segmentation](https://github.com/smellslikeml/MotionTransfer_PersonSeg)

[BodyPix](https://github.com/tensorflow/tfjs-models/tree/master/body-pix)

[OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)

[Pix2PixHD](https://github.com/NVIDIA/pix2pixHD)





