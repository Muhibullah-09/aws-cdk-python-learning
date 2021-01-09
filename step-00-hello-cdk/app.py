#!/usr/bin/env python3

from aws_cdk import core

from step_00_hello_cdk.step_00_hello_cdk_stack import Step00HelloCdkStack


app = core.App()
Step00HelloCdkStack(app, "step-00-hello-cdk")

app.synth()
