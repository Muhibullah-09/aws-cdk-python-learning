
# Welcome to your CDK Python project!

[What is AWS CDK?](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
[AWS CDK in python](https://docs.aws.amazon.com/cdk/api/latest/python/index.html)

## Setup cdk with python (overview)


[Working with cdk with python](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)

## AWS CDK and Python : Deploy a s3 bucket

mkdir step-00-hello-cdk 

cd step-00-hello-cdk

cdk init app --language python

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
python3 -m venv .venv (use sudo in case of permission only for linux users)
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.


To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## app.py
```
install_requires = [
        "aws-cdk.core",
        "aws-cdk.aws_s3"
    ],
```

after adding service in app.py run:
```
pip install -r requirements.txt
```
## Another way to install services
```
pip install aws-cdk.aws_s3

```

then edit 

## step_00_hello_cdk_stack.py :
```
from aws_cdk import (
     core, 
     aws_s3 as s3
   )
   
class Step00HelloCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # The code that defines your stack goes here
        Bucket = s3.Bucket(self,'Python-cdk-step-00',
                  versioned=True,
                  bucket_name = 'step00-hello-cdk-python')//bucket_name is optional
```

At this point you can now synthesize the CloudFormation template for this code.

```
cdk synth (optional)

```

```
cdk deploy

```

```
cdk destroy (must)

```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
