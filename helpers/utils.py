import json
import time

import pytest
from faker import Faker

faker = Faker()


def allure_attach(description, data):
    if isinstance(data, (list, tuple)):
        if all([isinstance(d, str) for d in data]):
            data = '\n'.join(data)
        else:
            converted_data = []
            for d in data:
                try:
                    converted_data.append(d.__dict__)
                except:
                    converted_data.append(d)
            data = converted_data

    if not isinstance(data, str):
        data = str(data)

    pytest.allure.attach(description, data)


def current_timestamp():
    return int(time.time())


def request_as_curl(url, method=None, data=None, params=None, headers=None, cookies=None):
    """ Build from request data as curl format """
    curl = 'curl '
    if method:
        curl += '-X %s ' % method

    curl += url

    if data:
        curl += ' -d \'%s\'' % json.dumps(data)

    if params:
        if isinstance(params, str):
            params = json.loads(params)

        curl += '/?%s' % '&'.join(['%s=%s' % (key, value) for (key, value) in params.items()])

    if headers:
        curl = '%s %s' % (curl, ' '.join(['-H \'%s:%s\'' % (key, value) for (key, value) in headers.items()]))

    if cookies:
        curl += ' -H \'Cookie: %s\'' % ";".join(['%s=%s' % (key, value) for (key, value) in cookies.items()])

    return curl
