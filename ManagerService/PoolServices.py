__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

import os
from .Service import Service
from .ServiceException import ServiceException


class PoolService:
    '''
    Объект этого класса представляет собой список сервисов
    Список берется из текстового файла services.cnf
    Он позволяет управлять сервисами с помощью своего интерфейса
    '''

    _services = None
    _commands = None
    _file_service = None
    _file_inactive_service = None

    def __init__(self):
        self._services = dict()
        self._file_service = os.path.dirname(__file__) + os.sep + 'service.cnf'
        self._file_inactive_service = os.path.dirname(__file__) + os.sep + 'inactive.service.cnf'
        self._InitPoolService()

    def GetListService(self)-> list:
        return sorted(list(self._services.keys()))

    def StartService(self, servicename:str):
        self._CheckNameService(servicename=servicename)
        self._services[servicename].StartService()

    def StopService(self, servicename:str):
        self._CheckNameService(servicename=servicename)
        self._services[servicename].StopService()

    def RestartService(self, servicename:str):
        self.StopService(servicename=servicename)
        self._services[servicename].StartService()

    def GetInfoService(self, servicename:str)-> dict:
        self.StopService(servicename=servicename)
        return self._services[servicename].GetInfo()

    def GetStatusService(self, servicename:str)-> str:
        self._CheckNameService(servicename=servicename)
        return self._services[servicename].GetStatus()

    def GetDescriptionService(self, servicename:str)-> str:
        self._CheckNameService(servicename=servicename)
        return self._services[servicename].GetDescription()

    def GetActiveStatusService(self, servicename: str)-> bool:
        self._CheckNameService(servicename=servicename)
        return self._services[servicename].GetActiveStatus()

    def ActivateService(self, servicename: str):
        self._CheckNameService(servicename=servicename)
        self._services[servicename].Enable()
        self._SaveStatusService()

    def DeactivateService(self, servicename: str):
        self._CheckNameService(servicename=servicename)
        self._services[servicename].Disable()
        self._SaveStatusService()

    def _SaveStatusService(self):
        fin = open(self._file_inactive_service, 'w')
        for name in self._services.keys():
            if not self._services[name].GetActiveStatus():
                fin.write(name + '\n')
        fin.close()

    def _InitPoolService(self):
        ls_service = self._ReadInactiveService(self._file_service)
        ls_inactive_service = self._ReadInactiveService(self._file_inactive_service)
        for name in ls_service:
            try:
                service = Service(name=name)
                self._services[name] = service
                if name in ls_inactive_service:
                    self._services[name].Disable()
            except ServiceException as err:
                pass

    def _CheckNameService(self, servicename: str):
        if not servicename in self._services.keys():
            raise ServiceException(23, 'Unknown Name of Service')

    def _ReadInactiveService(self, filename)-> list:
        try:
            fout = open(filename, 'r')
            ls = list(map(lambda s: s.strip('\n'), fout.readlines()))
            fout.close()
            return ls
        except:
            return []


