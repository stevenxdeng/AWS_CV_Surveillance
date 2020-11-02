#!/usr/bin/env python

import boto3
import botocore
import json
import math
from decimal import *
import csv
import os
import random
import time

#Configuration of dynamoDB Tables
config = botocore.config.Config(max_pool_connections=100)
dynamodb = boto3.resource('dynamodb',config=config)
Upload_Table = dynamodb.Table('Vehicle_Trajectory_Database')
Download_Table = dynamodb.Table('Cloud_Feedback_Database')

#Your Kinesis name, please check before test
my_stream = 'CV_Surveillance_Stream'
kinesis_client = boto3.client('kinesis',region_name='us-east-1')

#Upload function
def Vehicle_State_upload(Table, ID, speed):
    Table.put_item(
        Item={
            'ID':ID,
            'speed': Decimal(str(speed))
        }
    )

#Download function
def Cloud_Feedback_download(Table, ID):
    response = Table.get_item(Key={'Platoon':ID})
    ave = float(response['Item']['Average'])
    pt = int(response['Item']['Process'])
    print('Average is ', ave, ' m/s')
    print('processs time is ', pt, ' ms')

#Kinesis Stream function
def kinesis_upload(stream, data):
    response = kinesis_client.put_record(
        StreamName=stream,
        Data=data.encode(),
        PartitionKey='0',
        ExplicitHashKey='0',
        SequenceNumberForOrdering='0'
    )
    return


for i in range(10):
    vspeed = round(random.uniform(6.0,20.0),2)
    Vehicle_State_upload(Upload_Table,str(i),vspeed)
    print('Upload Done')

kinesis_upload(my_stream,'0')
time.sleep(1)
Cloud_Feedback_download(Download_Table, '1')


