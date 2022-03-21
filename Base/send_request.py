# !/user/bin/python
# -*- coding: utf-8 -*-
import json
import requests

from log import log

def http_request(url, http_method, http_payload):
    if http_payload:
        json_data = json.loads(http_payload)
    else:
        json_data = None

    headers = {'Content-Type': 'application/json'}
    response = requests.request(http_method, url,headers=headers, json=json_data)
    log.logger.debug(f'http response:  {response.text}')
    return response



