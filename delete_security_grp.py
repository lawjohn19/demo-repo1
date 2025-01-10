import boto3

ec2 = boto3.client('ec2')

sg_id = 'sg-0430f7b19072bdab5'

response = ec2.delete_security_group(
    GroupId=sg_id
)

print(response)