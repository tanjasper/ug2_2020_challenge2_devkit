OUTPUT_DIR=/root/challenge2-3_test_output

if [ -d $OUTPUT_DIR/submission1 ]; then rm -rf $OUTPUT_DIR/submission1; fi
if [ -d $OUTPUT_DIR/submission2 ]; then rm -rf $OUTPUT_DIR/submission2; fi
if [ -d $OUTPUT_DIR/submission3 ]; then rm -rf $OUTPUT_DIR/submission3; fi

if test -f "/root/ug2_challenge2-3_submission1.sh"; then
	mkdir /root/challenge2-3_test_output/submission1
	chmod +x /root/ug2_challenge2-3_submission1.sh
	/root/ug2_challenge2-3_submission1.sh
	mv /root/ug2_challenge2-3_test_output_submission1.txt /root/challenge2-3_test_output/submission1/submission.txt
fi

if test -f "/root/ug2_challenge2-3_submission2.sh"; then
	mkdir /root/challenge2-3_test_output/submission2
	chmod +x /root/ug2_challenge2-3_submission2.sh
	/root/ug2_challenge2-3_submission2.sh
	mv /root/ug2_challenge2-3_test_output_submission2.txt /root/challenge2-3_test_output/submission2/submission.txt
fi

if test -f "/root/ug2_challenge2-3_submission3.sh"; then
	mkdir /root/challenge2-3_test_output/submission3
	chmod +x /root/ug2_challenge2-3_submission3.sh
	/root/ug2_challenge2-3_submission3.sh
	mv /root/ug2_challenge2-3_test_output_submission3.txt /root/challenge2-3_test_output/submission3/submission.txt
fi

