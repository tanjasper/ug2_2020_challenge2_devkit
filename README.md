# UG2 2020 Challenge 2 Development Kit
This repository contains the development kit for Challenge 2 of the CVPR 2020 UG2 Challenge.

### Sample Submissions

Submissions must be **Docker images** uploaded to Dockerhub. Sample submissions provided by the organizers for each of the subchallenges can be found in the following Dockerhub repository: 

https://hub.docker.com/repository/docker/tanjasper/ug2_2020_samples

We also provide the source Dockerfiles and accompanying scripts in _sample_submissions_. To build the Docker images, simply navigate to the correct subchallenge directory in _sample_submissions_ and run `Docker build -t <image_name> .`.

### Sample Evaluation Code

We also provide sample evaluation code, found in _sample_evaluation_ based on the code we will use to grade your submissions. These can be used to ensure your submission follows the expected format.

For subchallenges 1 and 2, we will run off-the-shelf face verification algorithms on your provided images. For the sample evaluation code, we simply use a dummy face verification algorithm.

The sample evaluation data is a subset of the validation set provided with the FlatCam Face Dataset (based on subjects 61-87). You may use this data to validate your methods. The actual test data consists of images of subjects not included in the FCFD (but captured in the same manner).

To run the sample evaluation code, follow the corresponding steps:

1. Choose __one__ of the following two ways to download sample test data
   1. Install gdown (`pip install gdown` in Terminal), and then navigate to `sample_evaluation` and run `./download_evaluation_data.sh` in Terminal.
   2. Manually download and unzip the following two directories from Google Drive and place them in `sample_evaluation`:
      - https://drive.google.com/open?id=15nzEP_K16TwTTz6xqWTgSVsX9qB_QDA4
      - https://drive.google.com/open?id=1Hu567rjzbeUgjqiYaxpwwrb_iRDj_w0Q
2. Navigate to _sample_evaluation/challenge2-#_ where # is the subchallenge number.
3. Set the `DOCKER_IMAGE` variable in _evaluate_challenge2-#.sh_ to the name of your Docker image submission in Dockerhub.
4. Run _evaluate_challenge2-#.sh_. The outputs will be placed in _sample_evaluation/challenge2-#/outputs_. Check that *verification_scores.txt* was saved in the outputs folder to see if the evaluation successfully ran all the way through.

### Tikhonov Reconstruction Code

We provide code to perform Tikhonov reconstruction in _tikhonov_reconstruction_code_. Both Python and Matlab functions are provided. Examples are available in _tikhonov_reconstruction_code/matlab/demo.m_ and _tikhonov/reconstruction_code/python/demo.py_. 

For details on the reconstruction procedure, see the following paper (in particular, Sections III and IV):

https://ieeexplore.ieee.org/document/7517296 (or pre-print available here: https://arxiv.org/abs/1509.00116)

We now describe in a high-level the reconstruction pipeline performed in the code. The following image represents the pipeline:

![FlatCam pipeline](https://github.com/tanjasper/ug2_2020_challenge2_devkit/figs/pipeline.png)

The FlatCam sensor is in a Bayer-filtered format. That is, pixels measure only one of the 3 RGB colors, and they are grouped into four pixels: 1 blue, 2 green, and 1 red. The FlatCam model is that the measurement for each of those four channels is a separable linear function of the corresponding color channel of the scene. In particular, the model is $P_{1c} X Q_{1c}^T$, where $P_{1c}$ and $Q_{1c}$ ($\Phi_L$ and $\Phi_R$ in the paper) are matrices obtained via calibration and $c$ represents the color channel. These matrices are saved in flatcam_calibdata.mat. Tikhonov reconstruction (Eq. 7 in Asif, et al 2017) is then performed on each of the color channels, and the reconstruction of each color channel is merged to form the RGB image.
