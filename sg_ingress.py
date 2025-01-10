import boto3

ec2 = boto3.client('ec2')

group_id ='sg-0430f7b19072bdab5'

response = ec2.authorize_security_group_ingress(
    GroupId=group_id,
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    
                },
            ],
            'ToPort': 22,
        },
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    
                },
            ],
            'ToPort': 80,
        },
    ],
)

print(response)
