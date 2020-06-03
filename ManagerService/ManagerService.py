__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from singleton_decorator import singleton
from Logger import Logger
from .PoolServices import PoolService
from .ServiceException import ServiceException

@singleton
class ManagerService:
    '''
    Объект этого класса является контроллером сервисов системы
    Он содержит словарь всех сервисов, которыми управляет.
    Для управления предоставляет набор функций.
    '''

    _services = None
    _logger = None
    _commands = None
    def __init__(self, logger: Logger):
        self._logger = logger
        try:
            self._services = PoolService()
        except ServiceException as err:
            self._logger.Message(err.GetErrorMessage(), 'error')
            raise ServiceException(1, "Not Started Manager Service")

        self._commands = {
            'start': self._services.StartService,
            'stop':  self._services.StopService,
            'restart': self._services.RestartService,
            'activate': self._services.ActivateService,
            'deactivate': self._services.DeactivateService
        }

    def GetListService(self)-> list:
        ls_service = []
        for name in self._services.GetListService():
            try:
                ls_service.append(self._services.GetInfoService(servicename=name))
            except ServiceException as err:
                self._logger.Message(err.GetErrorMessage(), 'error')
        return ls_service

    def RunCommand(self, servicename: str, command: str):
        if (not type(servicename) == str) or (not type(command) == str):
            raise ServiceException(5, 'Bad Type for Servicename or Command')
        if not command in self._commands:
            raise ServiceException(7, 'Unknown command ' + command)
        try:
            self._commands[command](servicename=servicename)
            self._logger.Message('Service ' + servicename + ' running command ' + command, 'info')
        except ServiceException as err:
            self._logger.Message(err.GetErrorMessage(), 'error')
            raise ServiceException(3, 'Manager not Running Command ' + command + ' for Service ' + servicename)

