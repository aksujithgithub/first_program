import boto3
from moto import mock_s3
import pytest


@mock_s3
def test_upload_file_to_s3():
    # Create an S3 client
    s3 = boto3.client('s3')
    # Create a bucket in default region
    s3.create_bucket(Bucket='mybuc'
                            'ket')
    # Upload a file to the bucket
    filename = 'example.txt'
    file_contents = 'This is an example.'
    response = s3.put_object(Bucket='mybucket', Key=filename, Body=file_contents)
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200
