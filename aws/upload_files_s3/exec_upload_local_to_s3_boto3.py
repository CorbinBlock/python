import boto3
import os
from upload_local_to_s3_boto3 import *

s3 = boto3.client('s3',
    aws_access_key_id=os.environ["ACCESS_ID"],
    aws_secret_access_key=os.environ["ACCESS_KEY"])
with open("/mnt/c/tmp/debian.tar.gz", mode = "rb") as f:
    s3.upload_fileobj(f, "s3-bucket-cblock", "debian.tar.gz",
    Callback=ProgressPercentage('/mnt/c/tmp/debian.tar.gz'))
print("\r")