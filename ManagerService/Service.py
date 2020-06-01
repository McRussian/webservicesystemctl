__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from subprocess import PIPE, run
from .ServiceException import ServiceException


class Service:
    '''
    Объект этого класса представляет собой обертку для управления конкретным сервисом
    Для создание такой обертки нужны имя сервиса.
    В качестве управления понимается: start, stop
    Управление происходит посредством системной команды systemctl
    '''
    _name = None
    _description = None
    _status = None
    _is_active = None

    def __init__(self, name:str):
        self._name = name
        self._is_active = True
        if not self._CheckServiceName():
            raise ServiceException(1, 'Error Create Service')
        try:
            self._ReadDescriptionService()
        except ServiceException as err:
            self._description = 'Unknown Service'

    def GetName(self)-> str:
        return self._name

    def GetDescription(self)-> str:
        return self._description

    def GetStatus(self)-> str:
        self._ReadStatusService()
        return self._status

    def StartService(self):
        if self._is_active:
            if not self._RunCommand('start') == 0:
                raise ServiceException(13, 'Service ' + self._name + ' not Started!!!')

    def StopService(self):
        if self._is_active:
            if not self._RunCommand('stop') == 0:
                raise ServiceException(15, 'Service ' + self._name + ' not Stoped!!!')

    def Enable(self):
        self._is_active = True

    def Disable(self):
        self._is_active = False

    def GetActiveStatus(self)-> bool:
        return self._is_active

    def _CheckServiceName(self)-> bool:
        command = ['systemctl', 'status', self._name]
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        if result.stdout.split('\n')[0] == '':
            return False
        else:
            return True

    def _ReadDescriptionService(self):
        command = ['systemctl', 'status', self._name]
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)

        try:
            fullname = result.stdout.split('\n')[0]
            self._description = ' '.join(fullname.split()[3:])
        except:
            raise ServiceException(11, 'Service not Read Description')

    def _ReadStatusService(self):
        command = ['systemctl', 'status', self._name]
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)

        try:
            status_service = result.stdout.split('\n')[2]
            self._status = status_service.split()[1]
        except:
            raise ServiceException(11, 'Service not Read Description')

    def _RunCommand(self, command: str) -> int:
        command = ['sudo', 'systemctl', command, self._name]
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        return result.returncode