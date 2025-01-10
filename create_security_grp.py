import boto3

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='Allows HTTP and SSH Traffic',
    GroupName='My-boto-grp',
    VpcId='vpc-0a3f97fba0b6d09e1',
)

print(response)