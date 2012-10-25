# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
import psd_tools.reader

DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'psd_files')

def load_psd(filename):
    full_filename = os.path.join(DATA_PATH, filename)
    with open(full_filename, 'rb') as f:
        return psd_tools.reader.parse(f)