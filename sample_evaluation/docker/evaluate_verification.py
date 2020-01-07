import argparse
import numpy as np
from skimage.io import imread 
from skimage.transform import resize

parser = argparse.ArgumentParser()
parser.add_argument('--image_dir', help='where images are stored', default='/root/images')
parser.add_argument('--subchallenge', type=int)
parser.add_argument('--pairs_txt', help='where pairs txt is located', default='../test_pairs.txt')
parser.add_argument('--gt_txt', help='where gt text is file is located', default='../test_gt.txt')
parser.add_argument('--preds_txt', help='location of predictions for subchallenge 3', default='')
opt = parser.parse_args()


def im2float(im):
    if im.dtype == 'uint8':
        return np.float32(im) / 255.
    if im.dtype == 'uint16':
        return np.float32(im) / 65535.
    if im.dtype == 'float32' or im.dtype == 'float64':
        return im


def dummy_verification(im1, im2):
    """Dummy verification function.

    Returns 1 if the normalized L2 distance between the two images is < 0.5.
    """
    im1 = im2float(im1)
    im2 = im2float(im2)
    if not size(im2) == size(im1):
        im2 = resize(im2, (im1.shape[0], im1.shape[1]), order=3)
    if np.linalg.norm(im1 - im2) / np.linalg.norm(im1) < 0.5:
        return 1
    else:
        return 0


if __name__ == '__main__':
    
    # Will hold predictions
    preds = []

    # Read in pairs and ground truth
    with open(opt.pairs_txt) as f:
        pairs = f.readlines()
    pairs = [line.strip() for line in pairs]
    with open(opt.gt_txt) as f:
        gt = f.readlines()
    gt = [int(line.strip()) for line in gt]

    # Check score for submission
    acc_rates = []
    for submission in range(1,4):
        if os.path.isdir(os.path.join(opt.image_dir, 'submission{}'.format(submission))):

            # For subchallenges 1 and 2, run off-the-shelf verification methods
            if opt.subchallenge in [1, 2]:
                for pair in pairs:
                    im1 = imread(os.path.join(opt.image_dir, pair.split()[0]))
                    im2 = imread(os.path.join(opt.image_dir, pair.split()[1]))
                    preds.append(dummy_verification(im1, im2))

            # For subchallenge 3, just read in provided predictions
            with open(opt.preds_txt) as f:
                preds = f.readlines()
            preds = [int(line.strip()) for line in gt]
            
            # Check predictions
            if any(pred not in [0, 1] for pred in preds):
                raise Exception('Encountered a prediction that is neither 0 nor 1')
            if len(preds) != len(gt):
                raise Exception('Number of predictions do not match number of test pairs')

            # Report accuracy rate
            correct_preds = 0.
            for i in range(len(pred)):
                if pred[i] == gt[i]:
                    correct_preds += 1.
            acc_rates.append(correct_preds / len(gt))
        with open(os.path.join(image_dir, 'verification_scores.txt'), 'w') as f:
            for acc in acc_rates:
                f.write('{}\n'.format(acc))

