from dotenv import load_dotenv
import boto3
import uuid
import os

load_dotenv()

class S3ImgUploader:
    def __init__(self, file):
        self.file = file

    def upload(self):
        s3_client = boto3.client(
            's3',
            aws_access_key_id     = os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
        )
        url = 'img'+'/'+uuid.uuid1().hex
        
        s3_client.upload_fileobj(
            self.file, 
            os.environ.get("AWS_STORAGE_BUCKET_NAME"), 
            url, 
            ExtraArgs={
                "ContentType": self.file.content_type
            }
        )
        return url