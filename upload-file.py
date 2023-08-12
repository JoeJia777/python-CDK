import boto3

s3 = boto3.client("s3")

response = s3.upload_file(r'C:\Users\Admin\Desktop\sample.txt', 'bydyangwang.com', 'sample.txt')
