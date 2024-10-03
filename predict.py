import boto3
import json
import boto3.session
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split


global app_name
global region

app_name='model-application'
region='us-east-1'


def check_status(app_name):
    sage_client=boto3.client('sagemaker',region_name=region)
    endpoint_description=sage_client.describe_endpoint(EndpointName=app_name)
    endpoint_status=endpoint_description['EndpointStatus']
    return endpoint_status


def query_endpoint(app_name,input_json):
    client=boto3.session.Session().client('sagemaker-runtime',region)
    response=client.invoke_endpoint(EndpointName=app_name,
                                   ContentType='application/json',
                                   Body=input_json)
    preds=response['Body'].read().decode('ascii')
    preds=json.loads(preds)
    print('Received response:{}'.format(preds))
    return preds

print(f'Application status is {check_status(app_name)}')

wine_data=datasets.load_wine()
df=pd.DataFrame(wine_data['data'],columns=wine_data['feature_names'])
x=df
y=wine_data.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

query_input=pd.DataFrame(x_train).iloc[[12]].to_json(orient='split')
print(query_input)
predictions=query_endpoint(app_name=app_name, input_json=query_input)