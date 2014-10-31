#!/usr/bin/env python

import os
import shutil
import subprocess

rootdir = '/nfs/farm/g/lsst/u1/jobHarness'
ccd_id = 'debug'

tasks = ('fe55_analysis',
         'bright_pixels', 
         'dark_pixels',
         'read_noise',
         'dark_current',
         'cte',
         'prnu',
         'trap',
         'flat_pairs',
         'ptc',
         'qe',
         'crosstalk',
         'test_report')

for subdir in ('jh_archive', 'jh_stage'):
    for task in tasks:
        path = os.path.join(rootdir, subdir, 'CCD', ccd_id, task)
        if os.path.isdir(path):
            print "removing %s" % path
            command = 'rm -rf %s' % path
            print command
            subprocess.call(command, shell=True)
            
shutil.copy('data_only_fakelims.db', 'my_fakelims.db')
