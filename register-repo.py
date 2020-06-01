# Disclaimer: this code is not mine, it is sample code taken from the AWS Documenation: https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains-snapshots.html

# Review each comment in this script and replace your appropriate values

import boto3
import requests
from requests_aws4auth import AWS4Auth

host = '' # include https:// and trailing /
region = '' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Register repository

path = '_snapshot/my-snapshot-repo-name' # the Elasticsearch API endpoint
url = host + path

payload = {
          "type": "s3",
            "settings": {
                    "bucket": "s3-bucket-name",
                        # "endpoint": "s3.amazonaws.com", # for us-east-1
                            "region": "us-west-1", # for all other regions
                                "role_arn": "arn:aws:iam::123456789012:role/TheSnapshotRole"
                                  }
            }

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)
