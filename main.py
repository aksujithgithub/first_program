s3 = boto3.client('s3')
 # Upload a new file
data = open('testfile.txt', 'rb')
s3.upload_fileobj(data, 'my-bucket', 'testfile.txt')
 # Download the file from S3
s3.download_file('my-bucket', 'testfile.txt', 'downloaded-testfile.txt')
 # Check if the files are the same
with open('testfile.txt','rb') as f1, open('downloaded-testfile.txt','rb') as f2:
    if f1.read() != f2.read():
        print("The files are different")
    else:
        print("The files are the same")
