#!/usr/bin/env python

from distutils.core import setup

version = '0.02'

data = dict(
    name = 'xantrexWatcher',
    version = version,
    description = 'xantrexWatcher - A script to monitor a Xantrex inverter and report status to external parties.  Supports Zabbix and PVOutput.org',
    author = 'David Whyte',
    author_email = 'david@thewhytehouse.org',

    scripts = ['xantrexWatcher'],
    data_files = [('/etc/init', ['xantrexWatcher.conf']), ('/etc/xantrexWatcher', ['xantrexWatcher.ini.default'])],
    )


setup(**data)
