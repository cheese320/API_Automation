# !/user/bin/python
# -*- coding: utf-8 -*-

import json
import os
from config import settings

def load_info(filename):
    doc = "%s\db\%s.json" %(settings.BASE_DIR, filename)
    if os.path.isfile(doc):
        with open(doc, "r", encoding='utf-8') as f:
            endPoints = json.load(f)
            return endPoints



