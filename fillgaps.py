#!/usr/bin/env python3

import os
import re


def get_pattern(file_prefix):
    pattern = re.compile(r"""^(file_prefix) # file_prefix
    (\d+)""", re.VERBOSE            # file number
                         )
    return pattern


def file_gap(folder):
    pass
