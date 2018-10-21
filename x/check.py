#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 jack <jack@6k>
#
# Distributed under terms of the MIT license.

"""
check rate
"""

import urllib2
import json
import os
import ConfigParser

cf = ConfigParser.ConfigParser()
prefix = os.path.dirname(os.path.abspath(__file__))
cf.read(prefix + '/check.conf')
api_url = cf.get("default", "api_url")
threshold = cf.getint("default", "threshold")

def main():
    r = urllib2.urlopen(api_url)
    if r.getcode() != 200:
        report(0)
    d = json.loads(r.read().replace('\n', ''))
    single_hashrate_60s = d[u'hashrate'][u'total'][1] / len(d[u'hashrate'][u'threads'])
    if single_hashrate_60s < threshold:
        report(single_hashrate_60s)

def report(value):
    print value

def test():
    report(20)

if __name__ == "__main__":
    main()
