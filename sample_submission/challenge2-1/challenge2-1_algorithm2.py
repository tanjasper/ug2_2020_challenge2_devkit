import os
import shutil
import imageio
import numpy as np

src_dir = '/root/challenge2-1_test_input'
dest_dir = '/root/challenge2-1_test_output/submission2'

for file in os.listdir(src_dir):
    if file.endswith('.png'):
        # read in image and apply gamma correction
        im = imageio.imread(os.path.join(src_dir, file))
        im = (np.float32(im) / np.iinfo(im.dtype).max) ** 0.8
        im = np.uint8(im * 255)
        imageio.imwrite(os.path.join(dest_dir, file), im)
