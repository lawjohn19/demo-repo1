import json
import boto3

def lambda_handler(event, context):
    
  ec2 = boto3.client('ec2')
  instance_ids = []
  response = ec2.stop_instances(InstanceIds=instance_ids)

  print("f'stopeed' instances: {response['instance is stopping']}" )