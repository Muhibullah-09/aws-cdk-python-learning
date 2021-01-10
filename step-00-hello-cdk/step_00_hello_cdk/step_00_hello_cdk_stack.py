from aws_cdk import (core, aws_s3 as s3)

class Step00HelloCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        # Here we define our first bucket
        Bucket = s3.Bucket(self,'Python-cdk-step-00',versioned=True,bucket_name = 'simple s3 bucket')
