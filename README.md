# AWS Cost Optimization Automation

A set of Python scripts utilizing the boto3 library designed to run as AWS Lambda functions. They find and delete unattached EBS volumes, release unused Elastic IPs, and stop non-production EC2 instances after hours.

## Tech Stack
- Python
- Boto3
- AWS Lambda
- Amazon EventBridge

## Deployment Instructions
1. Deploy the IAM roles using `template/iam_roles.yaml`.
2. Run `./build.sh` to package the Lambda functions.
3. Deploy the CloudFormation template `template/cloudformation.yaml` to create EventBridge rules.
4. Upload the packaged ZIP files to AWS Lambda.

## Usage
The Lambda functions will automatically trigger based on the EventBridge schedules.
