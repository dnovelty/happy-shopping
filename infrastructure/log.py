#!/usr/bin/env python
# -*- encoding=utf8 -*-
import logging
import logging.handlers
import os
LOG_FILENAME = 'jd-assistant.log'

logger = logging.getLogger()
try:
    os.remove('E:\workspace\ideaProjects\jd-assistant\jd-assistant.log')
except Exception as e:
    e

def set_logger():
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILENAME, maxBytes=10485760, backupCount=5, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


set_logger()
