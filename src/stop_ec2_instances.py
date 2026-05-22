import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Find instances tagged with Environment: Non-Production that are running
    filters = [
        {'Name': 'tag:Environment', 'Values': ['Non-Production', 'Dev', 'Test']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]
    
    instances = ec2.describe_instances(Filters=filters)
    
    instance_ids = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
            
    if instance_ids:
        logger.info(f"Stopping instances: {instance_ids}")
        ec2.stop_instances(InstanceIds=instance_ids)
        return {"stopped_instances": instance_ids}
    else:
        logger.info("No instances to stop.")
        return {"stopped_instances": []}
