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