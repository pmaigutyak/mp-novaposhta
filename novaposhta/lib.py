
import httplib
import json

from novaposhta.settings import NOVA_POSHTA_API_KEY
from novaposhta.models import Warehouse


def refresh_warehouses():

    api_domain = 'api.novaposhta.ua'

    method = 'POST'

    url = '/v2.0/json/AddressGeneral/getWarehouses'

    headers = {
        'Content-Type': 'application/json'
    }

    body = json.dumps({
        'modelName': 'AddressGeneral',
        'calledMethod': 'getWarehouses',
        'apiKey': NOVA_POSHTA_API_KEY
    })

    try:
        conn = httplib.HTTPConnection(api_domain)

        conn.request(method, url, body, headers)

        response_data = json.loads(conn.getresponse().read())

        if response_data.get('success') is not True:
            raise Exception

        Warehouse.objects.all().delete()

        for item in response_data.get('data'):
            Warehouse.objects.create(
                title_uk=item.get('Description'),
                title_ru=item.get('DescriptionRu'),
                address_uk=item.get('CityDescription'),
                address_ru=item.get('CityDescriptionRu'),
            )

        conn.close()
    except Exception as e:
        print(e)