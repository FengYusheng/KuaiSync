# -*- coding: utf-8 -*-
from P4 import P4, P4Exception

import json


class P4Client(P4):
    """
    Programming with p4python:

    https://www.perforce.com/manuals/p4python/Content/P4Python/python.programming.html#Programming_with_P4Python
    """
    def __init__(self, port='1666'):
        super(P4Client, self).__init__()
        self.port = port
        # We can't add our own attribute when inheriting the P4 class. This limitation should be from the
        # p4python cpp implementation:
        # https://github.com/rptb1/p4python/blob/master/P4API.cpp#L391
        # self.water = 'water'

    def ping(self):
        """
        Validate if the server is reachable.
        :return:
        """
        try:
            self.connect()
            info = self.run('info')
            print(json.dumps(info, indent=4, ensure_ascii=False))
        except P4Exception as e:
            print('p4 errors: {0}'.format(e))
        finally:
            self.disconnect()


if __name__ == '__main__':
    client = P4Client()
    client.ping()
