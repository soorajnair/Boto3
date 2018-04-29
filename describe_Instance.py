import boto3

connection=boto3.client('ec2',region_name='us-east-1')
response=connection.describe_instances()
for r in range(len(response['Reservations'])):
    print response['Reservations'][r]['Instances'][0]['InstanceId'] + ' , '+ response['Reservations'][r]['Instances'][0]['BlockDeviceMappings'][0]['Ebs']['VolumeId']