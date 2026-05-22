import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    addresses = ec2.describe_addresses()
    
    released_eips = []
    for address in addresses['Addresses']:
        if 'InstanceId' not in address and 'NetworkInterfaceId' not in address:
            allocation_id = address['AllocationId']
            public_ip = address['PublicIp']
            logger.info(f"Releasing unused EIP: {public_ip} ({allocation_id})")
            ec2.release_address(AllocationId=allocation_id)
            released_eips.append(public_ip)
            
    return {"released_eips": released_eips}
