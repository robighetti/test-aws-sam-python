import json

from src.utils.logger import logger
from src.data.handler import Handler

def lambda_handler(event, context):  
    try:
      logger.info('start lambda function [${context.functionName}]');

      data = Handler.handler()

      return {
        "statusCode": 200,
        "body": json.dumps(event),
      }
    except Exception as e:
      print('ok')