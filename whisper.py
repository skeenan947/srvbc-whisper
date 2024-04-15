import os
import sys

import boto3
s3 = boto3.client('s3')

vidList = sys.argv[1].split(',')

for title in vidList:
  wav="{}.wav".format(title)
  vid="{}.mp4".format(title)
  print('Decoding: {}'.format(vid))
  s3.download_file(
      "srvbcvideo", vid, vid
  )
  os.system("ffmpeg -i {} {}".format(vid, wav))
  os.system("whisperx {} --model large-v2 -f srt --compute_type int8 --language en".format(vid))
