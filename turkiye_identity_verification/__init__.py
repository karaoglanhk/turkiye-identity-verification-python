__all__ = ['native_citizen_verify', 'foreign_citizen_verify']

import http.client
import ssl
import re

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

def post(props):
    try:
        body = props['body']
        options = props['options']

        connection = http.client.HTTPSConnection(options['hostname'], options['port'], context=context)
        connection.request(options['method'], options['path'], body.encode('utf-8'), options['headers'])
        
        response = connection.getresponse()
        data = response.read().decode('utf-8')

        return data

    except Exception as e:
        raise e

def native_citizen_verify(identityNo:str, name:str, surname:str, birthYear:str):
    """
    Args:
        identityNo (str): etc. 11111111111
        name (str): etc. Hüseyin
        surname (str): etc. Karaoğlan
        birthYear (str): etc. 2000

    Returns:
        bool: True or False
    """
    
    try:
        body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    <soap12:Body>
        <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
        <TCKimlikNo>{identityNo}</TCKimlikNo>
        <Ad>{name}</Ad>
        <Soyad>{surname}</Soyad>
        <DogumYili>{birthYear}</DogumYili>
        </TCKimlikNoDogrula>
    </soap12:Body>
    </soap12:Envelope>"""

        request = post({
            'body': body,
            'options': {
                'port': 443,
                'method': 'POST',
                'path': '/Service/KPSPublic.asmx',
                'hostname': 'tckimlik.nvi.gov.tr',
                'headers': {'Content-Type': 'application/soap+xml'},
            },
        })

        search_pattern = r'<TCKimlikNoDogrulaResult>(.*?)<\/TCKimlikNoDogrulaResult>'
        found_part = re.search(search_pattern, request)

        return found_part and found_part.group(1) == 'true'

    except Exception as e:
        raise e

def foreign_citizen_verify(identityNo:str, name:str, surname:str, birthDate:str, birthMonth:str, birthYear:str):
    """
    Args:
        identityNo (str): etc. 99111111111
        name (str): etc. Hüseyin
        surname (str): etc. Karaoğlan
        birthDate (str): etc. 10
        birthMonth (str): etc. 8
        birthYear (str): etc. 2000

    Returns:
        bool: True or False
    """
    
    try:
        body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
      <soap:Body>
        <YabanciKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
          <KimlikNo>{identityNo}</KimlikNo>
          <Ad>{name}</Ad>
          <Soyad>{surname}</Soyad>
          <DogumGun>{birthDate}</DogumGun>
          <DogumAy>{birthMonth}</DogumAy>
          <DogumYil>{birthYear}</DogumYil>
        </YabanciKimlikNoDogrula>
      </soap:Body>
    </soap:Envelope>"""

        request = post({
            'body': body,
            'options': {
                'port': 443,
                'method': 'POST',
                'path': '/Service/KPSPublicYabanciDogrula.asmx',
                'hostname': 'tckimlik.nvi.gov.tr',
                'headers': {
                    'Content-Type': 'text/xml; charset=utf-8',
                    'SOAPAction': 'http://tckimlik.nvi.gov.tr/WS/YabanciKimlikNoDogrula',
                },
            },
        })

        search_pattern = r'<YabanciKimlikNoDogrulaResult>(.*?)<\/YabanciKimlikNoDogrulaResult>'
        found_part = re.search(search_pattern, request)

        return found_part and found_part.group(1) == 'true'

    except Exception as e:
        raise e
    
