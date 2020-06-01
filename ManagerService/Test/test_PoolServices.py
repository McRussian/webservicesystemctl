__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from unittest import TestCase
from ..PoolServices import PoolService
from ..ServiceException import ServiceException


class TestPoolService(TestCase):
    nameservice = {
        'vmware': 'LSB: This service starts and stops VMware services',
        'ufw': 'Uncomplicated firewall',
        'cups': 'CUPS Scheduler'
    }

    def test_CreatePoolServices(self):
        services = [
            'accounts-daemon', 'acpid', 'alsa-restore', 'alsa-state', 'anacron', 'anydesk', 'apparmor',
            'apport-autoreport', 'apport', 'apt-daily-upgrade', 'apt-daily', 'avahi-daemon', 'console-setup',
            'cron', 'cups-browsed', 'cups', 'dbus', 'emergency', 'fstrim',
            'getty-static', 'getty@tty1', 'gpu-manager', 'grub-common', 'irqbalance', 'kerneloops',
            'keyboard-setup', 'kmod-static-nodes', 'ModemManager', 'motd-news', 'mountcifs', 'mpd',
            'networkd-dispatcher', 'NetworkManager-wait-online', 'NetworkManager', 'ondemand',
            'packagekit', 'plymouth-quit-wait', 'plymouth-quit', 'plymouth-read-write', 'plymouth-start', 'polkit',
            'postgresql', 'postgresql@10-main', 'pppd-dns', 'rc-local', 'rescue', 'rsync', 'rsyslog', 'rtkit-daemon',
            'sddm', 'setvtrgb', 'snapd.autoimport', 'snapd.core-fixup', 'snapd.failure', 'snapd.seeded', 'snapd',
            'snapd.snap-repair', 'sysstat', 'systemd-ask-password-console', 'systemd-ask-password-plymouth',
            'systemd-ask-password-wall', 'systemd-binfmt', 'systemd-fsck-root', 'systemd-fsckd', 'systemd-hwdb-update',
            'systemd-initctl', 'systemd-journal-flush', 'systemd-journald', 'systemd-logind',
            'systemd-machine-id-commit', 'systemd-modules-load', 'systemd-networkd', 'systemd-random-seed',
            'systemd-remount-fs', 'systemd-resolved', 'systemd-rfkill', 'systemd-sysctl',
            'systemd-timesyncd', 'systemd-tmpfiles-clean', 'systemd-tmpfiles-setup-dev', 'systemd-tmpfiles-setup',
            'systemd-udev-trigger', 'systemd-udevd', 'systemd-update-utmp-runlevel',
            'systemd-update-utmp', 'systemd-user-sessions', 'teamviewerd', 'thermald',
            'udisks2', 'ufw', 'unattended-upgrades', 'upower', 'ureadahead-stop', 'ureadahead', 'user@1000', 'uuidd',
            'virtualbox', 'vmware-USBArbitrator', 'vmware', 'whoopsie', 'wpa_supplicant'
        ]

        pool = PoolService()
        self.assertEqual(pool.GetListService(), sorted(services))

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

    def test_DescriptionService(self):
        pool = PoolService()
        for name in self.nameservice.keys():
            self.assertEqual(self.nameservice[name], pool.GetDescriptionService(name))

    def test_ManagedService(self):
        pool = PoolService()
        for name in self.nameservice.keys():
            pool.StopService(name)
            self.assertEqual(pool.GetStatusService(name), 'inactive')
            pool.RestartService(name)
            self.assertEqual(pool.GetStatusService(name), 'active')
            pool.StopService(name)
            self.assertEqual(pool.GetStatusService(name), 'inactive')

        for name in self.nameservice.keys():
            pool.StartService(name)
            self.assertEqual(pool.GetStatusService(name), 'active')
            pool.RestartService(name)
            self.assertEqual(pool.GetStatusService(name), 'active')

    def test_ActivateService(self):
        pool = PoolService()
        for name in self.nameservice.keys():
            pool.StopService(name)
            self.assertEqual(pool.GetStatusService(name), 'inactive')
            pool.DeactivateService(name)
            pool.StartService(name)
            self.assertEqual(pool.GetStatusService(name), 'inactive')
            pool.ActivateService(name)

        for name in self.nameservice.keys():
            pool.StartService(name)
            self.assertEqual(pool.GetStatusService(name), 'active')
            pool.DeactivateService(name)
            pool.StopService(name)
            self.assertEqual(pool.GetStatusService(name), 'active')
            pool.ActivateService(name)

    def test_SaveInActiveService(self):
        pool = PoolService()
        for name in self.nameservice.keys():
            pool.DeactivateService(name)

        pool = PoolService()
        for name in self.nameservice.keys():
            self.assertFalse(pool.GetActiveStatusService(name))
            pool.ActivateService(name)



