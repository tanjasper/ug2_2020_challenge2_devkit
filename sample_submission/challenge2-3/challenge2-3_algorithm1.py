import os
import shutil
import matplotlib.image as mpimg
import scipy.misc
from scipy.io import loadmat
from tikhonov_reconstruction_code.python import flatcam

src_dir = '/root/challenge2-3_test_input'

calib = loadmat('tikhonov_reconstruction_code/flatcam_calibdata.mat')  # load calibration data
flatcam.clean_calib(calib)
lmbd = 3e-4

# find the best threshold on the validation set
same_dists = []
diff_dists = []

with open('/root/challenge2-3_')

with open('/root/challenge2-3_test_pairs.txt', 'r') as fp:


for file in os.listdir(src_dir):
    if file.endswith('.png'):
        # run tikhonov reconstruction
        meas = mpimg.imread(os.path.join(src_dir, file))  # load flatcam measurement
        recon = flatcam.fcrecon(meas, calib, lmbd)