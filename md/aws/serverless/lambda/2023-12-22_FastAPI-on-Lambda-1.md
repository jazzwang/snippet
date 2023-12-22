# 2023-12-22

## Goal

* ask ChatGPT for instructions. exam the correctness.
```
could you give me a step-to-step command line instruction for the following requirements?

Requirements:
1. use AWS Lambda with python container image
2. write a python program using FastApi helloworld example
3. deploy python program to AWS Lambda as a container instance
4. enable external URL for testing functionality
```
* https://chat.openai.com/share/c8f12225-fc0d-4118-8770-c80b42236d82

## Environment

* test on https://ap-northeast-1.console.aws.amazon.com/cloudshell/home
* ( 2023-12-22 08:44:49 )
```bash
[cloudshell-user@ip-10-130-62-101 ~]$ ls -al
total 32
drwxrwxrwx. 4 cloudshell-user cloudshell-user 4096 Dec 22 00:32 .
drwxr-xr-x. 3 root            root            4096 Dec 22 00:32 ..
-rw-r--r--. 1 cloudshell-user cloudshell-user   18 Dec 22 00:32 .bash_logout
-rw-r--r--. 1 cloudshell-user cloudshell-user  141 Dec 22 00:32 .bash_profile
-rw-r--r--. 1 cloudshell-user cloudshell-user  539 Dec 22 00:32 .bashrc
drwxr-xr-x. 3 cloudshell-user cloudshell-user 4096 Dec 22 00:32 .config
drwxr-xr-x. 3 cloudshell-user cloudshell-user 4096 Dec 22 00:32 .local
-rw-r--r--. 1 cloudshell-user cloudshell-user  777 Dec 22 00:32 .zshrc
[cloudshell-user@ip-10-130-62-101 ~]$ mkdir my_lambda_project
[cloudshell-user@ip-10-130-62-101 ~]$ cd my_lambda_project
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ cat > Dockerfile << EOF
> FROM public.ecr.aws/lambda/python:3.8
> 
> COPY app.py \${LAMBDA_TASK_ROOT}
> 
> CMD ["app.handler"]
> EOF
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ pip install fastapi[all]
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ cat > app.py << EOF
> from fastapi import FastAPI
> 
> app = FastAPI()
> 
> @app.get("/")
> def read_root():
>     return {"Hello": "World"}
> EOF
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ sudo dockerd &     # https://stackoverflow.com/a/76041922
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ sudo usermod -aG docker $USER
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ sudo chmod 766 /var/run/docker.sock 
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ docker build -t my_lambda_function .
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ aws ecr create-repository --repository-name jazz-ecr
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ export ecr_uri="********.dkr.ecr.ap-northeast-1.amazonaws.com/jazz-ecr"
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ aws ecr get-login-password | docker login --username AWS --password-stdin $ecr_uri 
WARNING! Your password will be stored unencrypted in /home/cloudshell-user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ docker tag my_lambda_function:latest ${ecr_uri}:latest
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ docker push ${ecr_uri}:latest
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ cat > trust-policy.json << EOF
> {
>   "Version": "2012-10-17",
>   "Statement": [
>     {
>       "Effect": "Allow",
>       "Principal": {
>         "Service": "lambda.amazonaws.com"
>       },
>       "Action": "sts:AssumeRole"
>     }
>   ]
> }
> EOF
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ # Create IAM Role
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ aws iam create-role \
>     --role-name LambdaExecutionRole \
>     --assume-role-policy-document file://trust-policy.json
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ # Attach AWSLambdaBasicExecutionRole policy to the IAM Role
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ aws iam attach-role-policy \
>     --role-name LambdaExecutionRole \
>     --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ aws iam attach-role-policy \
>     --role-name LambdaExecutionRole \
>     --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ aws lambda create-function \
>     --function-name MyLambdaFunction \
>     --package-type Image \
>     --code ImageUri=${ecr_uri}:latest \
>     --role arn:aws:iam::817023017819:role/LambdaExecutionRole \
>     --memory-size 256 \
>     --timeout 30
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ aws lambda invoke \
>     --function-name MyLambdaFunction \
>     --cli-binary-format raw-in-base64-out \
>     --payload '{}' \
>     output.json
{
    "StatusCode": 200,
    "FunctionError": "Unhandled",
    "ExecutedVersion": "$LATEST"
}
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ pip install jq
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ cat output.json | jq .
{
  "errorMessage": "Unable to import module 'app': No module named 'fastapi'",
  "errorType": "Runtime.ImportModuleError",
  "stackTrace": []
}
```
* ( 2023-12-22 09:44:30 )
    * it means that I need to install `fastapi` within Dockerfile
```bash
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ cat > Dockerfile << EOF
> FROM public.ecr.aws/lambda/python:3.8
> 
> RUN pip install fastapi[all]
> 
> COPY app.py \${LAMBDA_TASK_ROOT}
> 
> CMD ["app.handler"]
> EOF
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ docker build -t my_lambda_function .
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ docker tag my_lambda_function:latest ${ecr_uri}:latest
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ aws lambda update-function-code \
>     --function-name MyLambdaFunction \
>     --image-uri ${ecr_uri}:latest
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ aws lambda invoke \
>     --function-name MyLambdaFunction \
>     --cli-binary-format raw-in-base64-out \
>     --payload '{}' \
>     output.json

{
    "StatusCode": 200,
    "FunctionError": "Unhandled",
    "ExecutedVersion": "$LATEST"
}
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ cat output.json | jq .
{
  "errorMessage": "Handler 'handler' missing on module 'app'",
  "errorType": "Runtime.HandlerNotFound",
  "stackTrace": []
}
```
* ( 2023-12-22 10:15:45 )
    - it seems that we need a handler for FastAPI + AWS Lambda
* Reference:
    - https://fanchenbao.medium.com/api-service-with-fastapi-aws-lambda-api-gateway-and-make-it-work-c20edcf77bff
    - https://github.com/FanchenBao/fastapi_lambda_api-gateway_sample/
    - https://blog.searce.com/fastapi-container-app-deployment-using-aws-lambda-and-api-gateway-6721904531d0
    - https://www.deadbear.io/simple-serverless-fastapi-with-aws-lambda/
    - https://ademoverflow.com/blog/tutorial-fastapi-aws-lambda-serverless/
* All of those reference use the same solution - mangum.io "AWS Lambda support for ASGI applications"
* ( 2023-12-22 10:29:00 )
    - cleanup 
```
[cloudshell-user@ip-10-130-62-101 my_lambda_project]$ aws lambda delete-function --function-name MyLambdaFunction
```