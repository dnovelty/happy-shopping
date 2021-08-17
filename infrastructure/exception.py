#!/usr/bin/env python
# -*- encoding=utf8 -*-
from infrastructure.log import logger


class BizException(Exception):

    def __init__(self, message):
        super().__init__(message)
        logger.error(message)
