from mlflow.models import build_docker
from mlflow.deployments import get_deploy_client
model_name='Elastic Net'
        # model_uri = f"runs:/{run_id}/model"
        # result=mlflow.register_model(model_uri,model_name)
model_version=4
model_uri=f"models:/{model_name}/{model_version}"

build_docker(name="mlflow-pyfunc")

client = get_deploy_client("sagemaker")
client.run_local(
    name="my-local-deployment",
    model_uri="models:/Elastic Net/2",
    flavor="python_function",
    config={
        "port": 5000,
        "image": "mlflow-pyfunc",
    },
) 