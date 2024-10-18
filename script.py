import os
from faker import Faker
from time import sleep

# Configuration
MINIO_ENDPOINT = "https://minio.cloudflow.ir"  # Change to your MinIO server endpoint
ACCESS_KEY = "siavash"          # Replace with your MinIO access key
SECRET_KEY = "4YJ97rJviWDPJ2mTEGxsXT4e4kHRmh"      # Replace with your MinIO secret key
BUCKET_NAME = "backup"  # Replace with your MinIO bucket name
NUM_FILES = 10            # Number of fake files to generate

# Initialize Faker and MinIO client
fake = Faker()

try:
    os.system(f"mc alias set client {MINIO_ENDPOINT} {ACCESS_KEY} {SECRET_KEY}")
except Exception as error:
    print(error)

# Generate fake files and upload to MinIO
for i in range(NUM_FILES):
    # Generate fake content
    file_name = f"fake_file_{i + 1}.txt"
    content = fake.text(max_nb_chars=200)  # Generate random text content

    # Save the content to a local file
    with open(file_name, 'w') as f:
        f.write(content)

    # Upload the file to MinIO
    try:
        # minio_client.fput_object(BUCKET_NAME, file_name, file_name)
        os.system(f"mc cp {file_name} client/{BUCKET_NAME}")
        print(f"Uploaded {file_name} to bucket {BUCKET_NAME}")
    except Exception as e:
        print(f"Error uploading {file_name}: {e}")

    # Optionally, remove the local file after uploading
    os.remove(file_name)
    sleep(3)

print("All files uploaded successfully.")
