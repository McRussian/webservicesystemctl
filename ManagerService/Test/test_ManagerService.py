__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from unittest import TestCase
from ..ManagerService import ManagerService
from ..ServiceException import ServiceException
from Logger import Logger

class TestManagerService(TestCase):
    _logger = Logger()

    def test_UncorrectCommand(self):
        manager = ManagerService(self._logger)
        self.assertRaises(ServiceException, manager.RunCommand, 'test', 'test')
        self.assertRaises(ServiceException, manager.RunCommand, 12, 'test')
        self.assertRaises(ServiceException, manager.RunCommand, 'test', 12)