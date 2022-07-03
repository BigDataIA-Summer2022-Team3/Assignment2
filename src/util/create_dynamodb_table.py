# # Adding the parent directory to the path.
import sys
sys.path.append('../')

import boto3
from service import config

ACKEY = config.ACKEY
SCKEY = config.SCKEY

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
                    'KeyType': 'S'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'timestamp',
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
        waiter.wait(TableName='ISS_locations')
        print("Table created")
        
    except ddb_exceptions.ResourceInUseException:
        print("Table exists")
