import os

import boto3
s3 = boto3.client('s3')

vidList = []
objects = s3.list_objects(Bucket='srvbcvideo', Marker='da2.mp4',Prefix='d')
print("objects: {}".format(len(objects['Contents'])))
for object in objects['Contents']:
  if(len(object['Key']) == 12):
    vidList.append(object['Key'])
print(vidList)

for vid in vidList:
  print('Decoding: {}'.format(vid))
  s3.download_file(
      "srvbcvideo", vid, vid
  )
  os.system("decipher transcribe -i {} --model large --language english".format(vid))
  #dir = os.getcwd()
  #transcribe(vid, language='english',model='large',output_dir='result',task='transcribe',subs=None)
  #os.chdir(dir)
  s3 = boto3.client('s3')
  with open("result/{}".format(vid.replace('mp4','srt')), "rb") as f:
    s3.upload_fileobj(f, "srvbcvideo", "srt/{}".format(vid.replace('mp4','srt')))

