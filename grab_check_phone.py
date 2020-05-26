import requests
from requests import ConnectTimeout
from requests.exceptions import ProxyError
import common
import json


def try_register_phone(phone, session: requests.Session):
    data = f'method=SMS&countryCode=RU&phoneNumber={phone}&templateID=pax_android_production&numDigits=6'
    headers = {
            'x-ray': 'eyJpIjoibTIiLCJjIjoiaGVsbGZpcmU+MXVxbm0iLCJ2IjoieS4xLjMuNCIsImsiOjc4NTgxODY1fQ==',
            'x-request-id': '7bbdcc88-6e2d-43f0-a480-fa3d51faabf7',
            'content-encoding': 'gzip',
            'accept-language': 'en-US;q=1.0, en;q=0.9',
            'user-agent': 'Grab/5.97.0 (Android 5.0; Build 15521905)',
            'content-type': 'application/x-www-form-urlencoded',
            'content-length': '95',
            'accept-encoding': 'gzip',
              }
    try:
        r = session.post('https://api.grab.com/grabid/v1/phone/otp', timeout=20, headers=headers, data=data)
        print(r.status_code)
    except ConnectTimeout:
        raise ProxyError()
    except json.JSONDecodeError:
        raise ('unexpected answer')



session = requests.Session()
session.verify = "w.pem"
try_register_phone(79857736639, session)


