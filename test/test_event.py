# coding: utf-8

"""
    LiveAgent Async Event API

    This API is for async event communication  # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Contact: mcivan@qualityunit.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import qu.la_internal
from qu.la_internal.models.event import Event  # noqa: E501
from qu.la_internal.rest import ApiException

class TestEvent(unittest.TestCase):
    """Event unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Event
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Event`
        """
        model = qu.la_internal.models.event.Event()  # noqa: E501
        if include_optional :
            return Event(
                id = '', 
                topic = ''
            )
        else :
            return Event(
        )
        """

    def testEvent(self):
        """Test Event"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
