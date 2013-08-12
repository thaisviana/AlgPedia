# -*- coding: utf-8 -*-

import os.path

try:
    from local import *
except ImportError:
    from production import *
