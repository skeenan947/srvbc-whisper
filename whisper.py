import os
import sys

import boto3
s3 = boto3.client('s3')

vidList = [sys.argv[1]]

for vid in vidList:
  print('Decoding: {}'.format(vid))
  s3.download_file(
      "srvbcvideo", vid, vid
  )
  os.system("decipher transcribe -i {} --model large --language english".format(vid))
  s3 = boto3.client('s3')
  with open("result/{}".format(vid.replace('mp4','srt')), "rb") as f:
    s3.upload_fileobj(f, "srvbcvideo", "srt/{}".format(vid.replace('mp4','srt')))

