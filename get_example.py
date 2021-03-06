import os
from dotenv import load_dotenv
import http.client

latitude = "51.53239000197473"  # example latt/logt set
longitude = "-0.10646610354395085"

load_dotenv()

# connect to Weather DataHub
datahub_conn = http.client.HTTPSConnection("rgw.5878-e94b1c46.eu-gb.apiconnect.appdomain.cloud")

headers = {
    'X-IBM-Client-Id': os.getenv('DATAHUB_API_KEY'),
    'X-IBM-Client-Secret': os.getenv('DATAHUB_SECRET'),
    'accept': "application/json"
    }


datahub_conn.request("GET", f"/metoffice/production/v0/forecasts/point/hourly?excludeParameterMetadata=false&includeLocationName=true&latitude={latitude}&longitude={longitude}", headers=headers)

datahub_res = datahub_conn.getresponse()
datahub_json = datahub_res.read()


# data dump example
with open('dump.json', 'wb') as datahub_dump:
    datahub_dump.write(datahub_json)
    print("Data written to dump.json")
    datahub_dump.close()
