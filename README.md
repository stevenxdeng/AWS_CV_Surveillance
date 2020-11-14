# AWS CV Surveillance
Author: ***Hsien-wen "Steven" Deng***\
This is a cloud-based Connected Vehicles (CV) Surveillance Application running in serverless architecture in Amazon Web Services (AWS). 
**Template**: The template includes a system of AWS services allows you to establish this application.\
**Test Program**: The test program is a Python script running in the client to test the availability of your cloud application. The program first simulates 10 vehicles sending Basic Safety Messages (ID, speed) to the Vehicle_Trajectory_Database. Then, the program simulates a Roadside Unit (RSU) sending a Kinesis Data Stream to trigger AWS Lambda. Last, the program requests results from Cloud_Feedback_Database.

## Prerequisite
1. [Python 3.8](https://www.python.org/downloads/)
2. Python IDE, recommend [Pyzo](https://pyzo.org/start.html)
3. [AWS Account](https://aws.amazon.com/)\
   *AWS Educate may not be eligible due to lack of permission configuring CLI*
4. AWS User Credential 
   1) From AWS Console go to **IAM**
   2) Select to **users**
   3) Click **Add user**
   4) Select **Programmatic access** for the AWS access type to generate an access key ID and secret access key for use with the AWS API, CLI, SDK, and other development tools
   5) Select the created user and select **Security Credentials** tab
   6) Click **Create access key** and copy the access key ID and secret access key after a new user is created\
*For more details, please check: [AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)*
5. AWS CLI
   1) Download [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.htm) and install 
   2) Open CMD (Windows) or Terminal (Linux): `aws configure`
   3) Input **access key ID** and **secret access key** copied from 4
   4) Configure region (default "us-east-1")
   5) Configure output (default "json")\
*For more details, please check: [AWS CLI Configuration Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)*
   
## Build-up Application
1. From AWS Console go to **CloudFormation**
2. Click **Create stack**
3. Select **Upload a template file** and upload *CV_Surveillance_Template.json*
4. Input a name and click **Create stack**

## Test Application
1. Install boto3: `python -m pip install boto3`
2. Run *CV_Surveillance_Client.py*: `python CV_Surveillance_Client.py`\
*If errors show up, check names of resources (DynamoDB, Kinesis)*

## Destroy Application
After deletion of CloudFormation, resources are still in usage, **deletions** of these resources are needed to reduce cost impacts:\
**DynamoDB**\
**Kinesis Data Stream**
