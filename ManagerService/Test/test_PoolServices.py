__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from unittest import TestCase
from ..PoolServices import PoolService
from ..ServiceException import ServiceException


class TestPoolService(TestCase):
    services = [
        'postgresql', 'cups',
    ]

    def test_CreatePoolServices(self):
        pool = PoolService()
        self.assertEqual(pool.GetListService(), sorted(self.services))

    def test_CommandUncorrectServicename(self):
        pool = PoolService()
        self.assertRaises(ServiceException, pool.StartService, 'test')
        self.assertRaises(ServiceException, pool.StartService, 'test')
        self.assertRaises(ServiceException, pool.GetStatusService, 'test')
        self.assertRaises(ServiceException, pool.GetDescriptionService, 'test')
        self.assertRaises(ServiceException, pool.GetActiveStatusService, 'test')
        self.assertRaises(ServiceException, pool.ActivateService, 'test')
        self.assertRaises(ServiceException, pool.DeactivateService, 'test')
        self.assertRaises(ServiceException, pool.RestartService, 'test')

    # def test_DescriptionService(self):
    #     pool = PoolService()
    #     for name in self.services:
    #         self.assertEqual(name, pool.GetDescriptionService(name))

    def test_ManagedService(self):
        pool = PoolService()
        for name in self.services:
            pool.StopService(name)
            self.assertEqual(pool.GetStatusService(name), 'inactive')
            pool.RestartService(name)
            self.assertEqual(pool.GetStatusService(name), 'active')
            pool.StopService(name)
            self.assertEqual(pool.GetStatusService(name), 'inactive')

        for name in self.services:
            pool.StartService(name)
            self.assertEqual(pool.GetStatusService(name), 'active')
            pool.RestartService(name)
            self.assertEqual(pool.GetStatusService(name), 'active')

    def test_ActivateService(self):
        pool = PoolService()
        for name in self.services:
            pool.StopService(name)
            self.assertEqual(pool.GetStatusService(name), 'inactive')
            pool.DeactivateService(name)
            pool.StartService(name)
            self.assertEqual(pool.GetStatusService(name), 'inactive')
            pool.ActivateService(name)

        for name in self.services:
            pool.StartService(name)
            self.assertEqual(pool.GetStatusService(name), 'active')
            pool.DeactivateService(name)
            pool.StopService(name)
            self.assertEqual(pool.GetStatusService(name), 'active')
            pool.ActivateService(name)

    def test_SaveInActiveService(self):
        pool = PoolService()
        for name in self.services:
            pool.DeactivateService(name)

        pool = PoolService()
        for name in self.services:
            self.assertFalse(pool.GetActiveStatusService(name))
            pool.ActivateService(name)



