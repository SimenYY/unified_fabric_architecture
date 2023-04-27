# encoding:utf-8

import json
import importlib
import os
from common.singleton import Singleton


class PluginManager(metaclass=Singleton):
    # set static variable to store plugin path.
    __pluginPath = 'pass'

    def __int__(self, name, bases, dict):
        pass
