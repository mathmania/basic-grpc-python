from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddRequest(_message.Message):
    __slots__ = ("value_1", "value_2")
    VALUE_1_FIELD_NUMBER: _ClassVar[int]
    VALUE_2_FIELD_NUMBER: _ClassVar[int]
    value_1: int
    value_2: int
    def __init__(self, value_1: _Optional[int] = ..., value_2: _Optional[int] = ...) -> None: ...

class AddReply(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: int
    def __init__(self, response: _Optional[int] = ...) -> None: ...
