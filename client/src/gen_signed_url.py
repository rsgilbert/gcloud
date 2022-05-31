# Generate signed url 
import datetime 
from google.cloud import storage 


def generate_upload_signed_url_v4(bucket_name: str, blob_name: str):
    """"
    Generatte a v4 signed url for uploading a blob using HTTP PUT
    This method requires a service account key file.
    You specify the service account using: export GOOGLE_APPLICATION_CREDENTIALS=./my-service-account-key.json
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    url = blob.generate_signed_url(
        version="v4",
        # URL will be valid for 15 minutes
        expiration=datetime.timedelta(minutes=15),
        # Allow PUT requests using this URL
        method="PUT",
        content_type="application/octet-stream"
    )

    return url

# url = generate_upload_signed_url_v4(bucket_name, 'public/pie-pie.txt')
# print(url)


def generate_download_url_v4(bucket_name: str, blob_name: str):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    url = blob.generate_signed_url(
        version="v4",
        expiration=datetime.timedelta(minutes=10),
        method="GET",
        content_type="application/octet-stream"
    )
    return url

bucket_name = 'rsgilbert-new-bkt-1' 


url = generate_download_url_v4(bucket_name, 'public/pie-pie.txt')
print(url)