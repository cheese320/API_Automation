# !/user/bin/python
# -*- coding: utf-8 -*-

import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction' : 'transactions.log'
}



