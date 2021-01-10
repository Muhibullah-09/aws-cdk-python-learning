
# Welcome to your CDK Python project!
## Step 1
```
mkdir step-01-hello-lambda 
```

## Step 2
```
cd  step-01-hello-lambda
```

## Step 3
```
cdk init app --language python
```

# Activating the Virtualenv
The init script we ran in the last step created a bunch of code to help get us started but it also created a virtual environment within our directory. If you haven’t used virtualenv before, you can find out more here but the bottom line is that they allow you have a self-contained, isolated environment to run Python and install arbitrary packages without polluting your system Python.

## [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html#virtual-environments-and-packages)




## Step 3
```
To manually create a virtualenv on MacOS and Linux:

python3 -m venv .venv (use sudo in case of permission only for linux users)
```


```
If you are a Windows platform, you would activate the virtualenv like this:

% .venv\Scripts\activate.bat
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

## Step 4
```
source .venv/bin/activate
```

## One a Windows platform, you would use this:

## Step 5
```
.env\Scripts\activate.bat
```

## Step 6
```
Now that the virtual environment is activated, you can safely install the required python modules.

pip install -r requirements.txt
```

Once the virtualenv is activated, you can install the required dependencies.To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Step 7
```
in setup.py :

    install_requires=[
        "aws-cdk.core",
        "aws-cdk-aws_apigateway",
        "aws-cdk.aws-lambda"
    ],
```

## Step 8
```
after adding service in setup.py run:

pip install -r requirements.txt
```

## Step 9
```
then edit step_01_hello_lambda_stack.py :

from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)


class Step01HelloLambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here

        my_lambda = _lambda.Function(
            self, 'HelloLambdaHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='index.handler',
        )

```

At this point you can now synthesize the CloudFormation template for this code.

## Step 10
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

Enjoy!
This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
