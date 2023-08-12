import boto3

s3 = boto3.client("s3")

response = s3.download_file( 
'bydyangwang.com','sample.txt',r'C:\Users\Admin\Desktop\s3download\download.txt'
)