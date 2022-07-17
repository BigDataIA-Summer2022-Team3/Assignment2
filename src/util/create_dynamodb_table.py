# # Adding the parent directory to the path.
import sys, os
sys.path.append(os.path.abspath('../service'))
print(os.getcwd())

import boto3
# from config 
from config import funct

ACKEY, SCKEY = funct()
#  = config.SCKEY

client = boto3.client(
    'dynamodb',
    aws_access_key_id= ACKEY,
    aws_secret_access_key= SCKEY,
    )

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=ACKEY,
    aws_secret_access_key=SCKEY,
    )
ddb_exceptions = client.exceptions

def create_dynamodb_table():
    try:
        table = client.create_table(
            TableName='damg-users',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'password',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'last_login',
                    "AttributeType": 'N'
                },
                {
                    'AttributeName': 'isAdmin',
                    'AttributeType': 'N'
                }
        
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        print("Creating table")
        waiter = client.get_waiter('table_exists')
        waiter.wait(TableName='damg-users')
        print("Table created")
        
    except ddb_exceptions.ResourceInUseException:
        print("Table exists")

create_dynamodb_table()