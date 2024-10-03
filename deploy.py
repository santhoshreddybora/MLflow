import mlflow.sagemaker as mfs


exp_id='983826555450263583'
run_id='6b189eed983b42128c5351c4448deffe' 
region='us-east-1'
## for aws id execute this command in gitbash aws sts get-caller-identity --query Account --output text
aws_id= '960055660452'
arn= 'arn:aws:iam::960055660452:role/aws-sagemaker-for-deploymlmodel'
app_name='model-application'
model_uri=f"mlruns/{exp_id}/{run_id}/artifacts/Regression-Elastic-Net Model"
tag_id= '2.16.2'

image_url= aws_id + '.dkr.ecr.' +region+'.amazonaws.com/mlflow-pyfunc:'+ tag_id

mfs._deploy(app_name,
    model_uri=model_uri,
    region_name=region,
    mode='create',
    execution_role_arn=arn,
    image_url=image_url
)