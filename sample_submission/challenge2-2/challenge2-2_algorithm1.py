import os
import shutil
import matplotlib.image as mpimg
import numpy as np
import imageio
from scipy.io import loadmat
from tikhonov_reconstruction_code.python import flatcam

src_dir = '/root/challenge2-2_test_input'
dest_dir = '/root/challenge2-2_test_output/submission1'

calib = loadmat('tikhonov_reconstruction_code/flatcam_calibdata.mat')  # load calibration data
flatcam.clean_calib(calib)
lmbd = 3e-4

counter = 0
for file in os.listdir(src_dir):
    if file.endswith('.png'):
        # run tikhonov reconstruction
        meas = mpimg.imread(os.path.join(src_dir, file))  # load flatcam measurement
        recon = flatcam.fcrecon(meas, calib, lmbd)
        imageio.imwrite(os.path.join(dest_dir, file), np.uint8(recon*255))
        counter += 1
        if counter % 50 == 0:
            print('Submission 1: reconstructed image {}'.format(counter))


