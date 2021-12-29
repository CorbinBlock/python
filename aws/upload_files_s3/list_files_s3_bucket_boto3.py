import json
import boto3
import os

s3 = boto3.client('s3',
    aws_access_key_id=os.environ["ACCESS_ID"],
    aws_secret_access_key=os.environ["ACCESS_KEY"])

def get_s3_keys(bucket):
    """Get a list of keys in an S3 bucket."""
    keys = []
    resp = s3.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
        keys.append(obj['Key'])
    return keys

key_list = get_s3_keys("s3-bucket-cblock")

# key_list_sorted = key_list.sort()

print(key_list)