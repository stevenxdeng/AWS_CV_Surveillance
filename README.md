# AWS_CV_Surveillance
Author: Hsien-wen "Steven" Deng\
This is a cloud-based Connected Vehicles (CV) Surveillance Application running in serverless architecture in Amazon Web Services (AWS). You can construct a cloud system using given AWS template and test as a client through a python script.

Prerequisite
1. Python 3.8\
   Download via: https://www.python.org/downloads/
2. Python IDE\
   Recommend Pyzo: https://pyzo.org/start.html
3. AWS account (AWS Educate may not be eligible due to lack of permission configuring CLI)\
   Login via: https://aws.amazon.com/
4. Set up a user in AWS
   1) Go to IAM
   2) Go to users
   3) Click "Add user"
   4) Copy the access key ID and secret access key after a new user is created\
For more details, please check: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html
5. AWS CLI\
   Download via: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
6. Configure AWS CLI
   1) Open cmd (Windows) or terminal (Linux)
   2) Type "aws configure"
   3) Configure your access key ID
   4) Configure your secret access key
   5) Configure region (default "us-east-1")
   6) Configure output (default "json")\
For more details, please check: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
   
Build-up
1. Import N_Template.json through AWS CloudFormation
2. Generate a Kinesis Stream service manually (due to limitation on Cloudformation, Kinesis Data Stream needed to be set manually)
   1) In AWS console, go to Kinesis
   2) Click "Create data stream"
   3) Configure stream name and set "Number of open shards" to be "1"
   4) Click "Create data stream"
3. Link Lambda and Kinesis
   1) In AWS console, go to Lambda
   2) In functions, choose the function imported from CloudFormation
   3) In Designer block, chooese "Add trigger"
   4) Choose "Kinesis" and select the data stream created (Make sure "Enable trigger" is selected)
   5) Click "Add"

Test
1. Open CV_Surveillance_Client.py by your Python IDE or text editor
2. Check if the names of resources matches your AWS (DynamoDB, Kinesis)
3. Run CV_Surveillabce_Client.py
