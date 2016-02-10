# -*- coding: utf-8 -*-
import re


HASATTR_RE = re.compile(r'(^|.*\s)(?P<h>hasattr)\(.+\).*')


class PloneHasattrChecker(object):
    name = 'flake8_plone_hasattr'
    version = '0.1'
    message = 'P002 found "hasattr", consider replacing it'

    def __init__(self, tree=None, filename=None, lines=None):
        self.filename = filename
        self.lines = lines

    def run(self):
        if self.filename:
            with open(self.filename) as f:
                self.lines = f.readlines()

        for lineno, line in enumerate(self.lines, start=1):
            found = HASATTR_RE.search(line)
            if found:
                yield lineno, line.find('hasattr'), self.message, type(self)
