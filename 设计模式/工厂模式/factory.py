#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/7/31

import xml.etree.ElementTree as etree
import json

class JSONConnector(object):
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector(object):
    def __init__(self, filepath):
        self.etree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.etree

a = 'a'
print()