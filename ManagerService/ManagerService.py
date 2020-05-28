__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

class ManagerService:
    '''
    Объект этого класса является контроллером сервисов системы
    Он содержит словарь всех сервисов, которыми управляет.
    Для управления предоставляет набор функций.
    Для управления сервисами необходимо имя пользователя системы,
    от лица которого происходит управления
    '''

    _username = None
    _services = None

    def __init__(self, username: str):
        self._username = username