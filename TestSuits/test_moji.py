# !/user/bin/python
# -*- coding: utf-8 -*-

from Base import tools
from Base import send_request
import pytest


def test_http():
    api = tools.load_info("endPoints")["geography"]
    requestype = api["request"]
    url = api["url"]
    payload = api["payload"]

    response = send_request.http_requset(url,requestype,payload)
    assert response.status_code == "200"
    assert response.content.find("北京市")!=-1


if __name__ == '__main__':
    pytest.main()

