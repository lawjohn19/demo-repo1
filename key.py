import boto3

ec2 = boto3.client('ec2')

key = 'numkey1'

response = ec2.create_key_pair(
    KeyName=key,
)

print(response)