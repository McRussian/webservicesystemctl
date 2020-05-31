__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from subprocess import PIPE, run
from .Service import Service
from .ServiceException import ServiceException


class PoolService:
    '''
    Объект этого класса представляет собой список всех существующих сервисов
    Он позволяет управлять сервисами с помощью своего интерфейса
    Для управления сервисами необходимо имя пользователя системы,
    от лица которого происходит управления
    '''

    _services = None
    _username = None

    def __init__(self, username:str):
        self._services = dict()
        self._username = username
        self._InitPoolService()


    def GetListService(self)-> list:
        return sorted(list(self._services.keys()))


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
                service = Service(name=name, username=self._username)
                self._services[name] = service
            except ServiceException as err:
                pass



