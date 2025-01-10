import boto3

ec2 = boto3.client('ec2')

select = input('What would you like to do with EC2 instance:  Start,  Stop,  Terminate ')

response = ec2.start.stop.terminate_instances(
    InstanceIds=[]
        )
if select == ('Start'):
    print(response, 'instance started successfully' ['InstanceIds'])
if select == ('Stop'):
   print(response, 'instance stopped successfully' ['InstanceIds'])
if select == ('Terminate'):
   print(response, 'instance terminated successfully' ['InstanceIds'])   
    

else: 
 print(response)
