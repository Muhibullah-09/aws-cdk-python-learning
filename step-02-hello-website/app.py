#!/usr/bin/env python3

from aws_cdk import core

from step_02_hello_website.step_02_hello_website_stack import Step02HelloWebsiteStack


app = core.App()
Step02HelloWebsiteStack(app, "step-02-hello-website")

app.synth()
