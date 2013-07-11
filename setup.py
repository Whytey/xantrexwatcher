#!/usr/bin/env python

from distutils.core import setup
import os

version = '0.01'

data = dict(
    name = 'xantrexWatcher',
    version = version,
    description = 'xantrexWatcher - A script to monitor a Xantrex inverter and report status to Zabbix',
    author = 'David Whyte',
    author_email = 'david@thewhytehouse.org',

    scripts = ['xantrexWatcher'],
    data_files = [('/etc/init', ['xantrexWatcher.conf'])],
    )


setup(**data)
