import boto3

instances_id = 'i-09e9d0e4c7b955dba'

def start_instances(client, instances_id):
    response = ec2.start_instances(
    InstanceIds=[
        instances_id
    ],
)

    
def stop_instances(client, instances_id):
    response = client.stop_instances(
    InstanceIds=[
        instances_id
    ],
 )
    
def terminate_instances(client, instances_id):
    response = client.terminate_instances(
    InstanceIds=[
        instances_id
    ],
 )    
    
if __name__ == '__main__':
    instances_id = 'i-09e9d0e4c7b955dba'
    
    ec2 = boto3.client('ec2')
    terminate_instances(ec2, instances_id)
    

     


      
