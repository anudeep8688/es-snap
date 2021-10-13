import requests
from requests_aws4auth import AWS4Auth

AWS_ACCESS_KEY_ID = str(sys.argv[1])
AWS_SECRET_ACCESS_KEY = str(sys.argv[2])
AWS_REGION = str(sys.argv[3])
HOST_URL = str(sys.argv[4])
PATH = str(sys.argv[5])
BUCKET_NAME = str(sys.argv[6])

region = 'AWS_REGION'
service = 'es'

awsauth = AWS4Auth(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, region, service)

host = 'HOST_URL'

path = 'PATH'
url = host + path

payload = {
  "type": "s3",
  "settings": {
    "bucket": "BUCKET_NAME",
    "region": "AWS_REGION",
    "role_arn": "arn:aws:iam::559346093313:user/anudeep"
  }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.text)
