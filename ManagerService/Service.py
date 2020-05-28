__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from subprocess import PIPE, run
from .ServiceException import ServiceException


class Service:
    '''
    Объект этого класса представляет собой обертку для управления конкретным сервисом
    Для создание такой оберкти нужны имя сервиса и имя пользователя системы,
    от лица которого будет происходить управление сервисом.
    В качестве управления понимается: start, stop
    Управление происходит посредством системной команды systemctl
    '''
    _name = None
    _description = None
    _username = None

    def __init__(self, name:str, username:str):
        self._name = name
        self._username = username

        try:
            self._ReadDescriptionService()
        except ServiceException as err:
            raise ServiceException(1, 'Error Create Service')


    def GetName(self)-> str:
        return self._name

    def GetDescription(self)-> str:
        return self._description

    def _ReadDescriptionService(self):
        command = ['systemctl', 'status', self._name]
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)

        if result.returncode == 0:
            fullname = result.stdout.split('\n')[0]
            self._description = ' '.join(fullname.split()[3:])
        else:
            raise ServiceException(11, 'Service not Read Description')