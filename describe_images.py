import pprint

import boto3

connection = boto3.client('ec2' , region_name='us-east-1')
response = connection.describe_images(ImageIds=['ami-00768769'])
for r in range(1):
    if(response['Images'][r]['BlockDeviceMappings'][0]):
        pprint.pprint(response['Images'][r]['BlockDeviceMappings'][0])
    else:
        print 'adsa'