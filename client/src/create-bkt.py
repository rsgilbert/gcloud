from google.cloud import storage

storage_client = storage.Client()

bucket_name = "rsgilbert-new-bkt-6"

bucket = storage_client.create_bucket(bucket_name)

print(f'Bucket {bucket.name} is created')
print(bucket)

