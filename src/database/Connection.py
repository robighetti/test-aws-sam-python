#%%
import boto3
from cassandra.cluster import Cluster, Session, dict_factory
from cassandra.auth import PlainTextAuthProvider
from cassandra.policies import RoundRobinPolicy, TokenAwarePolicy

from json import loads
from src.utils.logger import logger
from src.utils.constants import env

passion_secret_id = f"commercial/{env}/scylla/database/elo/username/apaixonada_user_secret"

class Connection:
  def __init__(self, secret_id: str):
    try:
      #client = boto3.client("secretsmanager")
      #response = client.get_secret_value(SecretId=secret_id)      
      response = {
          "Name": "commercial/dev/scylla/database/passion/username/apaixonada_user_secret",
          "VersionId": "803410cb-3edf-41c3-b268-64884898d564",
          "SecretString": "{\"username\": \"apaixonada_user_secret\", \"password\": \"LksjK1232kasS\", \"engine\": \"scylla\", \"host\": \"scylla-dev-node01.dev.naturacloud.com,scylla-dev-node02.dev.naturacloud.com,scylla-dev-node03.dev.naturacloud.com\" , \"host_rr\": \"scylla-dev-node01.dev.naturacloud.com,scylla-dev-node02.dev.naturacloud.com,scylla-dev-node03.dev.naturacloud.com\", \"dbname\": \"passion\", \"port\": 9042}",
          "VersionStages": [
              "AWSCURRENT"
          ],
          "CreatedDate": 1671647078.048,
          "ARN": "arn:aws:secretsmanager:us-east-1:352865225993:secret:commercial/dev/scylla/database/elo/username/apaixonada_user_secret-FDKrU3"
      }
      
      secret_string = loads(response["SecretString"])
      db_user = secret_string.get("username")
      db_pass = secret_string.get("password")
      db_host = secret_string.get("host").split(",")
      
      logger.info("secrets recuperado com sucesso")
    except Exception as e:
      logger.error("erro na obtenção das credenciais")

    try:
      auth_provider = PlainTextAuthProvider(username=db_user, password=db_pass)
      cluster = Cluster(
          contact_points=db_host,
          auth_provider=auth_provider,
          load_balancing_policy=TokenAwarePolicy(RoundRobinPolicy()),
      )
      self.session: Session = cluster.connect()
      self.session.row_factory = dict_factory
    except Exception as e:
      logger.error("Erro ao abrir a conexão:" + str(e))

passion_conn = Connection(passion_secret_id)