__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

class ServiceException (BaseException):
    _code = None
    _msg = None

    def __init__(self, code: int, msg: str):
        self._code = code
        self._msg = msg

    def GetErrorCode(self)-> int:
        return self._code

    def GetErrorMessage(self)-> str:
        return self._msg