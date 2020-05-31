__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from unittest import TestCase
from ..PoolServices import PoolService
from ..ServiceException import ServiceException


class TestPoolService(TestCase):

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

        pool = PoolService(username='user')
        self.assertEqual(pool.GetListService(), sorted(services))