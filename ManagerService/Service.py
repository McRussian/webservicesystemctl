__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from ManagerService.ServiceException import ServiceException

class Service:
    '''
    Объект этого класса представляет собой обертку для управления конкретным сервисом
    Для создание такой оберкти нужны имя сервиса и имя пользователя системы,
    от лица которого будет происходить управление сервисом.
    В качестве управления понимается: start, stop
    Управление происходит посредством системной команды systemctl
    '''
    _name = None
    _username = None

    def __init__(self, name:str, username:str):
        self._name = name
        self._username = username

    def GetName(self)-> str:
        return self._name

