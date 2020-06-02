import boto3
import pandas as pd

# install s3fs as a pip install
# Set up environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY (DO NOT STORE IT IN CODE)
# How to use secrets manager
# https://docs.aws.amazon.com/code-samples/latest/catalog/python-secretsmanager-secrets_manager.py.html

initial_matrix = pd.read_csv('s3n://srirambaskaraniristestbucket/iris.csv')

print initial_matrix
