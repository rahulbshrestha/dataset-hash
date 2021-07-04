
import boto3, logging, botocore, os
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_directory(path, bucket):
    for root,dirs,files in os.walk(path):
        for file in files:
            upload_file(os.path.join(root,file),bucket,file)

if __name__ == '__main__':
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('hub-2.0-tests')

    exists = True
    try:
        s3.meta.client.head_bucket(Bucket='hub-2.0-tests')
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = e.response['Error']['Code']
        if error_code == '404':
            exists = False

    upload_directory('../data/very-large-dataset-1', bucket)