import uuid

import boto3


def create_s3_bucket_name():
    return str(uuid.uuid4())


def create_s3_bucket(s3_client, region_name):
    bucket_name = create_s3_bucket_name()
    bucket_response = s3_client.create_bucket(
        ACL='public-read-write',
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': current_region})
    return bucket_name, bucket_response


def bucket_csv_upload(s3_client, csv_file_path, file_name, bucket_name):
    s3_client.upload_file(Filename=csv_file_path, Bucket=bucket_name, Key=file_name, ExtraArgs={'ACL': 'public-read-write'})


if __name__ == "__main__":
    session = boto3.session.Session(profile_name='default')
    current_region = session.region_name
    s3_client = session.client('s3')
    bucket_name, bucket_response = create_s3_bucket(s3_client, current_region)
    print(bucket_response)
    bucket_csv_upload(s3_client, 'demo_csv.csv', 'demo_csv.csv', bucket_name)
