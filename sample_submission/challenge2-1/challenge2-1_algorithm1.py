import os
import shutil

src_dir = '/root/challenge2-1_test_input'
dest_dir = '/root/challenge2-1_test_output/submission1'

for file in os.listdir(src_dir):
    if file.endswith('.png'):
        # copy file into output directory as is
        shutil.copyfile(os.path.join(src_dir, file), os.path.join(dest_dir, file))
