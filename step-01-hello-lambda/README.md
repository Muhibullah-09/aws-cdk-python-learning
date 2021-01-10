
[What is AWS Lambda ?](https://aws.amazon.com/lambda/)

[AWS Lambda construct with python](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda.html)

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

## Step 4
After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.
```
source .venv/bin/activate
```

## Step 5
One a Windows platform, you would use this:
```
.env\Scripts\activate.bat
```

## Step 6
Now that the virtual environment is activated, you can safely install the required python modules.
```
pip install -r requirements.txt
```
Once the virtualenv is activated, you can install the required dependencies.To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Step 7
Create a folder lambda at root directory and make index.py inside and add the handler code for your lambda in lambda/index.py
```
import json


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
    }
```
## Step 8
in setup.py :

```
    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-lambda"
    ],
```

## Step 9
after adding service in setup.py run:
```
pip install -r requirements.txt
```

## Step 10
then edit step_01_hello_lambda_stack.py :
```
from aws_cdk import (
    core,
    aws_lambda as _lambda,
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

## Step 11
```
cdk deploy
```

Now test the function in AWS Lambda Console (make sure you are in the correct region):
https://console.aws.amazon.com/lambda/home#/functions


## Next step is to add an API Gateway in front of our function. Install the dependency: 
## Step 12
in setup.py :
```
    install_requires=[
        "aws-cdk.core",
        "aws-cdk-aws_apigateway",
        "aws-cdk.aws-lambda"
    ],
```

## Step 13
after adding service in setup.py run:
```
pip install -r requirements.txt
```

## Step 14
then edit step_01_hello_lambda_stack.py:
```
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

        apigw.LambdaRestApi(
            self , 'LambdaEndpoint',
            handler = my_lambda
        )
```

At this point you can now synthesize the CloudFormation template for this code.

## Step 15
```
cdk synth (optional)
```


## Step 16
Deploy again

```
cdk deploy
```

## Step 17
Get the URL from the output and test it using curl or paste the url in browser:
```
https://xxxxxx.execute-api.us-east-2.amazonaws.com/prod/
```

## Step 18
```
cdk destroy (must)
```
## Step 19
If you want to deactivate the vartual enviroment write this command in the terminal of your project
```
deactivate
```

Enjoy!
