import boto3

ec2 = boto3.client('ec2')


def start_ec2(event, context):
    ec2_instances = get_all_ec2_ids()
    response = ec2.start_instances(
        InstanceIds=ec2_instances,
        DryRun=False
    )
    return response

def stop_ec2(event, context):
    ec2_instances = get_all_ec2_ids()
    response = ec2.stop_instances(
        InstanceIds=ec2_instances,
        DryRun=False
    )
    return response

def get_all_ec2_ids():
    response = ec2.describe_instances(DryRun=False)
    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append(instance["InstanceId"])
    return instances