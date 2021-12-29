import json
import boto3
import os

s3 = boto3.resource('s3',
    aws_access_key_id=os.environ["ACCESS_ID"],
    aws_secret_access_key=os.environ["ACCESS_KEY"])

bucket_list = []
for bucket in s3.buckets.all():
    print(bucket.name)
    bucket_list.append(bucket.name)
