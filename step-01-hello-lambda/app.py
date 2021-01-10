#!/usr/bin/env python3

from aws_cdk import core

from step_01_hello_lambda.step_01_hello_lambda_stack import Step01HelloLambdaStack


app = core.App()
Step01HelloLambdaStack(app, "step-01-hello-lambda")

app.synth()
