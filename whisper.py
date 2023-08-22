import os
import sys

import boto3
s3 = boto3.client('s3')

vidList = sys.argv[1].split(',')

for vid in vidList:
  vid="{}.mp4".format(vid)
  print('Decoding: {}'.format(vid))
  s3.download_file(
      "srvbcvideo", vid, vid
  )
  os.system("decipher transcribe -i {} --model large --language english".format(vid))
