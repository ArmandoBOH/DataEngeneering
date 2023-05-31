import os
import requests
import redshift_connector
import tqdm as t
import logging as log
from datetime import datetime


debug = os.environ.get('DEBUG')
log.basicConfig(
    format='%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s',
    level= log.INFO if debug is None or debug.upper() == 'FALSE' else log.DEBUG,  # Nivel de los eventos que se registran en el logger
)

# Obtén las credenciales de las variables de entorno
api_key = os.environ.get('API_KEY')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

log.info('Realiza la llamada a la API')
url = 'https://api.coincap.io/v2/rates'
response = requests.get(url)

# si responde ok
if response.status_code == 200:
    # Guardo los datos de la respuesta en formato json.
    data = response.json()
else:
    log.error("Error al momento de hacer el request")
    exit(1)

timestamp = data['timestamp']/1000
timestamp = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
assets = data['data']

# Me conecto a amazon redshift
conn = redshift_connector.connect(
    host=db_host,
    port=int(db_port),
    database=db_name,
    user=db_user,
    password=db_password
)

# Crea una tabla en Redshift si no existe
cur = conn.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS currency_data ( currency_symbol VARCHAR(10),id VARCHAR(100),rate_usd DECIMAL(18, 10),symbol VARCHAR(10),type VARCHAR(20),update_date TIMESTAMP);'

cur.execute(create_table)

log.info('Comienzo a insertar')
# Inserta los datos procesados en la tabla
for asset in t.tqdm(assets):
    query_insert = f"insert into currency_data (currency_symbol, id, rate_usd, symbol, type, update_date) " \
                   f"values ('{asset['currencySymbol']}','{asset['id']}',{asset['rateUsd']},'{asset['symbol']}','{asset['type']}','{timestamp}');"
    log.debug(query_insert)
    cur.execute(query_insert)
log.info('Termino el proceso de insercion')

log.info('Confirmo la transaccion')
conn.commit()
log.info('Cierro la conexcion')
conn.close()
log.info('Termine')