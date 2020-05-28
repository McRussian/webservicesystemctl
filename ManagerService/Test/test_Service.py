__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from unittest import TestCase
from ..Service import Service
from ..ServiceException import ServiceException


class TestService(TestCase):

    def test_CreateUncorrectService(self):
        self.assertRaises(ServiceException, Service, 'test', 'test')

    def test_DescriptionService(self):
        nameservice = {
            'vmware': 'LSB: This service starts and stops VMware services',
            'ufw': 'Uncomplicated firewall',
            'sddm': 'Simple Desktop Display Manager',
            'cups': 'CUPS Scheduler'
        }

        for name in nameservice.keys():
            service = Service(name=name, username='user')
            self.assertEqual(nameservice[name], service.GetDescription())