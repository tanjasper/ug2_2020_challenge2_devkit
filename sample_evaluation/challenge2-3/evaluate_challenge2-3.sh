DOCKER_IMAGE=tanjasper/ug2_2020_samples:challenge2-3

# Pull the Docker image
docker pull $DOCKER_IMAGE

# Run the Docker container, mounting the input images and output directory
echo Running submission
docker run --rm -i -t \
    --name ug2_challenge2-3_submission_exec \
		-v $(pwd)/test_pairs.txt/:/root/challenge2-3_test_pairs.txt \
    -v $(pwd)/../meas_input/:/root/challenge2-3_test_input:ro \
    -v $(pwd)/outputs/:/root/challenge2-3_test_output \
    -v $(pwd)/run_submissions.sh:/root/run_submissions.sh \
    $DOCKER_IMAGE \
    /bin/bash ./run_submissions.sh
echo Done running submission

docker pull tanjasper/ug2_2020_samples:evaluation

echo Running verification and evaluation
docker run --rm -i -t \
    --name ug2_challenge2-3_evaluation \
    -v $(pwd)/outputs/:/root/predictions \
		-v $(pwd)/test_gt.txt/:/root/test_gt.txt \
    tanjasper/ug2_2020_samples:evaluation \
    python evaluate_verification.py --subchallenge 3 --submissions_dir /root/predictions

echo Evaluation complete
