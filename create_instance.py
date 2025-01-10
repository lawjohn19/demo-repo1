import boto3

ec2 = boto3.client('ec2')

ami_id = 'ami-0ca9fb66e076a6e32'
key = 'key1'
sg_id = 'sg-0ef556ccc8a9bf540'


response = ec2.run_instances(
   ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        sg_id,
    ]    
    
    
)
       

print(response)