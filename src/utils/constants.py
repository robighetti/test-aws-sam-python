#%% 
from os import getenv

def set_env():
    return getenv("lambda_env")

env = set_env()

lambda_name = getenv('lambda_name')