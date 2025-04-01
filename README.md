# publish_total_instances
Lambda function that counts all running instances in an AWS environment, publish the value to Cloudwatch as a custom metric called "TotalInstances"
I used this code to monitor total running instances via Grafana and Cloudwatch datasource.

My solution to trigger this lambda was to connect it via Amazon Eventbridge to trigger every 30 minutes.
