__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from subprocess import PIPE, run
from .Service import Service
from .ServiceException import ServiceException


class PoolService:
    '''
    Объект этого класса представляет собой список всех существующих сервисов
    Он позволяет управлять сервисами с помощью своего интерфейса
    '''

    _services = None
    _commands = None

    def __init__(self):
        self._services = dict()
        self._InitPoolService()

    def GetListService(self)-> list:
        return sorted(list(self._services.keys()))

    def StartService(self, servicename:str):
        self._CheckNameService(servicename=servicename)
        self._services[servicename].StartService()

    def StopService(self, servicename:str):
        self._CheckNameService(servicename=servicename)
        self._services[servicename].StopService()

    def GetStatusService(self, servicename:str)-> str:
        self._CheckNameService(servicename=servicename)
        return self._services[servicename].GetStatus()

    def GetDescriptionService(self, servicename:str)-> str:
        self._CheckNameService(servicename=servicename)
        return self._services[servicename].GetDescription()

    def GetActiveStatusService(self, servicename: str)-> bool:
        self._CheckNameService(servicename=servicename)
        return self._services[servicename].GetActiceStatus()

    def ActivateService(self, servicename: str):
        self._CheckNameService(servicename=servicename)
        self._services[servicename].Enable()

    def DeactivateService(self, servicename: str):
        self._CheckNameService(servicename=servicename)
        self._services[servicename].Disable()

    def _InitPoolService(self):
        command = ['systemctl', '-a', '--type=service', '--no-legend']
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)

        if result.returncode == 0:
             list_service = result.stdout.split('\n')

        else:
            raise ServiceException(21, 'Not initialize List Service')

        for item in list_service:
            if item == '':
                continue
            name = '.'.join(item.split()[0].split('.')[:-1])
            try:
                service = Service(name=name)
                self._services[name] = service
            except ServiceException as err:
                pass

    def _CheckNameService(self, servicename: str):
        if not servicename in self._services.keys():
            raise ServiceException(23, 'Unknown Name of Service')

