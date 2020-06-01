# Disclaimer: this code is not mine, it is sample code taken from the AWS Documenation: https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains-snapshots.html

host = '' # include https:// and trailing /
path = '_snapshot/my-snapshot-repo/my-snapshot'
url = host + path

r = requests.put(url, auth=awsauth)

print(r.text)

