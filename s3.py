import boto3
import os
import time

# Espera LocalStack inicializar (ajuste opcional)
time.sleep(5)

s3 = boto3.client(
    "s3",
    endpoint_url="http://localstack:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

bucket_name = "meu-bucket-local"
file_name = "exemplo.txt"

s3.create_bucket(Bucket=bucket_name)

with open(file_name, "w") as f:
    f.write("Conteúdo de exemplo")

s3.upload_file(file_name, bucket_name, file_name)

print("Objetos no bucket:")
for obj in s3.list_objects(Bucket=bucket_name).get("Contents", []):
    print(" -", obj["Key"])
