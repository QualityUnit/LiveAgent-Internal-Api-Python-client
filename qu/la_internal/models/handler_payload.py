# coding: utf-8

"""
    LiveAgent Async Event API

    This API is for async event communication  # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Contact: mcivan@qualityunit.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr

class HandlerPayload(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[StrictStr] = None
    event: Optional[StrictStr] = None
    payload: Optional[StrictStr] = None
    __properties = ["id", "event", "payload"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> HandlerPayload:
        """Create an instance of HandlerPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HandlerPayload:
        """Create an instance of HandlerPayload from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return HandlerPayload.parse_obj(obj)

        _obj = HandlerPayload.parse_obj({
            "id": obj.get("id"),
            "event": obj.get("event"),
            "payload": obj.get("payload")
        })
        return _obj

