__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from unittest import TestCase
from ..Service import Service
from ..ServiceException import ServiceException


class TestService(TestCase):
    services = [
        'postgresql', 'cups',
    ]
    def test_CreateUncorrectService(self):
        self.assertRaises(ServiceException, Service, 'test')

    def test_DescriptionService(self):
        nameservice = {
            'vmware': 'LSB: This service starts and stops VMware services',
            'ufw': 'Uncomplicated firewall',
            'sddm': 'Simple Desktop Display Manager',
            'cups': 'CUPS Scheduler'
        }

        for name in nameservice.keys():
            service = Service(name=name)
            self.assertEqual(nameservice[name], service.GetDescription())

    def test_ManagedService(self):
        for name in self.services:
            service = Service(name=name)
            service.StopService()
            self.assertEqual(service.GetStatus(), 'inactive')

        for name in self.services:
            service = Service(name=name)
            service.StartService()
            self.assertEqual(service.GetStatus(), 'active')

    def test_ActivateService(self):
        for name in self.services:
            service = Service(name=name)
            service.StopService()
            self.assertEqual(service.GetStatus(), 'inactive')

            service.Disable()
            service.StartService()
            self.assertEqual(service.GetStatus(), 'inactive')

        for name in self.services:
            service = Service(name=name)
            service.StartService()
            status = service.GetStatus()
            self.assertEqual(status, 'active')

            service.Disable()
            service.StopService()
            self.assertEqual(service.GetStatus(), 'active')
