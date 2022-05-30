from google.cloud import storage

def upload_blob(bucket_name: str, source_file_name: str, destination_blob_name: str):
    """
    bucket_name: Bucket name 
    source_file_name: Path to file to upload 
    destination_blob_name: id of google cloud storage object
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}")



bucket_name = 'rsgilbert-new-bkt-1'
# upload_blob(bucket_name, '../.gitignore', 'my-gitignore.txt')

def upload_blob_from_memory(bucket_name: str, contents: str, destination_blob_name: str):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(contents)

upload_blob_from_memory(bucket_name, "Hey darling. I love you", "msg.txt")
