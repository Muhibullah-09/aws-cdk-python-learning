[What is AWS CDK?](https://docs.aws.amazon.com/cdk/latest/guide/home.html)

[AWS CDK in python](https://docs.aws.amazon.com/cdk/api/latest/python/index.html)

Setup cdk with python (overview)

[Working with cdk with python](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)

# Activating the Virtualenv
The init script we ran in the last step created a bunch of code to help get us started but it also created a virtual environment within our directory. If you haven’t used virtualenv before, you can find out more here but the bottom line is that they allow you have a self-contained, isolated environment to run Python and install arbitrary packages without polluting your system Python.

[Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html#virtual-environments-and-packages)
[Understand the project structure of cdk with python](https://cdkworkshop.com/30-python/20-create-project/300-structure.html)
## Step 1
```
mkdir step-00-hello-cdk 
```

## Step 2
```
cd step-00-hello-cdk
```

## Step 3
```
cdk init app --language python
```

## Step 3
To manually create a virtualenv on MacOS and Linux:
```
python3 -m venv .venv
```
(use sudo in case of permission only for linux users)

If you are a Windows platform, you would activate the virtualenv like this:
```
% .venv\Scripts\activate.bat
```

## Step 4
After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.
```
source .venv/bin/activate
```

## Step 5
On a Windows platform, you would use this:
```
.env\Scripts\activate.bat
```

## Step 6
Now that the virtual environment is activated, you can safely install the required python modules.
```
pip install -r requirements.txt
```

## Step 7
Once the virtualenv is activated, you can install the required dependencies.To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

in setup.py :
```
install_requires = [
        "aws-cdk.core",
        "aws-cdk.aws_s3"
    ],
```

## Step 8
after adding service in setup.py run:
```
pip install -r requirements.txt
```

## Step 9
then edit step_00_hello_cdk_stack.py :
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

## Step 10
At this point you can now synthesize the CloudFormation template for this code.
```
cdk synth (optional)
```

## Step 11
```
cdk deploy
```
## Step 12
```
cdk destroy (must)
```
## Step 13
If you want to deactivate the vartual enviroment write this command in the terminal of your project
```
deactivate
```

Enjoy!
