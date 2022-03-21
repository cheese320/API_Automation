# !/user/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import _json
import logging

path = os.path.dirname(os.path.dorname(os.path.abspath(__file__)))

sys.path.append(path)
sys.path.insert(0,path)


from config import settings

def log(logging_type):
    logger = logging.getLogger(logging_type)
    logger.setLevel(settings.LOG_LEVEL)
    log_file = "%s\log\%s" %(settings.BASE_DIR, settings.LOG_TYPES[logging_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    #define format of log
    formatter = logging.Formatter("%(actime)s-%(name)s-%(levelname)s-%(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

