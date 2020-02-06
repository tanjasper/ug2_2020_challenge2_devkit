import os
import numpy as np
import matplotlib.image as mpimg
from scipy.io import loadmat
from tikhonov_reconstruction_code.python import flatcam


def im2float(im):
    if im.dtype == 'uint8':
        return np.float32(im) / 255.
    if im.dtype == 'uint16':
        return np.float32(im) / 65535.
    if im.dtype == 'float32' or im.dtype == 'float64':
        return im


def dummy_verification(im1, im2):
    """Dummy verification function.

    Returns 1 if the normalized L2 distance between the two images is < 0.8.
    """
    im1 = im2float(im1)
    im2 = im2float(im2)
    if not im1.shape == im2.shape:
        im2 = resize(im2, (im1.shape[0], im1.shape[1]), order=3)
    if np.linalg.norm(im1 - im2) / np.linalg.norm(im1) < 0.8:
        return 1
    else:
        return 0


if __name__ == '__main__':

    # Load calibration data
    calib = loadmat('tikhonov_reconstruction_code/flatcam_calibdata.mat')
    flatcam.clean_calib(calib)
    lmbd = 3e-4

    # Read in image pair locations
    with open('/root/challenge2-3_test_pairs.txt') as f:
        pairs = f.readlines()
    pairs = [line.strip() for line in pairs]

    # Perform face verification on each pair of images
    preds = []
    counter = 0
    for pair in pairs:
        meas1 = mpimg.imread(pair.split()[0])  # load flatcam measurement
        recon1 = flatcam.fcrecon(meas1, calib, lmbd)  # tikhonov reconstruct
        meas2 = mpimg.imread(pair.split()[1])  # load flatcam measurement
        recon2 = flatcam.fcrecon(meas2, calib, lmbd)
        preds.append(dummy_verification(recon1, recon2))
        counter += 1
        if counter % 100 == 0:
            print('Pair {} out of {}'.format(counter, len(pairs)))
    
    with open('/root/ug2_challenge2-3_test_output_submission1.txt', 'w') as f:
        for pred in preds:
            f.write('{}\n'.format(pred))
