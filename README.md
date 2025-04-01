# publish_total_instances
Lambda function that counts all running instances in an AWS environment, publish the value to Cloudwatch as a custom metric called "TotalInstances"
I used this code to monitor total running instances via Grafana and Cloudwatch datasource.

My solution to run this lambda is to connect it via AWS Eventbridge and trigger the lambda every 30 minutes.
