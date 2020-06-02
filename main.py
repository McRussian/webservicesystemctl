__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from WebService.WebService import WebService
from Logger import Logger
from ManagerService.ManagerService import ManagerService

if __name__ == '__main__':
    logger = Logger()
    manager = ManagerService(logger=logger)
    webservice = WebService(manager=manager, logger=logger)
    webservice.Start()