import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Find available (unattached) EBS volumes
    filters = [
        {'Name': 'status', 'Values': ['available']}
    ]
    
    volumes = ec2.describe_volumes(Filters=filters)
    
    deleted_volumes = []
    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        logger.info(f"Deleting unattached volume: {volume_id}")
        ec2.delete_volume(VolumeId=volume_id)
        deleted_volumes.append(volume_id)
        
    return {"deleted_volumes": deleted_volumes}
