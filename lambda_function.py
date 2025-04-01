import boto3
import botocore.exceptions
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    autoscaling_client = boto3.client('autoscaling')
    cloudwatch_client = boto3.client('cloudwatch')

    try:
        paginator = autoscaling_client.get_paginator('describe_auto_scaling_groups')
        page_iterator = paginator.paginate()

        total_running_instances = 0

        for page in page_iterator:
            for asg in page['AutoScalingGroups']:
                asg_name = asg['AutoScalingGroupName']
                running_instances = [
                    instance for instance in asg['Instances']
                    if instance['LifecycleState'] == 'InService'
                ]
                instances_in_asg = len(running_instances)
                total_running_instances += instances_in_asg

        logger.info(f"Total running instances in ASGs: {total_running_instances}")

        response = cloudwatch_client.put_metric_data(
            Namespace='Custom/TotalInstances',
            MetricData=[
                {
                    'MetricName': 'TotalRunningInstances',
                    'Unit': 'Count',
                    'Value': total_running_instances
                },
            ]
        )

        logger.info("Custom metric published to CloudWatch.")

    except botocore.exceptions.ClientError as error:
        logger.error(f"An error occurred: {error}")
        raise error
