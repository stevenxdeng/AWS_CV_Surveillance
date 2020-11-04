# AWS_CV_Surveillance
Author: Hsien-wen "Steven" Deng\
This is a cloud-based Connected Vehicles (CV) Surveillance Application running in serverless architecture in Amazon Web Services (AWS). You can construct a cloud system using given AWS template and test as a client through a python script.

**Prerequisite**
1. Python 3.8\
   Download via: https://www.python.org/downloads/
2. Python IDE\
   Recommend Pyzo: https://pyzo.org/start.html
3. AWS Account (AWS Educate may not be eligible due to lack of permission configuring CLI)\
   Login via: https://aws.amazon.com/
4. AWS User Credential 
   1) From AWS Console go to IAM
   2) Select to "users"
   3) Click "Add user"
   4) Select "Programmatic access" for the AWS access type to generate an access key ID and secret access key for use with the AWS APi, CLI, SDK, and other development tools
   5) Select the created user and select "Security Credentials" tab
   6) Click "Create access key" and copy the access key ID and secret access key after a new user is created\
*For more details, please check: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html*
5. AWS CLI
   1) Download AWS CLI and install\
Download via: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html 
   2) Open cmd (Windows) or terminal (Linux) and type "aws configure"
   3) Input access key ID and secret access key copied from 4
   4) Configure region (default "us-east-1")
   5) Configure output (default "json")\
*For more details, please check: [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)*
   
**Build-up Application** 
1. From AWS Console Go to "CloudFormation"
2. Click "Create Stack"
3. Select "Upload a template file" and upload "CV_Surveillance_Template.json"
4. Input a name and click "Create stack"

**Test Application**\
    Run CV_Surveillance_Client.py: python CV_Surveillance_Client.py\
    *If errors show up, check names of resources (DynamoDB, Kinesis)*
