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
from qu.la_internal.models.handler_payload import HandlerPayload  # noqa: E501
from qu.la_internal.rest import ApiException

class TestHandlerPayload(unittest.TestCase):
    """HandlerPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HandlerPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HandlerPayload`
        """
        model = qu.la_internal.models.handler_payload.HandlerPayload()  # noqa: E501
        if include_optional :
            return HandlerPayload(
                id = '', 
                event = '', 
                payload = ''
            )
        else :
            return HandlerPayload(
        )
        """

    def testHandlerPayload(self):
        """Test HandlerPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
